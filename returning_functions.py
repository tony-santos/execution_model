def surround_with(surrounding):
    """Return a function that takes a single argument and returns a function that will surround the word with that
    value."""
    def surround_with_value(word):
        return '{}{}{}'.format(surrounding, word, surrounding)
    return surround_with_value

def transform_words(content, targets, transform):
    """Return a string based on *content* but with each occurrence
    of words in *targets* replaced with
    the result of applying *transform* function to it."""
    result = ''
    for word in content.split():
        if word in targets:
            result += ' {}'.format(transform(word))
        else:
            result += ' {}'.format(word)
    return result

markdown_string = 'My name is Jeff Knupp and I like Python but I do not own a Python'
markdown_string_italicized = transform_words(markdown_string, ['Python', 'Jeff'],
        surround_with('*'))
print(markdown_string_italicized)