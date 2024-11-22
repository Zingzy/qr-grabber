try:
    from pyzbar.pyzbar import decode, ZBarSymbol
except FileNotFoundError:
    import sys
    from loguru import logger
    from tkinter import messagebox

    logger.error(
        "Failed to import pyzbar. This may be due to a missing vcredist_x64.exe file."
    )
    logger.error(
        "Please download and install the Visual C++ Redistributable for Visual Studio 2013 from the following link:"
    )
    logger.error("https://www.microsoft.com/en-gb/download/details.aspx?id=40784")

    messagebox.showerror(
        "Import Error",
        "Failed to import pyzbar. This may be due to a missing vcredist_x64.exe file.\n\n"
        "Please download and install the Visual C++ Redistributable for Visual Studio 2013 from the following link:\n"
        "https://www.microsoft.com/en-gb/download/details.aspx?id=40784",
    )
    sys.exit(1)

from PIL import Image
from loguru import logger
from typing import Optional, Tuple, Union


class QRCodeProcessor:
    """Handles QR code detection and processing"""

    @staticmethod
    def detect_qr_code(
        image: Optional[Union[Image.Image, str]],
    ) -> Tuple[Optional[str], bool]:
        """
        Detect and decode QR code from an image

        Args:
            image: Image to process or path to the image file

        Returns:
            Tuple of (detected data, detection success)
        """
        if image is None:
            logger.warning("Attempted to process None image")
            return None, False

        try:
            if isinstance(image, str):
                image = Image.open(image)

            logger.debug("Starting QR code detection")
            decoded_objects = decode(image, symbols=[ZBarSymbol.QRCODE])

            if decoded_objects:
                data = decoded_objects[0].data.decode("utf-8")
                if not data:
                    logger.warning("Empty QR Code detected")
                    return None, False
                logger.success(f"QR Code detected: {data}")
                return data, True

            logger.warning("No QR Code detected in image")
            return None, False
        except Exception as e:
            logger.exception(f"QR code detection error: {e}")
            return None, False
