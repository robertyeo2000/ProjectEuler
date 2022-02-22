from UsefulFunctions import numberOfDivisors

n = 1
while True:
    triangularNumber = n*(n+1)/2
    if numberOfDivisors(triangularNumber) > 500:
        print(triangularNumber)
        break
    n += 1
