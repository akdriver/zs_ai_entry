from itertools import count

nums = [
        [255,255,255,255],
        [255,255,255,255],
        [0,255,0,255]
]
count_255 = 0
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if nums[i][j] == 255:
            count_255 +=1
print(count_255)


all_255_rows = []
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if nums[i][j] != 255:
            break
        if nums[i][j] == 255 and j == len(nums[0])-1:
            all_255_rows.append(i)
print(all_255_rows)

for index,value in enumerate(all_255_rows):
    nums.pop(value-index)

print(nums)