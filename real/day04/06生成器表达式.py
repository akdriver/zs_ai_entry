list01 = [1, 2, 3, 4, 5, 6]

g1 = (x for x in list01)

# 生成的是迭代器对象
print(type(g1))
print(g1)

# 配合next方法使用迭代器对象 只能迭代一次 如果迭代完了，第二次迭代g1，不会迭代出任何对象，因为迭代器已经指向末尾
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))

# 第二次迭代 不会打印任何值
for v in g1:
    print(g1)
