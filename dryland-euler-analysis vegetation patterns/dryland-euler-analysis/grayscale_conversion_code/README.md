# Grayscale Conversion Code

This project performs grayscale conversion, center cropping, and resizing for vegetation images using OpenCV in Python.

## Features
- Converts input images to grayscale
- Crops the central 350x350 region (or smaller if the image is smaller)
- Resizes the cropped image to 50x50 pixels
- Saves the processed images to an output folder

## Requirements
Install the required packages with pip:
```bash
pip install opencv-python
```

## Usage
Edit the `input_folder` and `output_folder` paths in the script:
```python
input_folder = "path/to/your/input/folder"
output_folder = "path/to/your/output/folder"
```
Run the script:
```bash
python grayscale_conversion_code.py
```

## Project Structure
```
.
├── grayscale_conversion_code.py
├── README.md
├── requirements.txt
├── input_images/       # Put your original images here
└── processed_images/   # Processed grayscale images saved here
```

## Example
Original: `tree.jpg`

Processed Output: `tree_processed_50x50.png`

## License
This project is open-source and available under the MIT License.