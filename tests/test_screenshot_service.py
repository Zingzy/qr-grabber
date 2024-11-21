import pytest
from unittest.mock import patch
from PIL import Image
from src.services.screenshot_service import ScreenshotCapture
from src.services.qr_processor import QRCodeProcessor


@pytest.mark.parametrize(
    "image_path, expected_data, x1, y1, width, height",
    [
        ("tests/data/screenshot_test1.png", "https://example.com", 809, 351, 376, 376),
        ("tests/data/screenshot_test1.png", "https://example.com", 10, 10, 1000, 1000),
    ],
)
@patch("pyautogui.screenshot")
def test_take_bounded_screenshot_and_detect_qr_code(
    mock_screenshot, image_path, expected_data, x1, y1, width, height
):
    # Load the image with a QR code
    qr_code_image = Image.open(image_path)
    mock_screenshot.return_value = qr_code_image

    screenshot = ScreenshotCapture.take_bounded_screenshot(x1, y1, width, height)

    mock_screenshot.assert_called_once_with(region=(x1, y1, width, height))
    assert screenshot == qr_code_image

    # Detect QR code in the screenshot
    result, success = QRCodeProcessor.detect_qr_code(screenshot)
    assert result == expected_data
    assert success
