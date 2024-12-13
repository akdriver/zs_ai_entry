name_set = {"Hank","Alice"}

print(name_set)

name_set.add("Sunny")
print(name_set)

empty_set = set()

print(empty_set)
empty_set.add("test")
print(empty_set)

# 随机删除一个元素，并返回元素
empty_set.pop()
# 删除指定元素，元素不存在会报错
empty_set.remove("123")
# 删除指定元素，元素不存在不会报错
empty_set.discard("123")