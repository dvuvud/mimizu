from SelectionOverlay import select_region
from RegionCapture import capture_region

def handle_selection(rect):
    png_base64 = capture_region(rect)
    if png_base64 is None:
        print("PNG_DATA:null")
    else:
        print("PNG_DATA:" + png_base64)

select_region(handle_selection)