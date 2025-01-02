def recur(temp):
    if len(temp) == 3:
        ret.append(temp)
        return
    for i in range(1, 5):
        if str(i) in temp:
            continue
        temp += str(i)
        recur(temp)
        temp = temp[:-1]


ret = []
recur("")
print(ret)
