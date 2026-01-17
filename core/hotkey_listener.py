import logging
from pynput import keyboard

logger = logging.getLogger(__name__)

class HotkeyListener:
    def __init__(self, hotkey, callback):
        self.hotkey = hotkey
        self.callback = callback
        self.listener = keyboard.GlobalHotKeys({
            hotkey: callback
        })

    def start(self):
        logger.info(f"Starting hotkey listener: {self.hotkey}")
        self.listener.start()

    def stop(self):
        logger.info("Stopping hotkey listener")
        self.listener.stop()

