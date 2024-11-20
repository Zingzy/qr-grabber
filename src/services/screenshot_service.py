import pyautogui
from PIL import ImageFile
from loguru import logger
from typing import Optional


class ScreenshotCapture:
    """Responsible for capturing screenshots"""

    @staticmethod
    def take_bounded_screenshot(
        x1: int, y1: int, x2: int, y2: int
    ) -> Optional[ImageFile.Image]:
        """
        Capture a screenshot within specified bounds

        Args:
            x1: Top-left x coordinate
            y1: Top-left y coordinate
            x2: Bottom-right x coordinate
            y2: Bottom-right y coordinate

        Returns:
            Captured screenshot or None if error occurs
        """
        try:
            x1, y1 = int(x1), int(y1)
            x2, y2 = int(x2), int(y2)

            # Ensure positive dimensions
            width: int = max(1, abs(x2 - x1))
            height: int = max(1, abs(y2 - y1))

            screenshot: ImageFile.Image = pyautogui.screenshot(
                region=(x1, y1, width, height)
            )
            logger.debug(f"Screenshot captured: {width}x{height} at ({x1},{y1})")
            return screenshot
        except Exception as e:
            logger.exception(f"Screenshot capture error: {e}")
            return None
