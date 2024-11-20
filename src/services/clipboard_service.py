import pyperclip
from loguru import logger


class ClipboardService:
    """Handles clipboard operations"""

    @staticmethod
    def copy_to_clipboard(text: str) -> None:
        """
        Copy text to clipboard

        Args:
            text: Text to copy
        """
        try:
            pyperclip.copy(text)
            logger.info(f"Text copied to clipboard (length: {len(text)})")
        except Exception as e:
            logger.exception(f"Clipboard copy error: {e}")
