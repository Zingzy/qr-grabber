from unittest.mock import patch
from src.services.clipboard_service import ClipboardService


@patch("pyperclip.copy")
def test_copy_to_clipboard(mock_copy):
    text = "Sample text"
    ClipboardService.copy_to_clipboard(text)
    mock_copy.assert_called_once_with(text)


@patch("pyperclip.copy")
def test_copy_to_clipboard_with_empty_string(mock_copy):
    text = ""
    ClipboardService.copy_to_clipboard(text)
    mock_copy.assert_called_once_with(text)


@patch("pyperclip.copy")
@patch("loguru.logger.exception")
def test_copy_to_clipboard_with_exception(mock_logger_exception, mock_copy):
    mock_copy.side_effect = Exception("Clipboard error")
    text = "Sample text"
    ClipboardService.copy_to_clipboard(text)
    mock_copy.assert_called_once_with(text)
    mock_logger_exception.assert_called_once_with(
        "Clipboard copy error: Clipboard error"
    )
