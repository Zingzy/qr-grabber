from plyer import notification
from loguru import logger


class NotificationService:
    """Manages user notifications"""

    @staticmethod
    def show_notification(title: str, message: str, timeout: int = 2) -> None:
        """
        Display a system notification

        Args:
            title: Notification title
            message: Notification message
            timeout: Duration to show notification
        """
        try:
            notification.notify(title=title, message=message, timeout=timeout)
            logger.debug(f"Notification sent: {title}")
        except Exception as e:
            logger.exception(f"Notification error: {e}")
