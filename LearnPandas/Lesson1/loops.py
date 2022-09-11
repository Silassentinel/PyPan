# cheatsheets for loops

# for loop
for i in range(10):
    print(i)

# while loop
i = 0
while i < 10:
    print(i)
    i += 1

# list comprehension
[i for i in range(10)]

# map
list(map(lambda x: x**2, range(10)))

# filter
list(filter(lambda x: x % 2 == 0, range(10)))

# enumerate
for i, x in enumerate(range(10)):
    print(i, x)

# zip
for i, x in zip(range(10), range(10)):
    print(i, x)

# list comprehension
[i for i in range(10)]
