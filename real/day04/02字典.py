# 创建空字典
my_dict = {}
print(my_dict)

# 传入指定的映射关系
my_dict = {"hello": "world"}
print(my_dict)

# 使用可列表元组对象创建
my_dict = dict([["hello", "world"], ["How", "Are"]])
print(my_dict)

my_dict = dict([("hello", "world"), ("How", "Are")])
print(my_dict)

# 从指定的key创建
my_dict = dict.fromkeys(range(1, 10))
print(my_dict)
my_dict = dict.fromkeys([1, 2, 3], "default_value")
print(my_dict)

a = [1, 2, 3]
b = [4, 5, 6]
c = zip(a, b)
my_dict = dict(c)
print(my_dict)

# 获取指定key,不存在返回default_value，如果没有指定则返回None
print(my_dict.get("ss"), "default_value")

# 删除指定key，如果不存在返回100
print(my_dict.pop(12, 100))

# LIFO 栈结构，删除最后加入的元素
print(my_dict.popitem())

# 修改元素，如果不存在，就添加,返回None
my_dict.update({"1": 100})
print(my_dict)

# d｜other 合并 两个字典,有相同的 d2 会覆盖d的值
d1 = {"1": 2, "3": 4}
d2 = {"1": 23, "3": 300}
d3 = d1 | d2
# 以下代码等价于 d2 = d2｜d3
d2 |= d3
print("d3", d3)
