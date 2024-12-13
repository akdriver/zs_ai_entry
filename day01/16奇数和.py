x = 0
for i in range(101):
    if i%2 == 0:
        continue
    print(i)
    x += i
print(x)