a = True
b = False
c = True
# False
print(a and b)

# True
print(a or b)

# False
print(not c)


# 短路 ,因为12 >32 不成立， 所以结果为False，and 后面的代码不会执行
print(12 > 32 and "123")

# or短路，前面已经为True，or 后面的代码不会执行
print(32 > 12 or "123")



i = 10
j = 20
# 逻辑运算符会返回最后一个表达式的值，这里返回j的值，所以k =20
k = i and j
print(k)
# k = 10
k = i or j
print(k)
