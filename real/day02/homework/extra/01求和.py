# 求1 + 1/2 + 2/3 + 3/4 + 4/5的和

i = 1
ret = 0
while i <= 4:
    ret += i / (i + 1)
    print(f"{i} / {i + 1} = {i / (i + 1)}")
    i += 1
print(ret + 1)
