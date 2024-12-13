
for i in range(5):
    print("hello")

mylist = [1,2,3,4,5]
for i in range(len(mylist)):
    print(mylist[i])

count = 0
# 当count == 11的时候，会执行else 里面的代码，所以最后的count == 12
while count <= 10:
    count+=1
else:
    count+=1
print(count)

count2 = 0
# 当break 时，不会执行else里面的代码，以下代码输出6
while count2 <= 10:
    count2+=1
    if count2 > 5 :
        break
else:
    count2+=1
print(count2)