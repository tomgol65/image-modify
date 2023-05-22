from matplotlib import pyplot as plt
from skimage.segmentation import mark_boundaries

ACCEPTABLE_FORMATS = ['jpg', 'jpeg', 'png', 'pdf', 'svg']


def save_image(input_image, transformed_image, path, dpi):
    if path.endswith(tuple(ACCEPTABLE_FORMATS)):
        fig = plt.figure(dpi=dpi)
        ax = fig.add_subplot(1, 1, 1)
        ax.imshow(mark_boundaries(input_image, transformed_image))
        plt.axis('off')
        plt.savefig(path)
        plt.show()
    else:
        print(f'Please change desired output extensions. Acceptable extensions: {ACCEPTABLE_FORMATS}')
