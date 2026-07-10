# Iterative Fibonacci
def iterative_fibonacci(n):
    a, b = 0, 1
    print("Iterative Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Recursive Fibonacci
def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Main Program
n = int(input("Enter the number of terms: "))

iterative_fibonacci(n)

print("Recursive Fibonacci Series:")
for i in range(n):
    print(recursive_fibonacci(i), end=" ")
