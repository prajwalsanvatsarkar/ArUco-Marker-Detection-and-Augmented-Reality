# ArUco Marker Image Overlay

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Code Explanation](#code-explanation)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
This project demonstrates how to overlay an image onto an ArUco marker detected in another image using OpenCV. The overlay image is resized, transformed, and blended with the original image to align with the perspective of the detected ArUco marker.

## Features
- Detect ArUco markers in an image.
- Resize and overlay an image onto the detected marker.
- Perspective transformation to match the overlay with the marker's perspective.
- Blending the overlay image seamlessly onto the original image.

## Installation
Follow these steps to install and set up the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/aruco-marker-overlay.git
    ```
2. Navigate to the project directory:
    ```bash
    cd aruco-marker-overlay
    ```
3. Install the required packages:
    ```bash
    pip install opencv-python opencv-contrib-python numpy
    ```

## Usage
Replace `"path_to_overlay_image"` and `"path_to_image"` in the script with the actual paths to your images. Then, run the script:

```bash
python script_name.py

## Configuration
image2 = cv2.imread("path_to_overlay_image", cv2.IMREAD_UNCHANGED)
scale_percent = 30

## Code Explaination
Function to diaplay Image
def image_shower(image):
    cv2.namedWindow('window', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('window', image)

Loading and Resizing Overlay Image
image2 = cv2.imread("path_to_overlay_image", cv2.IMREAD_UNCHANGED)
scale_percent = 30
width = int(image2.shape[1] * scale_percent / 100)
height = int(image2.shape[0] * scale_percent / 100)
dim = (width, height)
image2_resized = cv2.resize(image2, dim, interpolation=cv2.INTER_AREA)

Perspective Transformation
height, width, _ = image2_resized.shape
# (additional code for defining corners)
input_corners = np.float32([corner1, corner2, corner3, corner4])

Detect Markers and apply Transformations
aruco_type = cv2.aruco.DICT_6X6_250
aruco_dict = cv2.aruco.getPredefinedDictionary(aruco_type)
parameters = cv2.aruco.DetectorParameters()
image_path = "path_to_image"
image = cv2.imread(image_path)
arucocorners, ids, _ = cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters)
# (additional code for detecting and transforming)

Mask and Combine Image
_, mask = cv2.threshold(transformed_image2[:, :, 2], 1, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
image_bg = cv2.bitwise_and(image, image, mask=mask_inv)
overlay_fg = cv2.bitwise_and(transformed_image2, transformed_image2, mask=mask)
final_image = cv2.add(image_bg, overlay_fg)

Display the Image
image_shower(final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Contributing
We welcome contributions! Please follow these steps:

Fork the repository.
Create a new branch
git checkout -b feature-name

Make your changes and commit them:
git commit -m 'Add feature'

Push to the branch
git push origin feature-name

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or support, please contact Prajwal Sanvatsarkar at [sanvatsarkar.prajwal@gmail.com]

Replace placeholders such as `"path_to_overlay_image"`, `"path_to_image"`, `"script_name.py"`, `"yourusername"`, and `"your.email@example.com"` with your actual details. This comprehensive README provides clear instructions and explanations for users and contributors.






   




