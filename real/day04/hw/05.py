# 3、统计学校school中两个教室的学生表情, 描述如下:
grade_01 = [{"happy": 10}, {"dispirited": 2}]
grade_02 = [{"happy": 11, "exciting": 12}, {"dispirited": 5}]
school = [grade_01, grade_02]
dic = {}

# for s in school:
#     for item in s:
#         for key in item.keys():
#             if key in dic:
#                 k_count = dic.get(key)
#                 dic.update({key: k_count + item.get(key)})
#             else:
#                 dic.update({key: item.get(key)})
#
# print(dic)

# 遍历统计
for s in school:
    for item in s:
        for key, value in item.items():
            dic[key] = dic.get(key, 0) + value
