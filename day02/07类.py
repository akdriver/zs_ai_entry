class GirlFriend:
    def __init__(self,name,age):
        # 私有属性
        self.__private = name
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} + {self.age}"

    def hello(self):
        print(f"Hello,My name is {self.name}")

    # 私有方法
    def __hello2(self):
        print("private")


c = GirlFriend("asd",123)
c.hello()
print(c)
