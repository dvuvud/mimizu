import os
from datetime import datetime
import config

class ImageSaver:
    def __init__(self):
        self.save_dir = config.SAVE_DIRECTORY
        self.auto_save = config.AUTO_SAVE_CAPTURES

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
