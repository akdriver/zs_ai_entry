class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Animal info{self.name}")

class Cat(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)

    def info(self):
        print(f"cat info{self.name}")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def info(self):
        print(f"dog info{self.name}")

# Python 多态实现 就是靠函数实现
def multi_info(animal:Animal):
    animal.info()

cat = Cat("wow",123)
dog = Dog("wow",123)

multi_info(cat)
multi_info(dog)