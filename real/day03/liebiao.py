name = ["Alice", "Bob", "Cindy"]
print(name)

name.remove("Alice")
print(name)

name.append("Dog")
print(name)

next_name = ["NEXT"]

name.append(next_name)
print(name)

name.append("Next")
print(name)

name = name + next_name
print(name)

name.insert(0, "First")
print(name)

name.reverse()
print(name)

name.pop(2)
name.sort()
print(name)

name.sort(reverse=True)
print(name)

idx = name.index("Next")
print(idx)

print(name.count("Next"))
