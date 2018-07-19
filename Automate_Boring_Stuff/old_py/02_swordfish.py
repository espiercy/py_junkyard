#from automate the boring stuff, excercise 2
#epiercy, 5/12/18

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
