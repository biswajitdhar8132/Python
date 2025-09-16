'''1) Write a Python program to find the GCD of two numbers (take input from the
 user) using Euclid's algorithm.'''


def gcd(n, m):
    while n % m != 0:
        k = n
        l = m
        n = l
        m = k % l
    return m
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The GCD is:", gcd(a, b))
