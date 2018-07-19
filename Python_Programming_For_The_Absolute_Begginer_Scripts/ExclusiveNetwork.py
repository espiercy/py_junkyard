#Exclusive Network
#Demonstrates logical operators and compound conditions
#Evan Piercy
#3.18.15

print("\tExclusive Computer Network")
print("\t\tMembers only!")

security = 0

username = ""
while not username:
    username = input("Username: ")

password = ""

while not password:
    password = input("Password: ")

if username == "M.Dawson" and password == "secret":
    print("Hi, Mike.")
    security = 5

if username == "S.Meier" and password == "civilization":
    print("Hey, Sid.")
    security = 3

if username == "S.Miyamoto" and password == "mariobros":
    print("What's up, Shiguru?")
    security = 3

if username == "W.Wright" and password == "theisms":
    print("How goes it, Will?")
    security = 3

if username == "guest" or password == "guest":
    print("Welcome, guest.")
    security = 1

print("\n\nPress the enter key to exit.")
