def trim_and_repeat(text, offset=0, repetitions=1):
    return text[offset:] * repetitions


print(trim_and_repeat("Какашонка", 0, 3))
