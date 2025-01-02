list01 = [1, 2, 3, 4, 5, 6]
# 将list01 加1 得到list02

list02 = [x + 1 for x in list01]
print(list02)

# 将list01 中的偶数存储成一个新的元素
list03 = [x for x in list01 if x & 1 == 0]
print(list03)

# 双重循环
list04 = [(x, y) for x in list01 for y in list01]
print(list04)
