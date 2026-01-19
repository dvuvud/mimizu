import os
from datetime import datetime
import config

class ImageSaver:
    def __init__(self, ocr_engine=None, preprocessor=None):
        self.save_dir = config.SAVE_DIRECTORY
        self.auto_save = config.AUTO_SAVE_CAPTURES
        self.ocr_engine = ocr_engine;
        self.preprocessor = preprocessor

    def generate_filename(self):
        """Generate a timestamped filename for the capture"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return f"{self.save_dir}/capture_{timestamp}.png"

    def save_image(self, image):
        """Save image to disk"""
        os.makedirs(self.save_dir, exist_ok=True)
        filename = self.generate_filename()
        image.save(filename)
        return filename

    def handle_image(self, image):
        """Process and optionally save the captured image"""
        if self.auto_save:
            filename = self.save_image(image)
            print(f"Screen capture was saved to {filename}")

        if self.ocr_engine:
            print("\nExtracting text...")

            processed_image = image
            if self.preprocessor and config.OCR_PREPROCESS_MODE != 'none':
                if config.DEBUG_MODE:
                    print(f"[DEBUG] Preprocessing with mode: {config.OCR_PREPROCESS_MODE} :)")
                processed_image = self.preprocessor.preprocess_for_ocr(
                        image,
                        mode=config.OCR_PREPROCESS_MODE
                        )
            
            full_text = self.ocr_engine.get_full_text(processed_image)

            if full_text:
                print("Extracted text...")
                print(full_text)
            else:
                print("No text detected in the image")

        else:
            if config.DEBUG_MODE:
                print("[DEBUG] OCR engine not initialized")
                return None;
