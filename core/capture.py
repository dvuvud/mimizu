import subprocess
import base64
from io import BytesIO
from PIL import Image
import config
import platform

MACOS = 'Darwin'
LINUX = 'Linux'

class ScreenCapture:
    def __init__(self):
        self.platform = platform.system()

        if self.platform == MACOS:
            print("[DEBUG] Detected macos")
            self.sc_obj = config.SC_OBJ_MACOS

        elif self.platform == LINUX:
            print("[DEBUG] Detected linux")
            self.sc_obj = config.SC_PY_PATH

        else:
            raise Exception(f"Platform '{self.platform}' is not supported")

    def capture_region(self):
        """Capture a screen region using the configured screen capture tool"""
        print("capture started")
        try:
            proc = subprocess.Popen(
                    [self.sc_obj],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                    )

            stdout, stderr = proc.communicate()

            for line in stdout.split('\n'):
                if line.startswith('PNG_DATA:'):
                    data_part = line.split('PNG_DATA:', 1)[1].strip()
                    if data_part == 'null':
                        if config.DEBUG_MODE:
                            print("[DEBUG] Received null image data")
                        return None
                    else:
                        if config.DEBUG_MODE:
                            print("[DEBUG] Received image data (non-null)")

                        png_data = base64.b64decode(data_part)
                        image = Image.open(BytesIO(png_data))

                        if config.DEBUG_MODE:
                            print(f"[DEBUG] Successfully loaded: {image.size[0]}x{image.size[1]} pixels")

                        return image

            return None

        except Exception as e:
            if config.DEBUG_MODE:
                print(f"[DEBUG] Error during capture: {e}")
            return None

