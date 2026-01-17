import sys
import logging
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject, pyqtSignal

import config
from core.hotkey_listener import HotkeyListener
from gui.selection_overlay import SelectionOverlay

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MimizuApp(QObject):
    request_overlay = pyqtSignal()

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.overlay = None

        self.request_overlay.connect(self.show_overlay)

        self.hotkey_listener = HotkeyListener(
            config.ACTIVATION_HOTKEY,
            self.on_hotkey_pressed
        )
        self.hotkey_listener.start()
        logger.info("Mimizu initialized")

    def on_hotkey_pressed(self):
        self.request_overlay.emit()

    def show_overlay(self):
        self.overlay = SelectionOverlay()
        self.overlay.selection_finished.connect(self.on_selection_done)

    def on_selection_done(self, img):
        print(f"Captured image shape: {img.shape}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mimizu = MimizuApp(app)
    sys.exit(app.exec())

