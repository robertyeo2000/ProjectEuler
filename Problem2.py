

new = 2
old = 0
count = 0
while new <= 4000000:
    count += new
    new, old = 4*new + old, new

print(count)