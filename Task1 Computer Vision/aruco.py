import cv2
import numpy as np

# Function to display image
def image_shower(image):
    cv2.namedWindow('window', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('window', image)

# Load the overlay image
image2 = cv2.imread("path_to_overlay_image", cv2.IMREAD_UNCHANGED)  # Read with alpha channel

# Resize the overlay image
scale_percent = 30  # percent of original size
width = int(image2.shape[1] * scale_percent / 100)
height = int(image2.shape[0] * scale_percent / 100)
dim = (width, height)
image2_resized = cv2.resize(image2, dim, interpolation=cv2.INTER_AREA)

# Get the dimensions of the resized overlay image
height, width, _ = image2_resized.shape

# Define the corners of the overlay image
topleft = [0, 0]
topright = [width, 0]
bottomright = [width, height]
bottomleft = [0, height]

# Calculate the center of the overlay image
c = np.array([topleft, topright, bottomright, bottomleft], dtype=np.float32)
[x, y] = center = np.mean(c, axis=0)

# Define the width and height of the resized overlay image
w = width / 3
h = height / 3

# Define the corners of the resized overlay image
corner1 = (x - w / 2, y - h / 2)
corner2 = (x + w / 2, y - h / 2)
corner3 = (x + w / 2, y + h / 2)
corner4 = (x - w / 2, y + h / 2)

# Define the input corners for perspective transformation
input_corners = np.float32([corner1, corner2, corner3, corner4])

# Define the ArUco dictionary type
aruco_type = cv2.aruco.DICT_6X6_250

# Load ArUco dictionary
aruco_dict = cv2.aruco.getPredefinedDictionary(aruco_type)

# Define ArUco parameters
parameters = cv2.aruco.DetectorParameters()

# Load images and detect ArUco markers
image_path = f"path_to_image"
image = cv2.imread(image_path)
   

    # Detect ArUco markers in the main image
arucocorners, ids, _ = cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters)

if len(arucocorners) == 0:
        print(f"No ArUco markers found in image {image_path}")


    # Get the corners of the detected ArUco marker
Arucoc1 = arucocorners[0][0][0]
Arucoc2 = arucocorners[0][0][1]
Arucoc3 = arucocorners[0][0][2]
Arucoc4 = arucocorners[0][0][3]

    # Define the output corners for perspective transformation
output_corners = np.float32([Arucoc1, Arucoc2, Arucoc3, Arucoc4])

    # Calculate the perspective transformation matrix
M = cv2.getPerspectiveTransform(input_corners, output_corners)

    # Apply perspective transformation to the resized overlay image
transformed_image2 = cv2.warpPerspective(image2_resized, M, (image.shape[1], image.shape[0]))

# Fill the ArUco marker area in the original image with black
#_, mask= cv2.fillConvexPoly(transformed_image2, output_corners.astype(int), (0, 0, 0))

    # Create a mask for the overlayed region
_, mask = cv2.threshold(transformed_image2[:, :, 2], 1, 255, cv2.THRESH_BINARY)

    # Invert the mask
mask_inv = cv2.bitwise_not(mask)

    # Create image with alpha channel
image_bg = cv2.bitwise_and(image, image, mask=mask_inv)
overlay_fg = cv2.bitwise_and(transformed_image2, transformed_image2, mask=mask)

    # Combine the images
final_image = cv2.add(image_bg, overlay_fg)

    # Display the final image
image_shower(final_image)
cv2.waitKey(0)

cv2.destroyAllWindows()




































