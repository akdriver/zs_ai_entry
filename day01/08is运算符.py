
name1 = "sunny"
name2 = "sunny"

# 比较的是变量的内存地址是否是同一个
print(name1 is name2)
print(id(name1) == id(name2))

# 比较的是变量的值是否相同
print(name1 == name2)