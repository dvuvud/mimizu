import sys
import subprocess
import base64
from io import BytesIO
from PIL import Image
from pynput import keyboard
import config
import os

def capture_screen_region():
    try:
        proc = subprocess.Popen(
            [config.SC_OBJ],
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

def on_activation_hotkey_pressed():
    print("Capture triggered. Select a region...")
    
    captured_image = capture_screen_region()
    
    if captured_image:
        print("Capture successful")
        
        if config.AUTO_SAVE_CAPTURES:
            os.makedirs(config.SAVE_DIRECTORY, exist_ok=True)
            from datetime import datetime
            filename = f"{config.SAVE_DIRECTORY}/capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            captured_image.save(filename)
            print(f"Screen capture was saved to {filename}")
    else:
        print("Capture cancelled or failed")
        sys.exit(0)

def on_exit_hotkey_pressed():
    print(f"Exiting {config.APP_NAME}")
    sys.exit(0)

def main():
    print("="*50)
    print(f"{config.APP_NAME} started")
    print("="*50)
    print(f"\nCapture hotkey: {config.ACTIVATION_HOTKEY}")
    print(f"Debug Mode: {'ON' if config.DEBUG_MODE else 'OFF'}")
    print(f"Auto-save: {'ON' if config.AUTO_SAVE_CAPTURES else 'OFF'}")
    print(f"Press {config.EXIT_HOTKEY} to exit\n")
    
    with keyboard.GlobalHotKeys({
        config.ACTIVATION_HOTKEY: on_activation_hotkey_pressed,
        config.EXIT_HOTKEY: on_exit_hotkey_pressed
        }) as listener:
        try:
            listener.join()
        except SystemExit:
            listener.stop()
            sys.exit(0)
        except KeyboardInterrupt:
            listener.stop()
            print("\nInterrupted by user")
            sys.exit(130)
        except Exception as e:
            listener.stop()
            print(f"\nUnexpected error of type {type(e).__name__} occured")
            print(f"\nExiting...")
            sys.exit(1)


if __name__ == "__main__":
    main()
