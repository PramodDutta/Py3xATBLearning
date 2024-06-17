# Factorial
import math
import math

n = 5
factorial = 1
# result = math.factorial(5)
# print(result)
# range(1,10) #1-9

while n > 0:
    factorial = factorial * n
    n = n - 1


for i in range(1, n + 1):
    factorial *= i


print(factorial)
