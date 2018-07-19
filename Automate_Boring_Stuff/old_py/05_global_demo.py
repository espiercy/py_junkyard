#global demo, automate boring stuff
#epiercy 5/14/18
#this is probably never a good thing to actually do...btw

def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon' # this is a local
    print(eggs, 'is the value of eggs from ham()')

def ham():
    print(eggs, 'is the global value, printed from ham()')
    
spam()
bacon()
ham()

eggs = 42
print(eggs, 'is the value of eggs, after updated and printed directly')
