## Image Transformation and Saving Tool
This Python script provides a command-line interface for applying various image transformations using scikit-image and saving the results using Matplotlib.

## Prerequisites
Make sure you have the necessary dependencies installed before using the script:

pip install scikit-image matplotlib

## Usage
python main.py -i <input_image_path> -o <output_image_path> -t <transformation_type> -d <dpi>

## Arguments
-i or --input_path: Path to the input image (required).
-o or --output_path: Path to the output image (required).
-t or --transformation_type: Type of transformation. Choose from 'slic', 'quickshift', 'watershed', or other available methods (default: 'watershed', required).
-d or --dpi: Desired DPI (required).

## Examples
python main.py -i input_images/input.jpg -o output_images/output.jpg -t slic -d 300

python main.py -i input_images/input.jpg -o output_images/output.jpg -t quickshift -d 200

python main.py -i input_images/input.jpg -o output_images/output.jpg -t watershed -d 150

## Image Transformation Types
The script supports various image transformation types. Current options include:

SLIC (Simple Linear Iterative Clustering): Segmentation based on k-means clustering.
Quickshift: Quick approximation of kernelized mean shift.
Watershed: Segmentation based on watershed algorithm using image gradients.

## Additional Transformations
To add more transformation methods, refer to the scikit-image documentation for segmentation methods: Segmentation - scikit-image

Edit the transformations.py file to include additional transformation methods.

## Saving Options
The transformed images are saved using the Matplotlib library. The save_image function in the image_saving module combines the input and transformed images, marks the boundaries, and saves the result in various formats.

## Supported Formats
JPEG (jpg, jpeg)
PNG (png)
PDF (pdf)
SVG (svg)
