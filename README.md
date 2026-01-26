# Mimizu

**Mimizu** is a cross-platform screen capture tool with OCR and dictionary lookup capabilities.  

The macOS version is currently functional. Windows and Linux support are planned.

## Installation & Running

#### 1. Clone the repository
```bash
git clone https://github.com/yourusername/mimizu.git
cd mimizu
```

### macOS

#### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

#### 3. Build and run the program
```bash
make macos
```

>You may need to grant **Screen Recording** and **Accessibility** permissions to the terminal >in **macOS System Settings**.

### Linux (X11)

#### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

#### 3. Install Gtk dependencies
e.g. on Debian:
```
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 libcairo2 gtk3
```

#### 3. Build and run the program
```bash
make linux
```

You may need to grant **Screen Recording** and **Accessibility** permissions to the terminal in **macOS System Settings**.

## Keybinds & Settings

As of now, Mimizu is operated entirely via keyboard shortcuts.
The main hotkey triggers the screen selection and OCR workflow.
All keybinds and related settings are defined in [config.py](https://github.com/dvuvud/mimizu/blob/main/config.py) and can be edited as preferred.

### Defaults

| Value              | Description                            |
|--------------------|----------------------------------------|
| `<ctrl>+<shift>+s` | Start screen capture and OCR workflow  |
| `Esc`              | Exit program                           |
| `False`            | Auto save screen captures              |
| `captures/`        | Folder for saved screen captures       |
| `False`            | Display debug messages                 |
| `400`              | Lookup window width                    |
| `300`              | Lookup window height                   |
| `0.95`             | Lookup window alpha                    |

