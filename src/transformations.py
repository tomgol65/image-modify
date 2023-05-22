from skimage.segmentation import slic, quickshift, watershed
from skimage.filters import sobel
from skimage.color import rgb2gray

RANDOM_SEED = 42


def transform_slic(input_image):
    transformed_image = slic(input_image)

    return input_image, transformed_image


def transform_quickshift(input_image):
    transformed_image = quickshift(input_image, random_seed=RANDOM_SEED)

    return input_image, transformed_image


def transform_watershed(input_image):
    gradient = sobel(rgb2gray(input_image))
    transformed_image = watershed(gradient)

    return input_image, transformed_image

#TODO: Add more transformation methods, like here -
#https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_segmentations.html#sphx-glr-auto-examples-segmentation-plot-segmentations-py
