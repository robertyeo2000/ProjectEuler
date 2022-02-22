
count = 0
for a in range(1, 101):
    for b in range(1, 101):
        if a != b:
            count += a*b

print(count)

