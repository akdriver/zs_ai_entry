import os.path

with open("test.txt","a") as first_file:
    first_file.write("123\n")

# 读取整个文件的内容
with open("test.txt","r") as file:
    content = file.read()
    print(content)

# 按行读取文件
with open("test.txt","r") as file2:
    for line in file2:
        print(line)

# 按行读取文件
if os.path.exists("test.txt"):
    with open("test.txt","r") as rfile:
        while rfile.readline():
            print(line)