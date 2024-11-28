import tkinter as tk
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image
from loguru import logger
from typing import Optional
import abc
import os
import sys
import time

from src.services.qr_processor import QRCodeProcessor
from src.services.screenshot_service import ScreenshotCapture
from src.services.clipboard_service import ClipboardService
from src.services.notification_service import NotificationService


def get_asset_path(relative_path):
    """Get the absolute path to an asset, handling PyInstaller paths."""
    if getattr(sys, "frozen", False):  # If running as a PyInstaller EXE
        base_path = sys._MEIPASS
    else:  # If running in development
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


class SnippingToolBase:
    """Abstract base class for snipping tool"""

    @abc.abstractmethod
    def initialize(self) -> None:
        """Create screen canvas for screenshot selection"""
        pass

    @abc.abstractmethod
    def hide_window(self) -> None:
        """Hide the snipping tool window"""
        pass


class TkinterSnippingTool(SnippingToolBase):
    """Tkinter-based implementation of snipping tool"""

    is_window_open = False

    def __init__(
        self,
        qr_processor: QRCodeProcessor,
        screenshot_service: ScreenshotCapture,
        clipboard_service: ClipboardService,
        notification_service: NotificationService,
    ):
        self.snip_surface: Optional[Canvas] = None
        self.master_screen: Optional[Tk] = None
        self.start_x: Optional[float] = None
        self.start_y: Optional[float] = None
        self.current_x: Optional[int] = None
        self.current_y: Optional[int] = None
        self.rect: Optional[int] = None
        self.is_window_open: bool = False
        self.cursor_moved: bool = False

        # Dependency injection
        self.qr_processor: QRCodeProcessor = qr_processor
        self.screenshot_service: ScreenshotCapture = screenshot_service
        self.clipboard_service: ClipboardService = clipboard_service
        self.notification_service: NotificationService = notification_service

    def hide_window(self, event: tk.Event = None) -> None:
        """Hide the snipping tool window"""
        logger.debug("Attempting to hide the snipping tool window")
        try:
            if self.master_screen and self.master_screen.winfo_exists():
                self.is_window_open = False

                # Animate window
                alpha = 0.3
        
                while alpha > 0:
                    alpha -= 0.01
                    self.master_screen.wm_attributes("-alpha", alpha)
                    self.master_screen.update()

                    time.sleep(0.01)

                self.master_screen.withdraw()
                logger.info("Snipping tool window successfully hidden")
        except Exception as e:
            logger.exception(f"Error hiding snipping tool window: {e}")
        finally:
            self.is_window_open = False

    def initialize(self) -> None:
        """Create a fullscreen canvas for screenshot selection"""
        if self.is_window_open:
            logger.warning("Snipping tool already open")
            return

        try:
            logger.info("Initializing snipping tool window")
            self.master_screen = Tk()
            self.master_screen.title("QR Grabber Overlay")

            app_icon = PhotoImage(file=get_asset_path("../../assets/icon.png"))
            self.master_screen.iconphoto(True, app_icon)
            
            self.master_screen.attributes("-transparent", "blue")
            self.master_screen.geometry(
                f"{self.master_screen.winfo_screenwidth()}x{self.master_screen.winfo_screenheight()}+0+0"
            )

            self.snip_surface = Canvas(self.master_screen, cursor="crosshair", bg="grey18")
            self.snip_surface.pack(fill=tk.BOTH, expand=tk.YES)

            self.snip_surface.bind("<ButtonPress-1>", self.on_button_press)
            self.snip_surface.bind("<B1-Motion>", self.on_snip_drag)
            self.snip_surface.bind("<ButtonRelease-1>", self.on_button_release)
            self.snip_surface.bind("<Escape>", self.hide_window)
            self.master_screen.bind("<Escape>", self.hide_window)

            self.master_screen.attributes("-fullscreen", True)
            self.master_screen.attributes("-topmost", True)
            self.master_screen.withdraw()

            self.master_screen.protocol("WM_DELETE_WINDOW", self.hide_window)
            self.master_screen.mainloop()
        except Exception as e:
            logger.exception(f"Error creating screen canvas: {e}")

    def show_window(self) -> None:
        """Show the snipping tool window when needed"""
        logger.debug("Attempting to show the snipping tool window")

        # Clear canvas
        try: self.snip_surface.delete("all")
        except Exception as e: logger.exception(f"Error clearing the `snip_surface` canvas: {e}")

        self.master_screen.wm_attributes("-alpha", 0)
        self.master_screen.deiconify()

        # Animate window
        alpha = 0

        while alpha < 0.3:
            alpha += 0.01
            self.master_screen.wm_attributes("-alpha", alpha)
            self.master_screen.update()

            time.sleep(0.01)

        self.is_window_open = True
        logger.info("Snipping tool window successfully displayed")

    def on_button_press(self, event: tk.Event) -> None:
        """Handle mouse button press for selecting screenshot area"""
        try:
            logger.debug("Button press detected for screenshot selection")
            self.cursor_moved = False
            self.start_x = self.snip_surface.canvasx(event.x)
            self.start_y = self.snip_surface.canvasy(event.y)
            self.rect = self.snip_surface.create_rectangle(
                self.start_x,
                self.start_y,
                self.start_x,
                self.start_y,
                outline="white",
                fill="blue",
                width=1,
            )
        except Exception as e:
            logger.exception(f"Error during button press: {e}")

    def on_snip_drag(self, event: tk.Event) -> None:
        """Update rectangle during mouse drag"""
        try:
            self.cursor_moved = True
            self.current_x, self.current_y = (event.x, event.y)
            self.snip_surface.coords(
                self.rect, self.start_x, self.start_y, self.current_x, self.current_y
            )
        except Exception as e:
            logger.exception(f"Error during snip drag: {e}")

    def on_button_release(self, event: tk.Event) -> None:
        """Process screenshot after selection"""
        try:
            # Calculate the coordinates relative to the screen
            x1: int = int(self.start_x)
            y1: int = int(self.start_y)
            x2: int = int(self.snip_surface.canvasx(event.x))
            y2: int = int(self.snip_surface.canvasy(event.y))

            left: int = min(x1, x2)
            top: int = min(y1, y2)
            width: int = abs(x2 - x1)
            height: int = abs(y2 - y1)

            logger.info(f"Screenshot selection: {left},{top} {width}x{height}")

            if not (width < 40 or height < 40):
                screenshot: Optional[Image.Image] = (
                    self.screenshot_service.take_bounded_screenshot(
                        left, top, width, height
                    )
                )
                # if screenshot:
                #     screenshot.show()  # Display the screenshot for debugging
                self.hide_window()
                self.process_screenshot(screenshot)
            else:
                if self.cursor_moved:
                    self.snip_surface.delete("all")
                    logger.warning("The selected area is too small")
                else:
                    # Close if the user only clicks and doesn't select anything.
                    logger.warning("No selection made, closing")
                    self.hide_window()
        except Exception as e:
            logger.exception(f"Error during button release: {e}")
            self.hide_window()

    def process_screenshot(self, image: Optional[Image.Image]) -> None:
        """Process detected screenshot for QR code"""
        try:
            data: Optional[str]
            success: bool
            data, success = self.qr_processor.detect_qr_code(image)

            if success and data:
                try:
                    self.clipboard_service.copy_to_clipboard(data)
                except Exception as e:
                    logger.exception(f"Error copying data to clipboard: {e}")

                sanitized_data = f"{data[:200]}..." if len(data) > 200 else data
                try:
                    self.notification_service.show_notification(
                        "QR Code Detected",
                        f"QR Code data copied to clipboard:\n\n{sanitized_data}",
                    )
                except Exception as e:
                    logger.exception(f"Error showing notification: {e}")
            else:
                try:
                    self.notification_service.show_notification(
                        "No QR Code Detected",
                        "No QR Code was detected in the screenshot.",
                    )
                except Exception as e:
                    logger.exception(f"Error showing notification: {e}")
        except Exception as e:
            logger.exception(f"Error processing screenshot: {e}")
