
a = ["1", "123"]
print(a)

# 在末尾添加一个元素
a.append("nihao")

# 在指定下标添加一个元素
a.insert(0,"2")


print(a)
# 访问指定下标的元素
print(a[0])

# 删除指定元素，如果有多个 默认删除第一个
a.remove("nihao")
print(a)

# 默认删除最后一个元素
a.pop()
print(a)

# 删除指定下标元素
a.pop(0)
print(a)

# del 同pop
del a[0]
print(a)

a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
print(a)

# 将元素排序
a.sort(reverse=True)
print(a)

# 反转列表
a.reverse()
print(a)

# 获取最后一个元素
print(a[-1])

# 切片
print(a[0:1:2])
print(a[::-1])

# 获取元素第一次出现的索引
print(a.index(1))

# 获取元素出现的次数
print(a.count(1))

# 把元素b 添加到a
b = [5,6,7]
a.extend(b)

print(a)

mylist = [1,2,3,4,5,6]
# 列表推导
mylist = [x*x for x in mylist if x >3]
print(mylist)
