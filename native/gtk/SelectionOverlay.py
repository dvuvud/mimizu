
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, cairo

BORDER_WIDTH = 2.0
DARK_ALPHA = 0.0

class SelectionWindow(Gtk.Window):
    def __init__(self, callback):
        super().__init__(type=Gtk.WindowType.TOPLEVEL)
        self.callback = callback

        self.start = None
        self.end = None

        self.set_decorated(False)
        self.set_app_paintable(True)
        self.set_keep_above(True)
        self.fullscreen()

        self.captured = False # to prevent twofold output

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual:
            self.set_visual(visual)

        self.connect("draw", self.on_draw)
        self.connect("key-press-event", self.on_key_press)


        self.add_events(
            Gdk.EventMask.BUTTON_PRESS_MASK | 
            Gdk.EventMask.BUTTON_RELEASE_MASK |
            Gdk.EventMask.POINTER_MOTION_MASK
        )
        self.connect("button-press-event", self.on_button_press)
        self.connect("motion-notify-event", self.on_motion)
        self.connect("button-release-event", self.on_button_release)

        self.show_all()

    def on_button_press(self, widget, event):
        if event.button != 1:
            return
        self.start = (event.x, event.y)
        self.end = self.start
        self.queue_draw()

    def on_motion(self, widget, event):
        self.end = (event.x, event.y)
        self.queue_draw()

    def on_button_release(self, widget, event):
        if self.captured:
            return
        self.captured = True

        if not self.start or not self.end:
            self.callback(None)
            Gtk.main_quit()
            return

        x1, y1 = self.start
        x2, y2 = self.end

        rect = (
            min(x1, x2) + BORDER_WIDTH,
            min(y1, y2) + BORDER_WIDTH,
            abs(x2 - x1) - BORDER_WIDTH * 2,
            abs(y2 - y1) - BORDER_WIDTH * 2,
        )

        if rect[2] <= 0 or rect[3] <= 0:
            self.callback(None)
            Gtk.main_quit()
            return

        self.callback(rect)
        Gtk.main_quit()

    def on_key_press(self, widget, event):
        key = Gdk.keyval_name(event.keyval)
        if key == "Escape":
            self.callback(None)
            Gtk.main_quit()

    def on_draw(self, widget, cr):
        width = self.get_allocated_width()
        height = self.get_allocated_height()

        cr.set_source_rgba(0, 0, 0, DARK_ALPHA)
        cr.rectangle(0, 0, width, height)
        cr.fill()

        if not self.start or not self.end:
            return
        
        x1, y1 = self.start
        x2, y2 = self.end

        x = min(x1, x2)
        y = min(y1, y2)
        w = abs(x2 - x1)
        h = abs(y2 - y1)

        cr.set_source_rgba(1, 1, 1, DARK_ALPHA)
        cr.rectangle(x, y, w, h)
        cr.fill()

        cr.set_line_width(BORDER_WIDTH)
        cr.set_source_rgba(1, 0, 0, 1)
        cr.set_dash([8.0, 4.0], 0)
        cr.rectangle(x, y, w, h)
        cr.stroke()

def select_region(callback):
    """Calls callback when done"""
    print("[DEBUG] Screen capture started")
    win = SelectionWindow(callback)
    Gtk.main()

