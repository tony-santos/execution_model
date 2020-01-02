def add_to_tree(root, value_string):
    """Given a string of characters `value_string`, create or update a
    series of nested dictionaries where the value at each level is a nested dictionary of
    the characters that have been seen following the current character. Value for the last character is an empty
    dictionary.

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
print("adding 'abc' to empty tree")
add_to_tree(tree, mystring)
<<<<<<< HEAD
print(type(tree))
print("\ntree:", tree)
print("\ntree['a']:", tree['a'])
print("\ntree['a']['b']:", tree['a']['b'])
print("\ntree['a']['b']['c']:", tree['a']['b']['c'])
print("adding 'abd' to existing tree")
add_to_tree(tree, 'abd')
print("\ntree['a']:", tree['a'])
print("\ntree['a']['b']:", tree['a']['b'])
#c & d are at the same level because they were both seen after b
print("\ntree['a']['b']['c']:", tree['a']['b']['c'])
print("\ntree['a']['b']['d']:", tree['a']['b']['d'])
print("adding 'abe' to existing tree")
add_to_tree(tree, 'abe')
print("\ntree['a']:", tree['a'])
print("\ntree['a']['b']:", tree['a']['b'])
#c, d, e are at the same level because they were both seen after b
print("\ntree['a']['b']['c']:", tree['a']['b']['c'])
print("\ntree['a']['b']['d']:", tree['a']['b']['d'])
print("\ntree['a']['b']['e']:", tree['a']['b']['e'])
print("adding 'cf' to existing tree")
add_to_tree(tree, 'abcf')
print("\ntree['a']:", tree['a'])
print("\ntree['a']['b']:", tree['a']['b'])
print("\ntree['a']['b']['c']:", tree['a']['b']['c'])

=======
print(type(tree))  
print(tree['a']['b'])
>>>>>>> 4176eecb54f894328f0456a43af52a2d4d98aaa8
