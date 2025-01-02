list01 = [1, 2, 3, 4, 5, 6]

s = {x for x in list01}
print(type(s))

d = {x: x ** 2 for x in list01}
print(type(d))

for item in d.items():
    print(item)
