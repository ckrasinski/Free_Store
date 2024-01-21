import sys

colors = [
    "white",
    "gold",
    "lightgreen",
    "cyan",
    "navy",
    "darkbrown",
    "darkpink",
    "lightorange",
    "lightsea"
]

items = []
removed = []

class Item:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return self.color + " " + self.name

def main():
    print("Welcome to the free store! Here you can add items for your room for free!")
    while True:
        option = input("Select option(a - add, r - remove, s - show, t - trash, x - exit): ")
        option = option.strip().lower()
        if option in "arstx":
            match option:
                case "a":
                    add_item()
                case "r":
                    remove_item()
                case "s":
                    print_list_of_items()
                case "t":
                    show_trash()
                case "x":
                    print("It was a great adventure!")
                    sys.exit(0)
        else:
            print("Invalid option!")


def add_item():
    name = input("What's name of the item? ")
    while True:
        color = input("What's color of the item? (h for help) ")
        if color.strip().lower() == "h":
            print_available_colors()
        elif color not in colors:
            print("Color not available! Choose other!")
        else:
            item = Item(name, color)
            items.append(item)
            print("Item successfully added to your room!")
            break
    return True

def remove_item():
    while True:
        try:
            color, name = input("What item do you want to remove? (color name) ").split(" ")
            break
        except:
            print("Invalid data")
            continue
    found = False
    for i in range(len(items)):
        if name == items[i].name and color == items[i].color:
            items.pop(i)
            found = True
            print("Item successfully removed.")
            removed.append(Item(name, color))
            break
    if not found:
        print("Item already removed!")


def print_available_colors():
    for color in colors:
        print(color, end=" ")
    print()
    return True

def show_trash():
    if removed:
        for item in removed[:-1]:
            print(item, end=", ")
        print(items[-1])
    else:
        print("Trash is empty!")
    return True

def print_list_of_items():
    if items:
        for item in items[:-1]:
            print(item, end=", ")
        print(items[-1])
    else:
        print("Room is empty!")
    return True

if __name__ == "__main__":
    main()
