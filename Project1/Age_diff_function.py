def get_age_difference(first_age, second_age):
    return "The age difference is " + str(abs(first_age - second_age))


actual = get_age_difference(1986, 2018)
print(actual)  # => The age difference is 17
