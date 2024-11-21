from unittest.mock import patch
from src.services.notification_service import NotificationService


@patch("plyer.notification.notify")
def test_show_notification(mock_notify):
    title = "Test Title"
    message = "Test Message"
    timeout = 2

    NotificationService.show_notification(title, message, timeout)
    mock_notify.assert_called_once_with(title=title, message=message, timeout=timeout)


@patch("plyer.notification.notify")
@patch("loguru.logger.exception")
def test_show_notification_with_exception(mock_logger_exception, mock_notify):
    mock_notify.side_effect = Exception("Notification error")
    title = "Test Title"
    message = "Test Message"
    timeout = 2

    NotificationService.show_notification(title, message, timeout)
    mock_notify.assert_called_once_with(title=title, message=message, timeout=timeout)
    mock_logger_exception.assert_called_once_with(
        "Notification error: Notification error"
    )
