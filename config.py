import os

# Application settings
APP_NAME = 'Mimizu'

# App defaults
ACTIVATION_HOTKEY = '<ctrl>+<shift>+s'
EXIT_HOTKEY = '<esc>'
DEBUG_MODE = True

# Screen capture settings
AUTO_SAVE_CAPTURES = False
SAVE_DIRECTORY = './captures'
SC_OBJ_MACOS = './build/mimizu_overlay'
SC_PY_PATH = './native/gtk/index.py'

# OCR settings
OCR_LANGUAGE = 'ja'
OCR_MODEL_DIR = os.path.join(os.path.dirname(__file__), 'data', 'models')
OCR_DECODER = 'greedy'
OCR_BEAMSEARCH_WIDTH = 10
OCR_PREPROCESS_MODE = 'auto'

# GUI settings for lookups
RESULT_WINDOW_WIDTH = 400
RESULT_WINDOW_HEIGHT = 300
RESULT_WINDOW_ALPHA = 0.95

# Dictionary settings
DICT_DIR = os.path.join(os.path.dirname(__file__), 'data', 'dictionaries')

