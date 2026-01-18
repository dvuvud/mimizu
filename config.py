import os

# Application settings
APP_NAME = "Mimizu"

# App defaults
ACTIVATION_HOTKEY = '<cmd>+<shift>+l'
EXIT_HOTKEY = '<esc>'

SC_OBJ = './build/mimizu_overlay'
DEBUG_MODE = False

OCR_LANGUAGE = 'jpn'

# GUI settings for lookups
RESULT_WINDOW_WIDTH = 400
RESULT_WINDOW_HEIGHT = 300
RESULT_WINDOW_ALPHA = 0.95

# Dictionary settings
DICT_DIR = os.path.join(os.path.dirname(__file__), 'data', 'dictionaries')

# Screen capture settings
AUTO_SAVE_CAPTURES = False
SAVE_DIRECTORY = "./captures"
