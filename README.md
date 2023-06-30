# Image to FDF Converter

This script allows you to convert HEIC images with embedded depth information and basic images to FDF format. The FDF format is used for the 42 school FDF project.

## Features

- **HEIC to FDF Converter:** Convert HEIC images with embedded depth information to FDF format.
- **Image to FDF Converter:** Convert basic images to FDF format, using the luminosity of pixels as depth information.
- **Image + Depth Map to FDF Converter:** Combine a color image and a depth map to generate an FDF map.

## Requirements

- Python 3.x
- PIL (Python Imaging Library)
- pyheif

## Installation

1. Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/olimarmite/fdf-map-gen.git
```

2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage
The resulting FDF map will be saved as <image_name>.fdf in the same directory as the original image.
### HEIC to FDF Converter

Converts HEIC images with embedded depth information to FDF format.
HEIC images can be created in portrait mode on iPhone devices. 

```bash
python heic_to_fdf_converter.py <image_path> [-r REDUCTION_FACTOR] [-rgb]
```

- `<image_path>`: Path to the HEIC image file.
- `-r`, `--reduction-factor`: Reduction factor for image resizing (default: 0.1).
- `-rgb`: Encode color in RGB format (default: BGR).

### Image to FDF Converter

Converts basic images to FDF format, using the luminosity of pixels as depth information.

```bash
python image_to_fdf_converter.py <image_path> [-r REDUCTION_FACTOR] [-rgb]
```

- `<image_path>`: Path to the image file.
- `-r`, `--reduction-factor`: Reduction factor for image resizing (default: 0.1).
- `-rgb`: Encode color in RGB format (default: BGR).

### Image + Depth Map to FDF Converter

Combines a color image and a depth map to generate an FDF map.

```bash
python depth_to_fdf_converter.py <color_image_path> <depth_image_path> [-r REDUCTION_FACTOR] [-rgb]
```

- `<color_image_path>`: Path to the color image file.
- `<depth_image_path>`: Path to the depth image file.
- `-r`, `--reduction-factor`: Reduction factor for image resizing (default: 0.1).
- `-rgb`: Encode color in RGB format (default: BGR).

