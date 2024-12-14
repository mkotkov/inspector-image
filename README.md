
# Image Inspector

## Overview

The Image Inspector is a Python tool designed to extract metadata (including GPS coordinates) and hidden messages (like PGP keys) from image files. It leverages both steganography and metadata analysis to reveal hidden data in images. The project is divided into four primary components:

- **main.py**: The entry point of the program, managing user input and processing options.
- **steg.py**: Responsible for handling steganography-related functionality, such as extracting hidden messages.
- **metadata.py**: Contains functions to extract and process metadata, such as GPS data.
- **gui.py**: (Bonus) Implements a Tkinter-based graphical user interface for easier interaction.
- **requirements.txt**: Required Python dependencies.

## Steganography and EXIF

### Steganography
Steganography is the practice of hiding information within other, seemingly innocuous data, such as images. This project uses a technique to hide and extract messages from images by manipulating the least significant bit of pixel values, which results in imperceptible changes to the image while storing hidden information. Common uses for steganography include securely transmitting secrets or hiding sensitive data in plain sight.

### EXIF Metadata
EXIF (Exchangeable Image File Format) is a standard for storing metadata in image files, including information such as the image's creation date, camera model, exposure settings, and even geographical location (GPS coordinates). This project can extract GPS data from EXIF metadata embedded in images, which can be helpful for tracking the image's origin or pinpointing where a photo was taken.

## Installation

To get started with this project, clone the repository and install the required dependencies.

1. Clone the repository:
   ```bash
   git clone https://01.kood.tech/git/mkotkov/inspector-image
   cd inspector-image
   ```

2. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

This project provides two main features: extracting GPS coordinates and extracting hidden messages (like PGP keys) from image files. You can run the program via the command line or through a graphical user interface (GUI).

### Command Line Usage

The following options are available:

- `-map`: Extract GPS coordinates from the image's metadata.
- `-steg`: Extract hidden messages, such as PGP keys, from the image.

To use the command line tool:

```bash
python main.py -option image_path
```

- `-map` will output GPS coordinates if available in the image's metadata.
- `-steg` will extract and format a hidden PGP key if one exists in the image.

Example usage:

```bash
python main.py -map resources/image.jpg
```

```bash
python main.py -steg resources/image.jpg
```


### GUI Usage

Alternatively, you can use the graphical user interface (GUI) for easier interaction.

To run the GUI:

```bash
python gui.py
```

The GUI allows you to open an image file and perform the following:

- Extract GPS coordinates from the image.
- Extract any hidden PGP key message.



## License

MIT License

Copyright (c) [2024] [Maksym Kotkov]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
