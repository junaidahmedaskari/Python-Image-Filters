# ECOR 1051 MILESTONE #2
# Group L1-2
# Submission Date: 24/11/2019


import Cimpl
import typing

Image = typing.NewType('Image', str)
Color = typing.Tuple[int, int, int]


def _adjust_component(number: int) -> int:
    """Returns an integer based off of the quadrant the given number lays in.

    >>> _adjust_component(230)
    223
    >>> _adjust_component(50)
    31
    >>> _adjust_component(191)
    159

    Written by Kaitlyn Johnson 101064572
    """

    if 0 <= number <= 63:
        return 31
    if 64 <= number <= 127:
        return 95
    if 128 <= number <= 191:
        return 159
    if 192 <= number <= 255:
        return 223


def _choose_color(color_name: str) -> Color:
    """
    Returns the proper color tuple given a color name

    Colour options include: black, white, red, blue, yellow, lime, cyan,
    magenta, gray

    >>> _choose_color('black')
    (0, 0, 0)
    >>> _choose_color('white')
    (255, 255, 255)
    >>> _choose_color('lime')
    (0, 255, 0)

    Written By Nikita Yovchev (101140798)
    """

    if color_name == "black":
        return 0, 0, 0

    elif color_name == "white":
        return 255, 255, 255

    elif color_name == "red":
        return 255, 0, 0

    elif color_name == "blue":
        return 0, 0, 255

    elif color_name == "yellow":
        return 255, 255, 0

    elif color_name == "lime":
        return 0, 255, 0

    elif color_name == "cyan":
        return 0, 255, 255

    elif color_name == "magenta":
        return 255, 0, 255

    elif color_name == "gray":
        return 128, 128, 128


def _grayscale(image: Image) -> Image:
    """Return a grayscale copy of image.

    >>> image = Cimpl.load_image(Cimpl.choose_file())
    >>> gray_image = _grayscale(image)
    >>> Cimpl.show(gray_image)

    Written by D. Bailey (Carleton University)
    """
    new_image = Cimpl.copy(image)

    for x, y, (r, g, b) in image:
        # Use the pixel's brightness as the value of RGB components for the
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.

        brightness = (r + g + b) // 3

        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int

        gray = Cimpl.create_color(brightness, brightness, brightness)
        Cimpl.set_color(new_image, x, y, gray)

    return new_image


def blue_filter(picture: Image) -> Image:
    """
    Returns a copy of the given picture that is blue monochromatic.
    The blue value of each pixel determines the brightness of the blue
    in the filtered copy.

    >>> image = Cimpl.load_image(Cimpl.choose_file())
    >>> blue_image = blue_filter(image)
    >>> Cimpl.show(blue_image)

    Written by Nikita Yovchev (101140798) using Cimpl library made at
    Carleton University, D. Bailey et al.
    """

    copy_image = Cimpl.copy(picture)

    for x, y, (r, g, b) in copy_image:
        new_blue = Cimpl.create_color(0, 0, b)
        Cimpl.set_color(copy_image, x, y, new_blue)

    return copy_image


def green_filter(image: Image) -> Image:
    """
    Returns a copy of the image chosen in green.

    >>> image = Cimpl.load_image(Cimpl.choose_file())
    >>> Green_Image = green_filter(image)
    >>> Cimpl.show(Green_Image)

    Written by Andrea Chan 101107608 from simple_Cimple_filters
    at Carleton University by D. Bailey
    """

    new_image = Cimpl.copy(image)

    for x, y, (r, g, b) in image:
        new_green = Cimpl.create_color(0, g, 0)
        Cimpl.set_color(new_image, x, y, new_green)

    return new_image


def red_filter(image: Image) -> Image:
    """
    Returns a new_copy of a picture chosen in red.

    >>> image = Cimpl.load_image(Cimpl.choose_file())
    >>> red_image = red_filter(image)
    >>> Cimpl.show(red_image)

    Written by Kaitlyn Johnson 101064572 from simple_Cimpl_filters
    at Carleton University by D. Bailey
    """

    new_image = Cimpl.copy(image)

    for x, y, (r, g, b) in image:
        new_red = Cimpl.create_color(r, 0, 0)
        Cimpl.set_color(new_image, x, y, new_red)

    return new_image


def combine(red_image: Image, green_image: Image, blue_image: Image) -> Image:
    """
    This functions takes the red, green and blue images and returns another
    image with the red, blue and green monochromatics combined.

    >>> red_image= Cimpl.load_image(Cimpl.choose_file())
    >>> blue_image = Cimpl.load_image(Cimpl.choose_file())
    >>> green_image = Cimpl.load_image(Cimpl.choose_file())
    >>> combine_image = combine(red_image, green_image, blue_image)
    >>> Cimpl.show(combine_image)

    Name: Junaid Ahmed Askari
    Lab: L2-1
    Instructor: Donald Bailey

    """

    red = Cimpl.copy(red_image)
    green = Cimpl.copy(green_image)
    blue = Cimpl.copy(blue_image)
    color_images = Cimpl.copy(green_image)

    for x, y, (r, g, b) in color_images:
        red_color = Cimpl.get_color(red, x, y)
        green_color = Cimpl.get_color(green, x, y)
        blue_color = Cimpl.get_color(blue, x, y)

        new_image_color = Cimpl.create_color(red_color[0], green_color[1], blue_color[2])
        Cimpl.set_color(color_images, x, y, new_image_color)

    return color_images


def two_toned_filter(picture: Image, colour_1: str, colour_2: str) -> Image:
    """Returns a copy of the given picture that recolored in the two
    tones given: the first tone will be for the darker pixels and the
    second tone for the lighter pixels.

    Colour options include: black, white, red, blue, yellow, lime, cyan,
    magenta, gray

    >>> image = Cimpl.load_image( Cimpl.choose_file())
    >>> two_toned_image = two_toned_filter(image, 'red', 'blue')
    >>> Cimpl.show(two_toned_image)

    Written by Nikita Yovchev (101140798) using Cimpl library made at
    Carleton University, D. Bailey et al.
    """

    copy_image = Cimpl.copy(picture)

    for x, y, (r, g, b) in copy_image:
        if ((r + g + b) // 3) <= 127:
            new_color = _choose_color(colour_1)
            Cimpl.set_color(copy_image, x, y, Cimpl.create_color(new_color[0], new_color[1], new_color[2]))

        else:
            new_color = _choose_color(colour_2)
            Cimpl.set_color(copy_image, x, y, Cimpl.create_color(new_color[0], new_color[1], new_color[2]))

    return copy_image


def three_toned_filter(picture: Image, colour_1: str, colour_2: str, colour_3: str) -> Image:
    """Returns a copy of the given picture that recolored in the three tones
    given: the first tone will be for the darkest pixels, the second tone for
    the medium brightness pixels, and the third for the lighter pixels.

    Colour options include: black, white, red, blue, yellow, lime, cyan, magenta, gray

    >>> image = Cimpl.load_image(Cimpl.choose_file())
    >>> three_toned_image = three_toned_filter(image, 'magenta', 'lime', 'cyan')
    >>> Cimpl.show(three_toned_image)

    Written by Nikita Yovchev (101140798) using Cimpl library made at
    Carleton University, D. Bailey et al.
    """

    copy_image = Cimpl.copy(picture)

    for x, y, (r, g, b) in copy_image:
        if ((r + g + b) // 3) <= 84:
            new_color = _choose_color(colour_1)
            Cimpl.set_color(copy_image, x, y, Cimpl.create_color(new_color[0], new_color[1], new_color[2]))

        elif 85 <= ((r + g + b) // 3) <= 170:
            new_color = _choose_color(colour_2)
            Cimpl.set_color(copy_image, x, y, Cimpl.create_color(new_color[0], new_color[1], new_color[2]))

        else:
            new_color = _choose_color(colour_3)
            Cimpl.set_color(copy_image, x, y, Cimpl.create_color(new_color[0], new_color[1], new_color[2]))
            
    return copy_image


def extreme_contrast(image: Image) -> Image:
    """Returns a copy of an image in which the copy is an extreme contrasted
    version of the original image.

    >>> image = Cimpl.load_image(Cimpl.choose_file())
    >>> contrast = extreme_contrast(image)
    >>> Cimpl.show(contrast)

    Written by Andrea Chan 101107608
    """

    contrast_image = Cimpl.copy(image)
    for x, y, (r, g, b) in contrast_image:
        r, g, b = Cimpl.get_color(contrast_image, x, y)
        if 0 <= r <= 127:
            contrast_red = 0
        elif 128 <= r <= 255:
            contrast_red = 255
        if 0 <= g <= 127:
            contrast_green = 0
        elif 128 <= g <= 255:
            contrast_green = 255
        if 0 <= b <= 127:
            contrast_blue = 0
        elif 128 <= b <= 255:
            contrast_blue = 255

        new_image_color = Cimpl.create_color(contrast_red, contrast_green, contrast_blue)
        Cimpl.set_color(contrast_image, x, y, new_image_color)

    return contrast_image


def sepia(new_image: Image) -> Image:
    """
    The function takes the gray image, created by the grayscale filter provided by the
    prof on CULEARN, and adds a sepia tint on it, which is a hint of yellow.

    >>> image = Cimpl.load_image(Cimpl.choose_file())
    >>> sepia_image = sepia(image)
    >>> Cimpl.show(sepia_image)

    written by: Junaid Ahmed Askari
    Student number: 101111448
    """

    sepia_image = Cimpl.copy(_grayscale(new_image))

    for x, y, (r, g, b) in new_image:
        darkness = Cimpl.get_color(sepia_image, x, y)

        if sum(darkness) <= 189:
            new_color = Cimpl.create_color(darkness[0] * 1.1, darkness[1], darkness[2] * 0.9)
            Cimpl.set_color(sepia_image, x, y, new_color)

        elif 189 <= sum(darkness) <= 573:
            new_color = Cimpl.create_color(darkness[0] * 1.15, darkness[1], darkness[2] * 0.85)
            Cimpl.set_color(sepia_image, x, y, new_color)

        elif sum(darkness) >= 573:
            new_color = Cimpl.create_color(darkness[0] * 1.08, darkness[1], darkness[2] * 0.93)
            Cimpl.set_color(sepia_image, x, y, new_color)

    return sepia_image


def posterizing(image: Image) -> Image:
    """Returns a copy of the Image that is posterized (simplified colors).

    >>> image = Cimpl.load_image(Cimpl.choose_file())
    >>> post_image = posterizing(image)
    >>> Cimpl.show(post_image)

    Written by Kaitlyn Johnson 101064572 from simple_Cimpl_filters at Carleton
    University by D. Bailey
    """

    new_image = Cimpl.copy(image)

    for x, y, (r, g, b) in image:
        adjusted_r = _adjust_component(r)
        adjusted_g = _adjust_component(g)
        adjusted_b = _adjust_component(b)

        new_posterizing = Cimpl.create_color(adjusted_r, adjusted_g, adjusted_b)
        Cimpl.set_color(new_image, x, y, new_posterizing)

    return new_image


def detect_edges(picture: Image, threshold: int) -> Image:
    """Returns a black and white copy of the image provided with a specific
    contrast threshold that is composed only of the edges (looks like a sketch).

    >>> image = Cimpl.load_image(Cimpl.choose_file())
    >>> edge_image = detect_edges(image, 12)
    >>> Cimpl.show(edge_image)

    Written by Nikita Yovchev (101140798) using Cimpl library made at
    Carleton University, D. Bailey et al.
    """

    white = Cimpl.create_color(255, 255, 255)
    black = Cimpl.create_color(0, 0, 0)
    copy_image = Cimpl.copy(picture)

    for x, y, (r, g, b) in copy_image:
        if y < (Cimpl.get_height(copy_image) - 1):
            pixel_colour_bot = Cimpl.get_color(copy_image, x, y + 1)

            average_top = (r + b + g) // 3
            average_bot = (pixel_colour_bot[0] + pixel_colour_bot[1] + pixel_colour_bot[2]) // 3

            if abs(average_bot - average_top) <= threshold:
                Cimpl.set_color(copy_image, x, y, white)

            else:
                Cimpl.set_color(copy_image, x, y, black)

    return copy_image


def detect_edges_better(picture: Image, thresh: int) -> Image:
    """Returns a new and improved edge-only copy of the picture with a given
    threshold. This edged image is better because it compares the contrast
    between more pixels than the previous edge function.

    >>> image = Cimpl.load_image(Cimpl.choose_file())
    >>> edge_image = detect_edges_better(image, 12)
    >>> Cimpl.show(edge_image)

    Written by Kaitlyn Johnson (101064572) and Nikita Yovchev (101140798)
    using Cimpl library made at  Carleton University, D. Bailey et al.
    """

    white = Cimpl.create_color(255, 255, 255)
    black = Cimpl.create_color(0, 0, 0)
    copy_image = Cimpl.copy(picture)

    for x, y, (r, g, b) in copy_image:
        if y == (Cimpl.get_height(copy_image) - 1):
            if x != (Cimpl.get_width(copy_image) - 1):
                pixel_color_right = Cimpl.get_color(copy_image, x + 1, y)
                average_right = (pixel_color_right[0] + pixel_color_right[1] + pixel_color_right[2]) // 3
                average_current = (r + g + b) // 3

                if abs(average_right - average_current) < thresh:
                    Cimpl.set_color(copy_image, x, y, white)

                else:
                    Cimpl.set_color(copy_image, x, y, black)

        elif x == (Cimpl.get_width(copy_image) - 1):
            if y != (Cimpl.get_height(copy_image) - 1):
                pixel_color_bot = Cimpl.get_color(copy_image, x, y + 1)
                average_bot = (pixel_color_bot[0] + pixel_color_bot[1] + pixel_color_bot[2]) // 3
                average_current = (r + g + b) // 3

                if abs(average_bot - average_current) < thresh:
                    Cimpl.set_color(copy_image, x, y, white)

                else:
                    Cimpl.set_color(copy_image, x, y, black)

        elif x < (Cimpl.get_width(copy_image) - 1) and y < (Cimpl.get_height(copy_image) - 1):
            pixel_color_bot = Cimpl.get_color(copy_image, x, y + 1)
            pixel_color_right = Cimpl.get_color(copy_image, x + 1, y)

            average_bot = (pixel_color_bot[0] + pixel_color_bot[1] + pixel_color_bot[2]) // 3
            average_right = (pixel_color_right[0] + pixel_color_right[1] + pixel_color_right[2]) // 3
            average_current = (r + g + b) // 3

            if abs(average_bot - average_current) and abs(average_right - average_current) < thresh:
                Cimpl.set_color(copy_image, x, y, white)

            else:
                Cimpl.set_color(copy_image, x, y, black)

    return copy_image


def flip_vertical(image: Image) -> Image:
    """
    Returns a copy of the Image provided that is flipped along a vertical line in the center.

    >>> choose_image = Cimpl.load_image(Cimpl.choose_file())
    >>> vertical_image = flip_vertical(choose_image)
    >>> Cimpl.show(vertical_image)

    Written by: Junaid Ahmed Askari
    Student Number: 101111448
    """

    vertically_flipped = Cimpl.copy(image)
    height_of_image = Cimpl.get_height(vertically_flipped)
    half_width = (Cimpl.get_width(vertically_flipped)) // 2

    for y in range(0, height_of_image):
        for x in range(0, half_width):
            original_colour = Cimpl.get_color(vertically_flipped, x, y)
            opposite_colour = Cimpl.get_color(vertically_flipped, -x, y)

            Cimpl.set_color(vertically_flipped, x, y, opposite_colour)
            Cimpl.set_color(vertically_flipped, -x, y, original_colour)

    return vertically_flipped


def flip_horizontal(image: Image) -> Image:
    """Returns a copy of the image selected flipped along the middle of the horizon line

    >>> image = Cimpl.load_image(Cimpl.choose_file())
    >>> horizontal_image = flip_horizontal(image)
    >>> Cimpl.show(horizontal_image)

    Written by Andrea Chan 101107608 using Cimpl Library
    """

    horizontal_image = Cimpl.copy(image)
    length = Cimpl.get_height(horizontal_image)
    width = Cimpl.get_width(horizontal_image)

    for x in range(0, width):
        for y in range(0, length // 2):
            top_colour = Cimpl.get_color(horizontal_image, x, y)
            bottom_colour = Cimpl.get_color(horizontal_image, x, -y)

            Cimpl.set_color(horizontal_image, x, y, bottom_colour)
            Cimpl.set_color(horizontal_image, x, -y, top_colour)

    return horizontal_image
