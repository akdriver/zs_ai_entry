nums = [10, 20, 30, 50, 70, 20]

first_index_of_20 = -1
index_of_20 = []
for i, k in enumerate(nums):
    if k == 20:
        first_index_of_20 = i
        break

for i, k in enumerate(nums):
    if k == 20:
        index_of_20.append(k)

print("20 首次出现的索引:", first_index_of_20)
print("20 所在的索引下标:", index_of_20)
