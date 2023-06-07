# Calculate the factorial of a number using lambda function.


factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
n = 5
result = factorial(n)
print(result)
