
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} is making a {self.sound} sound")

    @staticmethod
    def sleep():
        print("Animal is Sleeping")

class Cat(Animal):
    def __init__(self, name, breed, color, sound):
        super().__init__(name, sound)
        self.breed = breed
        self.color = color
    # 重写父类方法
    def make_sound(self):
        print(f"cat:{self.name} with color:{self.color} is making a sound:{self.sound} ")
    def show_info(self):
        print(f"Cat Name:{self.name},Cat Color:{self.color},Cat Breed:{self.breed}")

cat = Cat("shelly","caffe","yellow",sound="meow")
cat.make_sound()


class Friend:
    def __init__(self,hobby):
        self.hobby = hobby
    def hobby_info(self):
        print(f"Friend's hobby is {self.hobby}")


class HoneyFriend(Friend):
    def __init__(self,hobby,name):
        super().__init__(hobby)
        self.name = name
    def hobby_info(self):
        super().hobby_info()
        print("honey Friend Hobby")





