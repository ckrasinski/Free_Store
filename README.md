    # FREE STORE
    #### Video Demo:  https://youtu.be/0zyvf2D1nMM?si=aPt7YOE4mkZQ6HAJ
    #### Description:
        For the CS50P (Introduction to programming with Python) final project I've
    implemented "Free Store".
        It gives you access to buy (virtually) items for your room for free! You can choose
    from nine differernt colors for each of your items : white, gold, lightgreen, navy,
    darkbrown, darkpink, lightsea, cyan. You are absolutely free to name each of your items
    but for the color you have to choose from that nine colors I've mentioned above. You can
    also remove items from your room, show list of all your items in the room, display all
    available colors, and see what you've putted into trash. And also you can exit whole
    application!
        Now I will tell what exactly my code does.
        In "project.py" I've implemented a list of colors called "colors", an empty list
    called "items", an empty list called "removed", a class called "Item" and six functions
    called : "main", "add_item", "remove_item", "print_available_colors", "show_trash",
    "print_list_of_items". And finally it also has the implementation of script that just
    calls the "main" function which is (as you propably figured out hihi) the main function
    that just does all the work. Now I will tell more about each of those things
    respectively.
        The list called "items" stores list of item objects added to the room. At first it is empty.
        The list called "removed" stores list of item objects removed from the room. At first it is empty.
        The class called "Item" represents an item which can be added to the room. It has __init__ and __str__ functions. The __init__ initalizies attributes "name", which is the name of the item and "color" which is the color of the
        item. They are given to __init__ function as parameters. The __str__ function convert object to string. It returns concatenation of color of the object, a space and the name of the object.
        The function called "main" at first displays welcome message. Then in infinite loop asks the person to select one of the options: add, remove, show, trash and exit. The shortcuts for them are: "a" for add, "r" for the remove,
        "s" for show, "t" for trash and "x" for exit. "Add" allows you to add item for
        your room, "remove" allows you to remove item from your room, "show" allows
        you to show all of items added to your room, "trash" allows you to show
        items removed from your room, "exit" exits the appliccation. After you type
        your choice it's stripped and lowered to lowercase. Then it's checked if it's
        in string "arstx" which is concatenation of all the shortcuts of the options.
        If it is in, the user typed correct option. If it's not in, computer displays
        message "Invalid option" and the loop starts over. Then, if you have chosen
        correctly it checks which of the option you have chosen. If it's "a" it calls
        "add_item" function, if it's "r" it calls "remove_item" function, if it's "s"
        it calls "show_items" function, if it's "t" it calls "show_trash" function and
        if it's "x" it gives you ending message and exits the program via sys.exit().
        The rest of the functions are so simple, there's no need for explaination. I believe you can figure out what they does by yourself :). Thank you very much!



