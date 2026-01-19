from PIL import Image, ImageEnhance, ImageFilter
import config

class ImagePreprocessor:
    """Preprocess images to improve OCR accuracy"""

    @staticmethod
    def upscale_image(image, scale_factor=2.0):
        """Upscale small text for better recognition"""
        if scale_factor <= 1.0:
            return image

        new_width = int(image.width * scale_factor)
        new_height = int(image.height * scale_factor)
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    @staticmethod
    def increase_contrast(image, factor=1.5):
        """Enhance contrast to make text stand out"""
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(factor)

    @staticmethod
    def increase_sharpness(image, factor=2.0):
        """Sharpen blurry text"""
        enhancer = ImageEnhance.Sharpness(image)
        return enhancer.enhance(factor)

    @staticmethod
    def denoise(image):
        """Remove noise from image"""
        return image.filter(ImageFilter.MedianFilter(size=3))

    @staticmethod
    def preprocess_for_ocr(image, mode='auto'):
        """
        Main preprocessing entry point

        Args:
            image: PIL Image
            mode: 'auto', 'aggressive', 'minimal', or 'none'

        Returns:
            Preprocessed PIL Image
        """
        if mode == 'none':
            return image

        processed = image.copy()

        if processed.width < 500 or processed.height < 500:
            processed = ImagePreprocessor.upscale_image(processed, scale_factor=2.0)
            if config.DEBUG_MODE:
                print(f"[DEBUG] Upscaled to {processed.width}x{processed.height}")

        if mode == 'minimal':
            processed = ImagePreprocessor.increase_sharpness(processed, factor=1.2)
        elif mode == 'aggressive':
            processed = ImagePreprocessor.denoise(processed)
            processed = ImagePreprocessor.increase_contrast(processed, factor=2.0)
            processed = ImagePreprocessor.increase_sharpness(processed, factor=2.5)
        else:  # auto
            processed = ImagePreprocessor.increase_contrast(processed, factor=1.3)
            processed = ImagePreprocessor.increase_sharpness(processed, factor=1.5)

        return processed
