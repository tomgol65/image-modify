import os
import pytest
import numpy as np
from skimage import io
from skimage.util import img_as_float

from main import argument_parser, transform_slic, transform_quickshift, transform_watershed, save_image


@pytest.mark.parametrize('input_path, output_path, transformation_type, dpi', [
    ('test_image.jpg', 'test_output.jpg', 'slic', 100),
    ('test_image.jpg', 'test_output.jpg', 'quickshift', 200),
    ('test_image.jpg', 'test_output.jpg', 'watershed', 300)
])
def test_main(input_path, output_path, transformation_type, dpi):
    # Generate a test image
    image = np.random.rand(100, 100, 3)
    io.imsave(input_path, img_as_float(image))

    # Run the transformation
    args = argument_parser.parse_args(['-i', input_path, '-o', output_path, '-t', transformation_type, '-d', str(dpi)])
    input_image, transformed_image = None, None
    if transformation_type == 'slic':
        input_image, transformed_image = transform_slic(image)
    elif transformation_type == 'quickshift':
        input_image, transformed_image = transform_quickshift(image)
    else:
        input_image, transformed_image = transform_watershed(image)

    # Save the transformed image
    save_image(input_image, transformed_image, output_path, dpi)

    # Load the saved image and compare with the transformed image
    saved_image = io.imread(output_path)
    assert np.allclose(saved_image, transformed_image)

    # Cleanup the test image and output file
    os.remove(input_path)
    os.remove(output_path)

