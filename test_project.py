from project import print_available_colors, show_trash, print_list_of_items

def test_print_available_colors():
    assert print_available_colors() == True

def test_show_trash():
    assert show_trash() == True

def test_print_list_of_items():
    assert print_list_of_items() == True
