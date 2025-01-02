i = 1
ret = 0
while i < 100:
    if i % 3 == 0 and i % 5 == 0:
        ret += i
    i += 1
print(ret)
