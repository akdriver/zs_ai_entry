# 1、统计下面字符出现的次数
# letters = 'abcdabcdabcdabcefg'
# 打印出下面的结构:
# a:4
# b:4
# c:4
# ...

letters = "abcdabcdabcdabcefg"
dic = {}
for letter in letters:
    dic[letter] = dic.get(letter, 0) + 1

for item in dic.items():
    print(f"{item[0]}:{item[1]}")
