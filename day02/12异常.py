

try:
    a = 123
    # a = int("abc")
    # result = 10/0
except ZeroDivisionError as e:
    print("Exception happened:",e)
except ValueError as ve:
    print(ve)
else:
    print("no error")
finally:
    print("finally end")


class CustomException(Exception):
    pass

try:
    raise CustomException("Custom Exception")
except CustomException as ce:
    print(ce)