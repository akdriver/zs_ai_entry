# 对于输入的四位数1234，返回翻转后的结果4321。
from typing import List

from numpy.ma.core import negative

x = 1234
ret = 0
while x != 0:
    tail_num = x % 10
    ret = ret * 10 + tail_num
    x //= 10

print(ret)
#
#
# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     dic = {}
#     for v in strs:
#         t = "".join(sorted(v))
#         if t in dic:
#             dic[t].append(v)
#         else:
#             dic[t] = [v]
#     print(dic.values().)
#
#
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# groupAnagrams(strs=strs)
