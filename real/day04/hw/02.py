"""
名片管理 系统 录入三张名片即可
名片盒子 列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?
cards = [
{“name”:”张三”,”tel”:”13812345678”,”job”:”CEO”,”addr”:”四川”}, # 字典
{名片信息2},{名片信息3}
]
需要完成的功能 就是对 名片盒子 进行增删改查
1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面 cards.append(一个人的名片字
典)
2. 显示所有名片: 遍历名片盒子输出名片信息
3. 修改名片: 录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,如果找到 , 重写录入新的名片信息, 完成修改操作
4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""

# 1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面 cards.append(一个人的名片字典)
cards = []
for _ in range(3):
    name = input("Input name:")
    tel = input("Input tel:")
    job = input("Input job:")
    addr = input("Input addr:")
    card = {"name": name, "tel": tel, "job": job, "addr": addr}
    cards.append(card)

# 2. 显示所有名片: 遍历名片盒子输出名片信息
for card in cards:
    for k, v in card.items():
        print(k, v)

# 3. 修改名片: 录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,如果找到 , 重写录入新的名片信息, 完成修改操作
card_name_to_be_updated = input("what is the card name you want to updated:")
for card in cards:
    if card.get("name") == card_name_to_be_updated:
        name = input("Input new name:")
        tel = input("Input new tel:")
        job = input("Input new job:")
        addr = input("Input new addr:")
        card.update({"name": name, "tel": tel, "job": job, "addr": addr})

# 4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
card_name_to_be_deleted = input("what is the card name you want to deleted:")
idx_to_be_deleted = -1
for idx, card in enumerate(cards):
    if card.get("name") == card_name_to_be_deleted:
        idx_to_be_deleted = idx
        break
if idx_to_be_deleted != -1:
    del cards[idx_to_be_deleted]
