def string_or_not(text):
    return isinstance(text, str) and 'yes' or 'no'


print(string_or_not('Hexlet'))  # yes
print(string_or_not(10))        # no
print(string_or_not(''))        # yes
print(string_or_not(False))     # no
