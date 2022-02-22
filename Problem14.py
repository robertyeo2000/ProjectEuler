import time


start = time.time()
largest = [1, 0]
numbersAlreadySeen = []
for start in range(1, 101):
    print(start)
    n = start
    length = 0
    while n != 1:
        if n in numbersAlreadySeen:
            # ends this loop
            n = 2
        else:
            numbersAlreadySeen.append(n)
        n = int(n/2) if n % 2 == 0 else 3 * n + 1
        length += 1
    if largest[1] < length:
        largest = [start, length]
print(largest)
end = time.time()
print(end - start)






# def shouldBreak(seenNumbers):
#     for i in range(1, 1001):
#         if i not in seenNumbers:
#             return False
#     return True
#
#
# start = time.time()
#
# seenNumbers = [1]
# seenNumbersWithStep = [[1]]
# step = 0
# while True:
#     seenNumbersWithStep.append([])
#     for number in seenNumbersWithStep[step]:
#         nextNumber = 2 * number
#         if nextNumber not in seenNumbers:
#             seenNumbers.append(nextNumber)
#             seenNumbersWithStep[step + 1].append(nextNumber)
#         nextNumber = (number - 1) / 3
#         if nextNumber == int(nextNumber):
#             nextNumber = int(nextNumber)
#             if nextNumber not in seenNumbers:
#                 seenNumbers.append(nextNumber)
#                 seenNumbersWithStep[step + 1].append(nextNumber)
#     step += 1
#     if shouldBreak(seenNumbers):
#         break
# print(seenNumbersWithStep)
# end = time.time()
# print(end - start)
