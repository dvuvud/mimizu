import logging
import numpy as np
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import Qt, QRect, pyqtSignal
from PyQt6.QtGui import QPainter, QColor
from core.screen_capture import ScreenCapture

logger = logging.getLogger(__name__)

class SelectionOverlay(QWidget):
    selection_finished = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
                Qt.WindowType.FramelessWindowHint |
                Qt.WindowType.WindowStaysOnTopHint |
                Qt.WindowType.Tool
                )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.setCursor(Qt.CursorShape.CrossCursor)

        screen = QApplication.primaryScreen()
        if screen is None:
            raise RuntimeError("No screen available")
        self.setGeometry(screen.geometry())

        self.start_pos = None
        self.end_pos = None
        self.selection_rect = QRect()

        self.show()
        self.raise_()


    def mousePressEvent(self, a0):
        if a0 is None:
            return
        logger.debug(f"Mouse pressed at {a0.pos()}")
        self.start_pos = a0.pos()
        self.end_pos = a0.pos()
        self.update()

    def mouseMoveEvent(self, a0):
        if a0 is None:
            return
        self.end_pos = a0.pos()
        if self.start_pos is not None:
            self.selection_rect = QRect(self.start_pos, self.end_pos)
        self.update()

    def mouseReleaseEvent(self, a0):
        if a0 is None:
            return
        self.end_pos = a0.pos()
        if self.start_pos is None:
            logger.warning("Mouse released but start_pos is None")
            self.close()
            return

        self.selection_rect = QRect(self.start_pos, self.end_pos)

        x, y, w, h = (self.selection_rect.left(), self.selection_rect.top(),
                      self.selection_rect.width(), self.selection_rect.height())
        img = ScreenCapture.capture_region(x, y, w, h)

        self.selection_finished.emit(img)
        self.close()

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if not self.selection_rect.isNull():
            painter.setPen(QColor(255, 255, 255))
            painter.drawRect(self.selection_rect.normalized())

