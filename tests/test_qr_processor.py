import pytest
from PIL import Image
from src.services.qr_processor import QRCodeProcessor


def test_detect_qr_code_with_none_image():
    result, success = QRCodeProcessor.detect_qr_code(None)
    assert result is None
    assert not success


@pytest.mark.parametrize(
    "image_path, expected_data",
    [
        ("tests/data/valid_qr1.png", "Valid QR Code"),
        ("tests/data/valid_qr2.png", "Valid QR Code"),
    ],
)
def test_detect_qr_code_with_valid_qr_code_image(image_path, expected_data):
    qr_code_image = Image.open(image_path)
    result, success = QRCodeProcessor.detect_qr_code(qr_code_image)
    assert result == expected_data
    assert success


@pytest.mark.parametrize(
    "image_path, expected_data",
    [
        ("tests/data/valid_gradient_qr1.png", "https://example.com"),
        ("tests/data/valid_gradient_qr2.png", "https://example.com"),
    ],
)
def test_detect_qr_code_with_valid_gradient_qr_code_image(image_path, expected_data):
    qr_code_image = Image.open(image_path)
    result, success = QRCodeProcessor.detect_qr_code(qr_code_image)
    assert result == expected_data
    assert success


lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In facilisis laoreet turpis, sit amet elementum nulla congue eget. Duis volutpat ex at vehicula tristique. Phasellus at ligula eu nisl cursus vulputate. Donec in tincidunt urna. Mauris mollis lacus nec consequat tristique. Mauris ligula risus, dictum blandit ante vel, accumsan aliquet leo. Maecenas mauris quam, varius vitae sapien at, malesuada pharetra nulla. Cras at mauris condimentum dui congue elementum. Cras fringilla erat sit amet orci vehicula suscipit. Fusce sit amet arcu et erat venenatis molestie non id velit.  Maecenas a posuere tortor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec semper mi nibh, sagittis convallis augue posuere quis. Nunc est augue, tincidunt a vulputate at, viverra ac tortor. Integer luctus, est in tincidunt iaculis, odio mi sodales odio, sit amet pretium diam justo sit amet mi. Integer cursus, felis vel molestie commodo, arcu augue varius massa, quis finibus eros lectus id est. Donec tristique gravida hendrerit. Mauris ac quam est. Nullam in feugiat elit. Quisque egestas dolor eros, eget tincidunt turpis aliquam eu. Aliquam gravida est tempor quam elementum vehicula. Quisque non blandit arcu, eget blandit odio. Phasellus suscipit erat at massa mollis tempor."


@pytest.mark.xfail(
    reason="Will Fail because the current QR detection System does not support huge QR codes"
)
@pytest.mark.parametrize(
    "image_path, expected_data",
    [
        ("tests/data/valid_huge_qr1.png", lorem),
        ("tests/data/valid_huge_qr2.png", lorem),
    ],
)
def test_detect_qr_code_with_valid_huge_qr_code_image(image_path, expected_data):
    qr_code_image = Image.open(image_path)
    result, success = QRCodeProcessor.detect_qr_code(qr_code_image)
    assert result == expected_data
    assert success


@pytest.mark.xfail(
    reason="Stylized QR detection is not supported by the current system"
)
@pytest.mark.parametrize(
    "image_path, expected_data",
    [
        ("tests/data/valid_stylized_qr1.png", "Valid QR Code"),
        ("tests/data/valid_stylized_qr2.png", "Valid QR Code"),
        ("tests/data/valid_stylized_qr3.png", "Valid QR Code"),
    ],
)
def test_detect_qr_code_with_valid_stylized_qr_code_image(image_path, expected_data):
    qr_code_image = Image.open(image_path)
    result, success = QRCodeProcessor.detect_qr_code(qr_code_image)
    assert result == expected_data
    assert success


def test_detect_invalid_qr_code_image():
    invalid_qr_code_image = Image.open("tests/data/invalid_qr.png")
    result, success = QRCodeProcessor.detect_qr_code(invalid_qr_code_image)
    assert result is None
    assert not success


def test_detect_qr_code_with_pil_image():
    pil_image = Image.new("RGB", (100, 100))
    result, success = QRCodeProcessor.detect_qr_code(pil_image)
    assert result is None
    assert not success
