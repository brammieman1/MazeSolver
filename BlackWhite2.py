#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Binarize (make it black and white) an image with Pyhton."""

from PIL import Image
from scipy.misc import imsave
import numpy

height = 0
width = 0

def binarize_image(img_path, threshold):
    """Binarize an image."""
    image_file = Image.open(img_path)
    image = image_file.convert('L')  # convert image to monochrome
    image = numpy.array(image)
    height, width = image_file.size
    image = binarize_array(image, threshold)
    #imsave(target_path, image)
    return image

def binarize_array(numpy_array, threshold=75):
    """Binarize a numpy array."""
    result = [[1 for x in range(width)] for y in range(height)]
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[i])):
           if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 0 #white
           else:
                numpy_array[i][j] = 1
    #print(numpy_array)
    return numpy_array


def get_parser():
    """Get parser object for script xy.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input",
                        dest="input",
                        help="read this file",
                        metavar="FILE",
                        required=True)
    parser.add_argument("-o", "--output",
                        dest="output",
                        help="write binarized file hre",
                        metavar="FILE",
                        required=True)
    parser.add_argument("--threshold",
                        dest="threshold",
                        default=200,
                        type=int,
                        help="Threshold when to show white")
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    binarize_image(args.input, args.threshold)
