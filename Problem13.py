
total = 0
with open('Problem13Input.txt') as file:
    for line in file:
        total += int(line.rstrip())
print(str(total)[0:10])
