

number = 600851475143
i = 1

while i < number:
    if number % i == 0:
        print(i, number)
        number /= i
    i += 1

print(number)