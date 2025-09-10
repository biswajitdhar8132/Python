name = input("Your name? ")
print("Hello ,", name )

salary = int(input("Your salary? "))

if salary <= 100000:
    tax = 0
    print("no tax")

    
if 100000 < salary <= 500000:
    tax = ( salary - 100000 ) * ( 10/100)
    print("Pay", tax, "for tax.")

if salary > 500000:
    tax = ( salary - 500000 ) * ( 20/100) + ( 400000 * (10/100))
    print("Pay", tax, "for tax.")

#10% tax on 1-5L and 20% on more than 5L.