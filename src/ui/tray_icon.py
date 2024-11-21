import threading
import keyboard
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageFile
from loguru import logger
from typing import Any, Callable


class TrayIconManager:
    """Manages system tray icon and menu"""

    def __init__(
        self,
        open_snipping_tool_callback: Callable,
        set_startup_registry: Callable[[bool], bool],
        is_startup_enabled: Callable[[], bool],
        icon_path: str = "assets/icon.png",
    ) -> None:
        self.open_snipping_tool_callback = open_snipping_tool_callback
        self.set_startup_registry = set_startup_registry
        self.is_startup_enabled = is_startup_enabled
        self.startup_enabled: bool = self.is_startup_enabled()
        self.tray_icon = None
        self.icon_path: str = icon_path
        self.stop_event: threading.Event = threading.Event()

    def create_tray_icon(self) -> None:
        """Create system tray icon with menu"""

        def toggle_startup(icon, item) -> None:
            """Toggle application startup on/off"""
            try:
                logger.info("Toggling application startup")
                self.startup_enabled = not self.startup_enabled
                success = self.set_startup_registry(self.startup_enabled)
                if success:
                    logger.info(
                        f"Run at startup {'enabled' if self.startup_enabled else 'disabled'}"
                    )
                else:
                    self.startup_enabled = not self.startup_enabled  # Revert if failed
                    logger.error("Failed to modify startup settings")
            except Exception as e:
                logger.exception(f"Error toggling startup setting: {e}")

        def quit_app(icon, item: Any) -> None:
            """Graceful application exit"""
            try:
                logger.info("Initiating application shutdown")

                # Stop keyboard hooks
                keyboard.unhook_all_hotkeys()
                logger.debug("Keyboard hooks removed")

                # Stop the tray icon
                if icon:
                    icon.stop()
                    logger.debug("Tray icon stopped")

                # Set stop event
                self.stop_event.set()
                logger.info("Application shutdown complete")
            except Exception as e:
                logger.exception(f"Error during quit: {e}")

        def open_snipping_tool(icon, item: Any) -> None:
            """Open snipping tool from tray menu"""
            try:
                logger.info("Opening snipping tool from tray menu")
                self.open_snipping_tool_callback()
            except Exception as e:
                logger.exception(f"Error opening snipping tool: {e}")

        # Create menu with error handling
        try:
            menu: Menu = Menu(
                MenuItem("Open Detection Tool", open_snipping_tool),
                MenuItem(
                    "Run at Startup",
                    toggle_startup,
                    checked=lambda item: self.startup_enabled,
                ),
                MenuItem("Quit", quit_app),
            )

            icon_image: ImageFile.Image = Image.open(self.icon_path)
            self.tray_icon = Icon("QR Grabber", icon_image, "QR Grabber", menu)
            logger.info("Tray icon created successfully")
            self.tray_icon.run()
        except Exception as e:
            logger.exception(f"Error creating tray icon: {e}")
