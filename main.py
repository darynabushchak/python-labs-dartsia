from chair import Chair

chairs = [
    Chair(),
    Chair("plastic", 120, "bilka", 9),
    Chair.get_instance(),
    Chair.get_instance(),
]

for chair in chairs:
    print(chair.__str__())
