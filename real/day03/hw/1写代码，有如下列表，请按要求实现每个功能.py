li = ['zoran', 'ethan', 'jim']
# a.计算列表长度并输出
print(f"列表长度:{len(li)}")

# b.列表中追加元素 “lucy”，并输出添加后的列表
li.append("lucy")
print(li)

# c.请在列表的第 1 个位置插入元素 “Tony”，并输出添加后的列表
li.insert(0, "Tony")
print(li)

# d.请修改列表第 2 个位置的元素为 “Kelly”，并输出修改后的列表
li[1] = "Kelly"
print(li)

# e.请删除列表中的元素 “ethan”，并输出修改后的列表
li.remove("ethan")
print(li)

# f.请删除列表中的第 2 个元素，并输出删除元素后的列表
li.pop(1)
print(li)
