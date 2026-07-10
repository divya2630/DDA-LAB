# Iterative Factorial
def iterative_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Recursive Factorial
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)

# Main Program
n = int(input("Enter a number: "))

print("Iterative Factorial:", iterative_factorial(n))
print("Recursive Factorial:", recursive_factorial(n))
