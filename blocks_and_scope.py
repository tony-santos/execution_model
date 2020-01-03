GLOBAL_CONSTANT = 42

def print_some_weird_calculation(value):
    number_of_digits = len(str(value))

    def print_formatted_calculation(result):
        """
        used to demonstrate how function can access variables in outer scopes. result is part of this scope, value is
        from the containing function and GLOBAL_CONSTANT is part of the outermost scope.
        :param result:
        :return:
        """
        print('{value} * {constant} = {result}'.format(value=value,
            constant=GLOBAL_CONSTANT, result=result))
        print('{}   {}   {}'.format('^' * number_of_digits, '++', '****'))
        print('\nKey: ^ points to number passed into print_some_weird_calculation, + points to constant from outermost scope, * points to value passed into print_formatted_calculation from print_some_weird_calculation')

    print_formatted_calculation(value * GLOBAL_CONSTANT)

print_some_weird_calculation(123)
