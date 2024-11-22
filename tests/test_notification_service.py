from unittest.mock import patch
from src.services.notification_service import NotificationService


@patch("plyer.notification.notify")
def test_show_notification(mock_notify):
    # Initialize the NotificationService
    app_icon = "test_icon.ico"
    service = NotificationService(app_icon)

    # Test parameters
    title = "Test Title"
    message = "Test Message"
    timeout = 2

    # Call the method to test
    service.show_notification(title, message, timeout)

    # Assert the `notify` function was called with the correct arguments
    mock_notify.assert_called_once_with(
        title=title, message=message, timeout=timeout, app_icon=app_icon
    )


@patch("plyer.notification.notify")
@patch("loguru.logger.exception")
def test_show_notification_with_exception(mock_logger_exception, mock_notify):
    # Simulate an exception in the notify call
    mock_notify.side_effect = Exception("Notification error")

    # Initialize the NotificationService
    app_icon = "test_icon.ico"
    service = NotificationService(app_icon)

    # Test parameters
    title = "Test Title"
    message = "Test Message"
    timeout = 2

    # Call the method to test
    service.show_notification(title, message, timeout)

    # Assert the `notify` function was called
    mock_notify.assert_called_once_with(
        title=title, message=message, timeout=timeout, app_icon=app_icon
    )

    # Assert the logger.exception was called with the correct message
    mock_logger_exception.assert_called_once_with(
        "Notification error: Notification error"
    )
