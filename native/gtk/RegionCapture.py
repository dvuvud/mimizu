import mss
from PIL import Image
import io
import base64

def capture_region(rect):
    if rect is None:
        return None

    x, y, w, h = rect
    with mss.mss() as sct:
        monitor = {"top": int(rect[1]),
                "left": int(rect[0]),
                "width": int(rect[2]),
                "height": int(rect[3])}
        sct_img = sct.grab(monitor)

        img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        png_data = buffer.getvalue()

        b64 = base64.b64encode(png_data).decode("utf-8")
        return b64