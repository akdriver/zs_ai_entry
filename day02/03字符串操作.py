
info = "Hello"

print(info[0])

for i in range(len(info)):
    print(info[i])

for s in info:
    print(s)

# 是否是空字符串
print(info.isspace())

# 去除首尾的空格
info = "  HeLLo  "
info = info.strip()
print(info)

# 去除右边的空格
info = "  HeLLo  "
info = info.rstrip()
print(info)

# 去除左边的空格
info = "  HeLLo  "
info = info.lstrip()
print(info)

info = "Hello@World@你好@世界"
splits = info.split("@")
print(splits)

rsplits = info.rsplit("@",1)
print(rsplits)

info = "Hello"
info = info.upper()
print(info)

info = info.lower()
print(info)

print(info.startswith("hel"))
print(info.endswith("o"))

info = "My name is {},Age:{}".format("Hank","24")
print(info)

info = "My name is {0},Age:{1}".format("Hank","24")
print(info)

info = "My name is {name},Age:{age}".format(name= "Hank",age= "24")

print(info)

# 字符串连接

names = ["Hanks","Alice","Jack"]

join_name = "-".join(names)
print(join_name)

info = "加QQ，提供上门服务，上门服务"

info = info.replace("上门服务","***")
print(info)

info = "123456"
print(info.isdigit()) 