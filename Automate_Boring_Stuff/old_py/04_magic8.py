#from automate the boring stuff
#I liked this function ex
#epiercy 5/13/18

import random

def get_answer(ans_num):
    if ans_num == 1:
        return 'It is certain'
    elif ans_num == 2:
        return 'It is decidedly so'
    elif ans_num == 3:
        return 'It is decidedly so'
    elif ans_num == 4:
        return 'Reply hazy try again'
    elif ans_num == 5:
        return 'Ask again later'
    elif ans_num == 6:
        return 'Concentrate and ask again'
    elif ans_num == 7:
        return 'My reply is no'
    elif ans_num == 8:
        return 'Outlook not so good'
    elif ans_num == 9:
        return 'Very doubtful'

r = random.randint(1,9) #look how sloppy this book is! r can't be 9 like this
fortune = get_answer(r)
print(fortune)
