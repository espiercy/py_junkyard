
dictionary = {'num': 56, 87:'value from key!', 'instructor':'fahad doopeedoop'}

print(dictionary['num'])
print(dictionary[87])

dictionary['new'] = 1234567

print(dictionary)

del dictionary['instructor']

print(dictionary)

#del dictionary

#dictionary.clear()

#print(dictionary)

print(len(dictionary))

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

emptDictionary = {}

emptDictionary = dictionary
print(emptDictionary)

testDict={'city':'los angeles'}

testDict.update(emptDictionary)
print(testDict)