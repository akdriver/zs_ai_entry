
class Animal:
    count = 0
    def __init__(self,name):
        self.name = name
        Animal.count+=1
    @classmethod
    def test(cls):
        print(cls)
    @staticmethod
    def test_static(msg):
        print(msg)

a1 = Animal("a1")
a2 = Animal("a2")
print(Animal.count)
Animal.test()
Animal.test_static("123")