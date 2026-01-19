import easyocr
import numpy as np
import config

class OCREngine:
    def __init__(self):
        self.language = config.OCR_LANGUAGE
        self.reader = None
        self.model_storage_directory = config.OCR_MODEL_DIR
        self._initialize_reader()

    def _initialize_reader(self):
        """Initialize the EasyOCR reader with configured language"""
        try:
            if config.DEBUG_MODE:
                print(f"[DEBUG] Initializing OCR reader for language: {self.language}")
                print(f"[DEBUG] Model directory: {self.model_storage_directory}")

            self.reader = easyocr.Reader(
                    [self.language],
                    gpu=True,
                    model_storage_directory=self.model_storage_directory,
                    download_enabled=True
                    )

            if config.DEBUG_MODE:
                print("[DEBUG] OCR reader initialized successfully")

        except Exception as e:
            print(f"Error initializing OCR reader: {e}")
            self.reader = None

    def extract_text(self, image):
        """
        Extract Japanese text from a PIL Image
        """
        if self.reader is None:
            print("OCR reader not initialized")
            return []

        try:
            img_array = np.array(image)

            if config.DEBUG_MODE:
                print(f"[DEBUG] Processing image: {img_array.shape}")

            results = self.reader.readtext(
                    img_array,
                    decoder=config.OCR_DECODER,
                    beamWidth=config.OCR_BEAMSEARCH_WIDTH,
                    min_size=10,
                    contrast_ths=0.1,
                    adjust_contrast=0.5,
                    text_threshold=0.7,
                    low_text=0.4,
                    link_threshold=0.4,
                    canvas_size=2560,
                    mag_ratio=1.0
                    )

            if config.DEBUG_MODE:
                print(f"[DEBUG] Found {len(results)} text regions")
                for bbox, text, conf in results:
                    print(f"[DEBUG] Text: '{text}' (confidence: {conf:.2f})")

            return results

        except Exception as e:
            if config.DEBUG_MODE:
                print(f"[DEBUG] Error during OCR extraction: {e}")
            return []

    def get_text_only(self, image):
        """
        Extract only the text strings from an image
        """
        results = self.extract_text(image)
        return [text for _, text, _ in results]

    def get_full_text(self, image, separator='\n'):
        """
        Extract all text and combine into a single string
        """
        text_list = self.get_text_only(image)
        return separator.join(text_list)
