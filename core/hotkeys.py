import sys
from pynput import keyboard
import config

class HotkeyManager:
    def __init__(self, screen_capture, image_saver):
        self.screen_capture = screen_capture
        self.image_saver = image_saver
        self.listener = None

    def on_activation_hotkey_pressed(self):
        """Handle capture hotkey press"""
        print("Capture triggered. Select a region...")

        captured_image = self.screen_capture.capture_region()

        if captured_image:
            print("Capture successful")
            self.image_saver.handle_image(captured_image)
        else:
            print("Capture cancelled or failed")
            sys.exit(0)

    def on_exit_hotkey_pressed(self):
        """Handle exit hotkey press"""
        print(f"Exiting {config.APP_NAME}")
        sys.exit(0)

    def run(self):
        """Start the hotkey listener"""
        with keyboard.GlobalHotKeys({
            config.ACTIVATION_HOTKEY: self.on_activation_hotkey_pressed,
            config.EXIT_HOTKEY: self.on_exit_hotkey_pressed
            }) as listener:
            self.listener = listener
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
                print(f"\nUnexpected error of type {type(e).__name__} occurred")
                print(f"\nExiting...")
                sys.exit(1)

    def stop(self):
        """Stop the hotkey listener"""
        if self.listener:
            self.listener.stop()
