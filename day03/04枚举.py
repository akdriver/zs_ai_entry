from enum import Enum,auto


class Color(Enum):
    RED = 1
    YELLOW = 2

print(Color.RED.name)
print(Color.RED.value)
