from day01.地址 import name1

dic = {
    "name":"Hank",
    "age" :18
}
print(dic)

# 添加一个元素，如果不存在height 就添加，存在就修改
dic["height"] = 185
# 如果key存在 返回对应值
dic.setdefault("height",185)
print(dic)

# 删除height
del dic["height"]
# 同上
# dic.pop("height")
print(dic)


# 判断key是否存在

if "name" in dic:
    # key 不存在会报错
    print(dic["name"])
    # key 不存在会返回None
    print(dic.get("name"))
else:
    dic["name"] = "Hank"

# 遍历所有keys
for key in dic.keys():
    print(key)

# 遍历所有values
for value in dic.values():
    print(value)

# 遍历所有item
for item in dic.items():
    print(item)