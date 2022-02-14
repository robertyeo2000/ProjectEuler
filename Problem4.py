
def isPalindrome(num):
    string = str(num)
    return string == string[::-1]

largest = 0
for a in range(100,1000):
    for b in range(100,1000):
        if a * b > largest:
            if isPalindrome(a * b):
                largest = a * b
                print(largest)
