# Mimizu

**Mimizu** is a cross-platform screen capture tool with OCR and dictionary lookup capabilities.  

The macOS version is currently functional. Windows and Linux support are planned.

## Installation

### macOS

#### 1. Clone the repository
```bash
git clone https://github.com/yourusername/mimizu.git
cd mimizu
```

#### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

#### 3. Build and run the program
```bash
make
```

You may need to grant **Screen Recording** and **Accessibility** permissions to the terminal in **macOS System Settings**.

## Keybinds & Settings

As of now, Mimizu is operated entirely via keyboard shortcuts.
The main hotkey triggers the screen selection and OCR workflow.
All keybinds and related settings are defined in [config.py](https://github.com/dvuvud/mimizu/blob/main/config.py) and can be edited as preferred.

### Defaults

Start screen capture and OCR workflow - `<ctrl>+<shift>+s`

Exit program - `Esc`

Auto save screen captures - `False` (Captures are saved to `captures/` when set to `True`)

Display debug messages - `False`

Lookup window width - `400`

Lookup window height - `300`

Lookup window alpha - `0.95`
