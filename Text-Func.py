def compute_string_properties(string):
    length = len(string)
    sorted_characters = sorted(list(string), reverse=True)
    distinct_characters = len(set(string))
    return (length, sorted_characters, distinct_characters)

def tally_letters(string):
    return dict(Counter(string))
