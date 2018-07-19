import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

def get_fortune():
    print(messages[random.randint(0, len(messages) - 1)])

#decided to enclose it in a function. I also call it down below

get_fortune()
