
name  = input("Please input your name:")
age  = input("How old are you:")
addr  = input("Where do you live:")
tel  = input("Your tel:")

case = f"""
{"*"*30},{12+32}
Hi, My name is {name},
{age} years old,
live in {addr},
you can contact me via my tel {tel}
{"*"*30}
"""

print(case)