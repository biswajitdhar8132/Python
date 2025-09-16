'''3. Write a program that prints the sum of the digits of a positive integer n. For 
example, if n = 1234, then the output would be: 1 + 2 + 3 + 4 = 10.'''

n = int(input("Enter a positive integer: "))
total = 0
expression_no = [] 

while n > 0:
    digit = n % 10
    total += digit
    expression_no.insert(0, str(digit))  
    n //= 10

expression = " + ".join(expression_no)
print(f"{expression} = {total}")
