
dictionary = {'num': 56, 87:'value from key!', 'instructor':'fahad doopeedoop', 'city':'los angeles'}

print(dictionary.get('number', 'This key does not exist'))

for key, value in dictionary.items():
    print(key, value)