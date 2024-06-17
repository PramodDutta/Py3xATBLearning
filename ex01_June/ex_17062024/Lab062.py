# *args - any number of arguments
# print("Pramod", "Amit", "SB")


def sum_three(a=1, b=1, c=1):
    return a + b + c


# result = sum_three()
result1 = sum_three()
result2 = sum_three(1,2)
result3 = sum_three(1,2,3)
result4 = sum_three(a=10,b=67,c=45)
result5 = sum_three(b=67,a=10,c=45)
print(result1,result2,result3,result4,result5)