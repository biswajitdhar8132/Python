def chocolate():
    n = int(input("Enter number for first stack: "))
    piles = []
    newnew = n
    for i in range(0, n):
        piles.append(newnew)
        newnew += 2
        print(piles)
chocolate()