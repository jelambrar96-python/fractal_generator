import math

import numpy as np
from PIL import Image

from line import plot_line


def draw_triangle(center, side_length, thickness, colour, pixels):
    
    # The height of an equilateral triangle is, h = ½(√3a)
    # where 'a' is the side length
    triangle_height = round(side_length * math.sqrt(3)/2)

    # The top corner
    top = [center[0] - triangle_height/2, center[1]]

    # Bottom left corner
    bottom_left = [center[0] + triangle_height/2, center[1] - side_length/2]

    # Bottom right corner
    bottom_right = [center[0] + triangle_height/2, center[1] + side_length/2]

    # Draw a line between each corner to complete the triangle
    plot_line(top, bottom_left, thickness, colour, pixels)
    plot_line(top, bottom_right, thickness, colour, pixels)
    plot_line(bottom_left, bottom_right, thickness, colour, pixels)


if __name__ == '__main__':

    # Define the size of our image
    pixels = np.zeros( (500,500,3), dtype=np.uint8 )

    # Draw a Triangle
    draw_triangle(
        center=(250,250), 
        side_length=300,
        thickness=2,
        colour=(255,200,0),
        pixels=pixels
    )

    # Turn our pixel array into a real picture
    img = Image.fromarray(pixels)

    # Show our picture, and save it
    # img.show()
    img.save('Triangle.png')
