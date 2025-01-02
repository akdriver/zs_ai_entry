nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
dic = {}
result = []

for i, num in enumerate(nums):
    complement = target - num
    if complement in dic:
        result.append((complement, num))
    dic[num] = i

print(result)
