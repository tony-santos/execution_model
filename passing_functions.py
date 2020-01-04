def is_even(value):
    """Return True if *value* is even."""
    return (value % 2) == 0

def count_occurrences(target_list, predicate):
    """Return the number of times applying the callable *predicate* to a
    list element returns True."""
    return sum([1 for e in target_list if predicate(e)])

# bind my_predicate variable to a function. no parentheses indicates means that the variabvle is bound to the
# function itself instead of the value returned by calling the function
my_predicate = is_even
my_list = [2, 4, 6, 7, 9, 11]
# this function call passes a function as the second parameter

# call using name of function
result1 = count_occurrences(my_list, is_even)
print(result1)

# call using name of variable that is bound to a function
result2 = count_occurrences(my_list, my_predicate)
print(result2)
