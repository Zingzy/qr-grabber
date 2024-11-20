import tkinter as tk
from tkinter import Tk, Canvas
from PIL import Image
from loguru import logger
from typing import Optional
import abc

from src.services.qr_processor import QRCodeProcessor
from src.services.screenshot_service import ScreenshotCapture
from src.services.clipboard_service import ClipboardService
from src.services.notification_service import NotificationService


class SnippingToolBase:
    """Abstract base class for snipping tool"""

    @abc.abstractmethod
    def create_screen_canvas(self) -> None:
        """Create screen canvas for screenshot selection"""
        pass

    @abc.abstractmethod
    def exit_program(self) -> None:
        """Exit the snipping tool"""
        pass


class TkinterSnippingTool(SnippingToolBase):
    """Tkinter-based implementation of snipping tool"""

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

        # Dependency injection
        self.qr_processor: QRCodeProcessor = qr_processor
        self.screenshot_service: ScreenshotCapture = screenshot_service
        self.clipboard_service: ClipboardService = clipboard_service
        self.notification_service: NotificationService = notification_service

    def exit_program(self, event: tk.Event = None) -> None:
        """Exit the snipping window"""
        logger.debug("Attempting to exit snipping tool")
        try:
            if self.master_screen and self.master_screen.winfo_exists():
                self.is_window_open = False
                self.master_screen.destroy()
                logger.info("Snipping tool closed successfully")
        except Exception as e:
            logger.exception(f"Error closing snipping tool: {e}")
        finally:
            self.is_window_open = False

    def create_screen_canvas(self) -> None:
        """Create a fullscreen canvas for screenshot selection"""
        if self.is_window_open:
            logger.warning("Snipping tool already open")
            return

        try:
            logger.info("Opening snipping tool")
            self.is_window_open = True
            self.master_screen = Tk()
            self.master_screen.attributes("-transparent", "blue")
            self.master_screen.geometry(
                f"{self.master_screen.winfo_screenwidth()}x{self.master_screen.winfo_screenheight()}+0+0"
            )
            self.master_screen.attributes("-alpha", 0.5)
            self.master_screen.attributes("-topmost", True)

            self.snip_surface = Canvas(self.master_screen, cursor="cross", bg="grey18")
            self.snip_surface.pack(fill=tk.BOTH, expand=tk.YES)

            self.snip_surface.bind("<ButtonPress-1>", self.on_button_press)
            self.snip_surface.bind("<B1-Motion>", self.on_snip_drag)
            self.snip_surface.bind("<ButtonRelease-1>", self.on_button_release)
            self.snip_surface.bind("<Escape>", self.exit_program)
            self.master_screen.bind("<Escape>", self.exit_program)
            self.master_screen.focus_force()  # Force focus on the window

            self.master_screen.attributes("-fullscreen", True)
            self.master_screen.attributes("-alpha", 0.3)
            self.master_screen.lift()
            self.master_screen.attributes("-topmost", True)

            self.master_screen.protocol("WM_DELETE_WINDOW", self.exit_program)
            self.master_screen.mainloop()
        except Exception as e:
            logger.exception(f"Error creating screen canvas: {e}")
            self.is_window_open = False

    def on_button_press(self, event: tk.Event) -> None:
        """Handle mouse button press for selecting screenshot area"""
        try:
            logger.debug("Button press detected for screenshot selection")
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
            self.current_x, self.current_y = (event.x, event.y)
            self.snip_surface.coords(
                self.rect, self.start_x, self.start_y, self.current_x, self.current_y
            )
        except Exception as e:
            logger.exception(f"Error during snip drag: {e}")

    def on_button_release(self, event: tk.Event) -> None:
        """Process screenshot after selection"""
        try:
            x1: int = int(self.start_x + self.master_screen.winfo_x())
            y1: int = int(self.start_y + self.master_screen.winfo_y())
            x2: int = int(event.x + self.master_screen.winfo_x())
            y2: int = int(event.y + self.master_screen.winfo_y())

            left: int = min(x1, x2)
            top: int = min(y1, y2)
            width: int = abs(x2 - x1)
            height: int = abs(y2 - y1)

            logger.info(f"Screenshot selection: {left},{top} {width}x{height}")

            screenshot: Optional[Image.Image] = (
                self.screenshot_service.take_bounded_screenshot(
                    left, top, width, height
                )
            )
            self.process_screenshot(screenshot)
            self.exit_program()
        except Exception as e:
            logger.exception(f"Error during button release: {e}")
            self.exit_program()

    def process_screenshot(self, image: Optional[Image.Image]) -> None:
        """Process detected screenshot for QR code"""
        try:
            data: Optional[str]
            success: bool
            data, success = self.qr_processor.detect_qr_code(image)

            if success and data:
                self.clipboard_service.copy_to_clipboard(data)
                self.notification_service.show_notification(
                    "QR Code Detected", f"QR Code data copied to clipboard:\n\n{data}"
                )
            else:
                self.notification_service.show_notification(
                    "No QR Code Detected", "No QR Code was detected in the screenshot."
                )
        except Exception as e:
            logger.exception(f"Error processing screenshot: {e}")
