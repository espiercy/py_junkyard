names = ["Evan", "Kellee", "David", "Thao", "Leslie", "Brett", "Emery", "Ooglethorpe"]

for name in names:
    if len(name) > 5:
        print(len(name))
        print(name.lower().find('n'))
    if "n" in name or "N" in name:
        print(name)

while len(names) > 0:
    print(names[-1])
    names.pop()

print("names all popped!")