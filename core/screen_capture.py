import mss
import numpy as np

class ScreenCapture:
    @staticmethod
    def capture_region(x, y, w, h):
        with mss.mss() as sct:
            monitor = {
                "top": y,
                "left": x,
                "width": w,
                "height": h
            }
            img = np.array(sct.grab(monitor))
            return img

