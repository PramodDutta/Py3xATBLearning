my_list = [1, 4, 5, 7]


def double_item(num):
    return num * 2


# Map()
# Takes each item from list
# execute function on it
# return same no of elements (list)
# return modified list

double_list = list(map(double_item, my_list))
print(double_list)
