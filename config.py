import os

# Application settings
APP_NAME = "mimizu"
VERSION = "0.1.0"

# Current default (might change)
ACTIVATION_HOTKEY = '<ctrl>+<shift>+t'

EASYOCR_PATH = 'vendor/easyocr'
OCR_LANGUAGE = 'jpn'

# GUI settings for lookups
RESULT_WINDOW_WIDTH = 400
RESULT_WINDOW_HEIGHT = 300
RESULT_WINDOW_ALPHA = 0.95

# Dictionary settings
DICT_DIR = os.path.join(os.path.dirname(__file__), 'data', 'dictionaries')
