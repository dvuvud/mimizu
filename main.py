import config
from core.hotkeys import HotkeyManager
from core.capture import ScreenCapture
from core.image_handler import ImageSaver
from core.ocr_engine import OCREngine
from core.preprocessor import ImagePreprocessor

def main():
    print("="*50)
    print(f"{config.APP_NAME} started")
    print("="*50)
    print(f"\nCapture hotkey: {config.ACTIVATION_HOTKEY}")
    print(f"Debug Mode: {'ON' if config.DEBUG_MODE else 'OFF'}")
    print(f"Auto-save: {'ON' if config.AUTO_SAVE_CAPTURES else 'OFF'}")
    print(f"OCR Language: {config.OCR_LANGUAGE}")
    print(f"Press {config.EXIT_HOTKEY} to exit\n")

    ocr_engine = OCREngine()
    preprocessor = ImagePreprocessor()

    screen_capture = ScreenCapture()
    image_saver = ImageSaver(ocr_engine, preprocessor)
    hotkey_manager = HotkeyManager(screen_capture, image_saver)

    hotkey_manager.run()

if __name__ == "__main__":
    main()
