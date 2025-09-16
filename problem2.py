



n = int(input("Enter no. to find factorial: "))
def fact(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output
    
print(fact(n))