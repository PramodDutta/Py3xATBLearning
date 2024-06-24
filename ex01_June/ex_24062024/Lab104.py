# Filter in Python
# The filter() function in Python is a built-in function
# allows you to filter elements in the list, tuple, set.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Filter on the above -> even ->
# new_list_Even = [2, 4, 6, 8, 10]


def is_even(num):
    return num % 2 == 0


def greater_5(num):
    return num > 5


# new_numbers_even = filter(is_even, numbers)
new_numbers_five = filter(greater_5, numbers)
print(list(new_numbers_five))
