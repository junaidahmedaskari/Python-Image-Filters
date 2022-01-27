


from L1_2_image_filters import *


def _choosing_function() -> str:
    """ 
    Displays the command options and promps the user to select one of them.
    Returns the selected option.
    
    Written by Nikita, Andrea, Kaitlyn, and Junaid
    
    """

    print('L)oad image S)ave-as')
    print('2)-tone 3)-tone X)treme contrast T)int sepia P)osterize')
    print('E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip')
    print('Q)uit')

    return input(': ').upper()


def _save_function(image: Image) -> Image:
    Cimpl.save_as(image, 'filtered_image.jpg')
    return image


def _filter_function(filter_name: str, image: Image) -> Image:
    """ 
    Returns an image with the applied filter depending on the name of 
    the filter name passed. 
    
    Will prompt the user to choose other parameters (threshold number) if 
    required for the filter they chose.
    
    Written by Nikita, Andrea, Kaitlyn, and Junaid
    """

    thresh_true = False

    filter_dict = {'2': two_toned_filter, '3': three_toned_filter, 'X': extreme_contrast,
                   'T': sepia, 'P': posterizing, 'E': detect_edges, 'I': detect_edges_better,
                   'V': flip_vertical, 'H': flip_horizontal, 'S': _save_function}

    if filter_name not in filter_dict:
        print('No such command')
        return image

    elif filter_name == '2':
        filter_to_call = filter_dict[filter_name]
        image = filter_to_call(image, 'yellow', 'cyan')

    elif filter_name == '3':
        filter_to_call = filter_dict[filter_name]
        image = filter_to_call(image, 'yellow', 'magenta', 'cyan')

    elif filter_name == 'E' or filter_name == 'I':
        while thresh_true == False:
            thresh = int(input('Threshold? (Integer between 0 and 255): '))
            if 0 <= thresh <= 255:
                thresh_true = True
            else:
                print('No such command\n')
        
        filter_to_call = filter_dict[filter_name]
        image = filter_to_call(image, thresh)

    else:
        filter_to_call = filter_dict[filter_name]
        image = filter_to_call(image)

    return image


def main_interface() -> None:
    """ 
    The main interface function that allows the user to load an image,
    calls the command/filter function and that displays the image 
    returned after a filter has been applied
    
    Written by Nikita, Andrea, Kaitlyn, Junaid
    """

    command = _choosing_function()
    chosen_image = None
    while command != 'Q':
        if command == 'L':
            chosen_image = Cimpl.load_image(Cimpl.choose_file())

        else:
            if type(chosen_image) == Cimpl.Image:
                chosen_image = _filter_function(command, chosen_image)
                Cimpl.show(chosen_image)

            else:
                print('No image loaded\n')

        command = _choosing_function()


main_interface()
