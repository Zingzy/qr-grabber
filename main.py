from src.config.logging_config import setup_logging
from src.services.screenshot_service import ScreenshotCapture
from src.services.qr_processor import QRCodeProcessor
from src.services.clipboard_service import ClipboardService
from src.services.notification_service import NotificationService
from src.ui.snipping_tool import TkinterSnippingTool
from src.ui.tray_icon import TrayIconManager
from src.utils.exceptions import handle_exception
from src.utils.startup_manager import set_startup_registry, is_startup_enabled
import threading
import sys
import keyboard
import os

# Setup logging at module import
logger = setup_logging()


class QRCodeDetectionApp:
    """Main application orchestrator"""

    def __init__(self):
        logger.info("Initializing QR Code Detection Application")
        # Dependency injection
        self.screenshot_service: ScreenshotCapture = ScreenshotCapture()
        self.qr_processor: QRCodeProcessor = QRCodeProcessor()
        self.clipboard_service: ClipboardService = ClipboardService()
        self.notification_service: NotificationService = NotificationService(
            app_icon=self.get_asset_path("assets/icon.ico")
        )

        # Create components
        self.snipping_tool: TkinterSnippingTool = TkinterSnippingTool(
            self.qr_processor,
            self.screenshot_service,
            self.clipboard_service,
            self.notification_service,
        )
        self.tray_icon_manager: TrayIconManager = TrayIconManager(
            self.snipping_tool.show_window,
            set_startup_registry,
            is_startup_enabled,
            self.get_asset_path("assets/icon.ico"),
        )

        # Initialize snipping tool window
        snipping_tool_thread = threading.Thread(
            target=self.snipping_tool.initialize, daemon=True
        )
        snipping_tool_thread.start()

    def listen_for_shortcut(self) -> None:
        """Set up keyboard shortcut and launch tray icon"""
        try:
            # Add keyboard shortcut
            keyboard.add_hotkey("ctrl+alt+q", self.snipping_tool.show_window)
            logger.info("Keyboard shortcut Ctrl+Alt+Q registered")

            # Create and run tray icon
            self.tray_icon_manager.create_tray_icon()
        except Exception as e:
            logger.exception(f"Error setting up application: {e}")

    def get_asset_path(self, relative_path):
        """Get the absolute path to an asset, handling PyInstaller paths."""
        if getattr(sys, "frozen", False):  # If running as a PyInstaller EXE
            base_path = sys._MEIPASS
        else:  # If running in development
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)

    def run(self) -> None:
        """Start the application"""
        try:
            logger.info("Starting QR Code Detection Application")
            # Create a thread for keyboard and tray icon
            tray_thread = threading.Thread(target=self.listen_for_shortcut, daemon=True)
            tray_thread.start()

            # Wait for stop event instead of thread join
            while not self.tray_icon_manager.stop_event.is_set():
                self.tray_icon_manager.stop_event.wait(1)

            logger.info("Application exit initiated")
        except Exception as e:
            logger.exception(f"Application run error: {e}")


def main() -> None:
    try:
        # Capture any uncaught exceptions
        sys.excepthook = handle_exception

        # Create and run the application
        app = QRCodeDetectionApp()
        app.run()
    except Exception as e:
        logger.critical(f"Fatal application error: {e}", exc_info=True)


if __name__ == "__main__":
    main()
