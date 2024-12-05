import math

import numpy as np
from PIL import Image

from line import plot_line
from triangle import draw_triangle
from fractal import draw_fractal


# Triangular fractal with shrink_side_by = 1/2 and max_depth = 2
if __name__ == '__main__':

    # Define the size of our image
    pixels = np.zeros( (500,500,3), dtype=np.uint8 )

    draw_fractal(
        center=(200,250),
        side_length=300,
        degrees_rotate=0,
        thickness=1,
        colour=(255,200,0),
        pixels=pixels,
        shrink_side_by=0.5,
        max_depth=8)

    # Turn our pixel array into a real picture
    img = Image.fromarray(pixels)

    # Show our picture, and save it
    # img.show()
    img.save('Fractal.png')
