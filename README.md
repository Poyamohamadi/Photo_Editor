
# Photo Editor

A sleek, modern photo editing application built using **Python**, **CustomTkinter**, and **Pillow (PIL)**. This tool allows users to enhance and filter images with real-time adjustments including brightness, color, sharpness, blur, and various advanced filters like edge detection, emboss, and more.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Structure](#structure)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)

---

## Program Demo

![Photo_Editor](https://github.com/Poyamohamadi/Photo_Editor/blob/main/demo.gif)


## Features

- **Open & Edit Images**: Load any image from your system.
- **Enhancement Tools**:
  - Brightness adjustment
  - Color saturation
  - Sharpness control
- **Filter Effects**:
  - Blur, Smooth, Smooth More
  - Sharpen, Contour, Detail, Edge Enhance, Edge Enhance More
  - Find Edges, Emboss
- **Advanced Filters**:
  - Min, Median, Max, Mode Filters
  - Box Blur, Gaussian Blur, Unsharp Mask
- **Real-Time Preview**: See changes instantly applied to your image.
- **Modern UI**: Built with `customtkinter` for a clean, responsive interface.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- Basic knowledge of running Python scripts.
### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Poyamohamadi/photo_editor.git
   cd photo_editor
   ```

2. Install required dependencies:
   ```bash
   pip install customtkinter pillow
   ```

3. Ensure you have a starting image named `picture.jpg` in the project directory (or use the "Open Picture" button to load any image).

4. Run the application:
   ```bash
   python main.py
   ```


---

## Usage

1. Launch the app:
   ```bash
   python main.py
   ```

2. Click **"Open Picture"** to load an image from your device.

3. Choose editing mode:
   - **Enhance**: Adjust brightness, color, and sharpness using sliders.
   - **Filter**: Apply visual effects via toggle switches and sliders.

4. Toggle filters on/off:
   - Simple filters (e.g., Blur, Sharpen) activate instantly.
   - Advanced filters (e.g., Median, Gaussian Blur) show a slider when enabled.

5. View results in real time — no manual "Apply" button needed!

6. Close the app when done.

>  Note: Edited images are temporarily saved as `new_picture.png` during runtime.

---

## Structure

The project is contained in a single script (`main.py`) with a class-based structure for modularity and readability.

### Key Components

#### `App(CTk)`
Main class inheriting from `customtkinter.CTk`. Manages the entire UI and image processing logic.

##### Core Methods:
- `__init__()`: Initializes variables, window settings, and starts the app loop.
- `run()`: Sets up the main UI layout — button and image display frame.
- `open_image()`: Opens a file dialog to load an image.
- `show_edit(value)`: Displays the editing panel with mode selector.
- `set_edit(value)`: Switches between "Enhance" and "Filter" modes.
- `enhance()`: Adds sliders for brightness, color, and sharpness.
- `filter()`: Builds a scrollable panel with toggleable filters and dynamic sliders.
- `edit_img()`: Applies all selected enhancements and filters in sequence and updates the preview.

##### Variables:
- `DoubleVar`, `IntVar`, `BooleanVar`: Track slider values and toggle states.
- `picture`: Original image loaded from file.
- `new_picture`: Working copy used for edits.

##### Image Processing:
Uses `Pillow` modules:
- `ImageEnhance.Brightness`, `Color`, `Sharpness`
- `ImageFilter.BLUR`, `SHARPEN`, `EMBOSS`, `FIND_EDGES`, etc.

---

## Dependencies

This project uses the following libraries:

| Library         | Purpose                                     |
| --------------- | ------------------------------------------- |
| `customtkinter` | Modern GUI framework with dark/light themes |
| `Pillow (PIL)`  | Image loading, manipulation, and filtering  |
| `tkinter`       | File dialog integration (via `filedialog`)  |

Install them using:
```bash
pip install customtkinter pillow
```

---

## Contributing

We welcome contributions! To help improve this project:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/new-filter`
3. Commit your changes: `git commit -m "Add brightness reset button"`
4. Push to the branch: `git push origin feature/new-filter`
5. Open a pull request.

Please ensure your code matches the existing style and includes comments where necessary.

---

## License

This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for more details.

---

## Acknowledgments

-  Thanks to the **CustomTkinter** team for a beautiful and easy-to-use GUI library.
- **Pillow** developers for powerful image processing in Python.
-  The Python community for continuous innovation and support.

---

## Contact

Have questions or suggestions? Reach out:

- **GitHub**: [@Poyamohamadi](https://github.com/Poyamohamadi)

---

Thank you for using **Photo Editor**! 
Let your creativity shine, one filter at a time.

