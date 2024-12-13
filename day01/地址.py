
# 相同字符串的地址值是一样的
name1 = "qiuqiu"
name2 = "qiuqiu"
name3 = "qiuqiu"

print(id(name1))
print(id(name2))
print(id(name3))

# 相同数字的地址值是一样的
age1 = 12
age2 = 12

print(id(age1))
print(id(age2))

# 释放内存空间
del age1
# 释放内存空间后的变量 再次使用会报错
# print(age1)