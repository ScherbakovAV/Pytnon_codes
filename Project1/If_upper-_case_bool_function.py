def has_upper_case(word):
    word_to_lower = str.lower(word)
    return word_to_lower != word


print(has_upper_case(''))
