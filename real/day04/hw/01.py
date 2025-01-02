"""
列表students中保存了6个学生的信息
students = [
    {'name': 'Tom', 'age': 19, 'score': 92, 'sex': '女', 'tel': '15300022839'},
    {'name': 'Jerry', 'age': 20, 'score': 40, 'sex': '男', 'tel': '15300022838'},
    {'name': 'Andy', 'age': 18, 'score': 85, 'sex': '女', 'tel': '15300022837'},
    {'name': 'Jack', 'age': 16, 'score': 65, 'sex': '男', 'tel': '15300022428'},
    {'name': 'Rose', 'age': 17, 'score': 59, 'sex': '男', 'tel': '15300022653'},
    {'name': 'Bob', 'age': 18, 'score': 78, 'sex': '男', 'tel': '15300022867'}
]

1） 遍历所有的姓名
2） 统计不及格学生的个数
3） 打印所有男生的信息
4） 求平均分数
"""

students = [
    {'name': 'Tom', 'age': 19, 'score': 92, 'sex': '女', 'tel': '15300022839'},
    {'name': 'Jerry', 'age': 20, 'score': 40, 'sex': '男', 'tel': '15300022838'},
    {'name': 'Andy', 'age': 18, 'score': 85, 'sex': '女', 'tel': '15300022837'},
    {'name': 'Jack', 'age': 16, 'score': 65, 'sex': '男', 'tel': '15300022428'},
    {'name': 'Rose', 'age': 17, 'score': 59, 'sex': '男', 'tel': '15300022653'},
    {'name': 'Bob', 'age': 18, 'score': 78, 'sex': '男', 'tel': '15300022867'}
]
# 1） 遍历所有的姓名
for student in students:
    print(student.get("name"))

# 2） 统计不及格学生的个数
failed_count = 0
for student in students:
    if student.get("score") < 60:
        failed_count += 1

# 3） 打印所有男生的信息
for student in students:
    if student.get("sex") == "男":
        print(student)

# 4） 求平均分数
avg_score = sum([student.get("score") for student in students]) / len(students)
print(avg_score)
