import random

# random()：生成 [0.0, 1.0) 范围内的随机浮点数。
r1 = random.random()
print(r1)

# uniform(a, b)：生成 [a, b] 范围内的随机浮点数。
r2 = random.uniform(1.0,2.0)
print(r2)

# randint(a, b)：生成 [a, b] 范围内的随机整数（包含两端）。
print(random.randint(1,2))

# 输出 0 到 10 的偶数
print(random.randrange(0, 10, 2))


colors = ["Red","Blue","Yellow"]
# 从列表中随机选一个
print(random.choice(colors))

# 从列表中随机选2个, 可重复
print(random.choices(colors,k=2))

# 从列表中随机选2个, 不重复
print(random.sample(colors, 2))

# 打乱顺序
random.shuffle(colors)
print(colors)


random.seed(42)  # 固定种子
print(random.random())  # 每次运行都输出相同的随机数