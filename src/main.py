import argparse
from skimage import io
from skimage.util import img_as_float

from transformations import transform_slic, transform_quickshift, transform_watershed
from image_saving import save_image

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-i', '--input_path', required=True, help='Path to the input image', type=str)
argument_parser.add_argument('-o', '--output_path', required=True, help='Path to the output image', type=str)
argument_parser.add_argument('-t', '--transformation_type', default='watershed', required=True,
                             help='Transformation type invalid. Please look at the list of possible types',
                             choices=['slic', 'quickshift', 'watershed'], type=str)
argument_parser.add_argument('-d', '--dpi', required=True, help='Desired DPI', type=int)

args = vars(argument_parser.parse_args())
image = img_as_float(io.imread(args['input_path']))
if args['transformation_type'] == 'slic':
    input_image, transformed_image = transform_slic(image)
elif args['transformation_type'] == 'quickshift':
    input_image, transformed_image = transform_quickshift(image)
else:
    input_image, transformed_image = transform_watershed(image)

save_image(input_image, transformed_image, args['output_path'], args['dpi'])

