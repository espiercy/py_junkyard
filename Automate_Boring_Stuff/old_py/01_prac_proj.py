#The Collatz Sequence
#epiercy 5/14/18
#this seems like a better construction to me
#clearly operating on the number that came in
#one print, one return
#otherwise we're cluttering things

def collatz(number):
    try:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        #print(number) <--not necessary
        return number
    except:
        print('That wasn\'t a number, dummy')
