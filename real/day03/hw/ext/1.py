# 1. 随机分配商品
# 需求:有三个店铺，6个商品，6个商品随机分配到3个店铺
import random

all_shop = [[] for _ in range(3)]
items = [1, 2, 3, 4, 5, 6]

random.shuffle(items)
for idx, value in enumerate(items):
    all_shop[idx % 3].append(value)
    
print(all_shop)
