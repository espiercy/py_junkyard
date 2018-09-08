people = [
    {
        "name": "Evan",
        "age": 36,
        "hobbies": ["reading", "writing", "hiking", "python"]
    },
    {
        "name": "Kellee",
        "age": 39,
        "hobbies": ["hiking", "biking", "badminton"]
    },
    {
        "name": "Izzie",
        "age": 17,
        "hobbies": ["purring", "eating", "sleeping"]
    },
    {
        "name": "David",
        "age": 65,
        "hobbies": ["hiking", "striking", "poetry"]
    },
]

print(people)
print('Names of people: ')
names = [person["name"] for person in people]
print(names)
print('Is everyone on list older than 20?')
twenty_plus = all([person["age"] > 20 for person in people])
print(twenty_plus)

new_people = [person.copy() for person in people]
new_people[0]["name"] = "Bofo"

print("Old list names: ")
print([person["name"] for person in people])
print("New list names: ")
print([person["name"] for person in new_people])

person_1, person_2, person_3, person_4 = people
print(person_1)
print(person_2)
print(person_3)
print(person_4)