def add_to_tree(root, value_string):
    """Given a string of characters `value_string`, create or update a
    series of dictionaries where the value at each level is a dictionary of
    the characters that have been seen following the current character.

    Example:
    >>> my_string = 'abc'
    >>> tree = {}
    >>> add_to_tree(tree, my_string)
    >>> print(tree['a']['b'])
    {'c': {}}
    >>> add_to_tree(tree, 'abd')
    >>> print(tree['a']['b'])
    {'c': {}, 'd': {}}
    >>> print(tree['a']['d'])
    KeyError 'd'
    """

    for character in value_string:
        root = root.setdefault(character, {})

def list_changer(input_list):
    print("\nbefore any changes made to input argument")
    print(input_list)
    input_list[0] = 10
    print("\nafter 1st element changed to input argument. this change should persist after return")
    print(input_list)

    print("\nafter rebinding name input_list to a new object. this change will not persist after exiting from function")
    input_list = list(range(1, 10))
    print(input_list)
    print("\nafter changing 1st element of rebound input_list object. this change will not persist after exiting from function")
    input_list[0] = 20
    print(input_list)

test_list = [5, 5, 5]
list_changer(test_list)
print("\nafter return from list_changer function. should see initial change made in list_changer")
print(test_list)

print("\n\n")
mystring = 'abc'
tree = {}
add_to_tree(tree, mystring)
print(type(tree))  
print(tree['a']['b'])
