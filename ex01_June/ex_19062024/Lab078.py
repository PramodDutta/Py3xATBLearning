# lambda arguments: expression

# def find_odd_even(num):
#     if num%2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
#
# find_odd_even(5)

check_even_odd = lambda num: "Even" if num%2 ==0 else "Odd"
print(check_even_odd(11))