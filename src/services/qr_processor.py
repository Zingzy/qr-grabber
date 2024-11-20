import cv2
import numpy as np
from PIL import Image
from loguru import logger
from typing import Optional, Tuple, Union


class QRCodeProcessor:
    """Handles QR code detection and processing"""

    @staticmethod
    def detect_qr_code(
        image: Optional[Union[Image.Image, np.ndarray]],
    ) -> Tuple[Optional[str], bool]:
        """
        Detect and decode QR code from an image

        Args:
            image: Image to process

        Returns:
            Tuple of (detected data, detection success)
        """
        if image is None:
            logger.warning("Attempted to process None image")
            return None, False

        try:
            image_cv: np.ndarray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            detector: cv2.QRCodeDetector = cv2.QRCodeDetector()
            data, bbox, _ = detector.detectAndDecode(image_cv)

            if data:
                logger.success(f"QR Code detected: {data}")
                return data, True

            logger.warning("No QR Code detected in image")
            return None, False
        except Exception as e:
            logger.exception(f"QR code detection error: {e}")
            return None, False
