def lcm(a, b):
    return a * b / gcd(a, b)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(gcd(12, 9), gcd(36, 21))

answer = 1
for i in range(1, 21):
    answer = lcm(i, answer)
    print(answer)
