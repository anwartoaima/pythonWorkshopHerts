import random

duplicates = []
seen = set()

randomList = [random.randint(1,100) for randomNumber in range(10)]

for num in randomList:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    seen.add(num)
print (randomList)
print (duplicates)