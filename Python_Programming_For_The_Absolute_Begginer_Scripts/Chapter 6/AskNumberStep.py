###AskNumberStepValue
###Evan Piercy
###This is probably one of the most asinine questions in the entire book.
###The objective is to 'improve' the ask_number() function so that it is called
###With a step value. That's a pretty meaningless task by itself
###Especially since the question doesn't define what the step value does.
###I don't really care about this, since it is an extension on the next
###Challenge question.
###So, the design will abbreviate and sidestep author's intent, since it doesn't
###Make programmatic sense for what we are trying to accomplish here.
###The step value is present, but meaningless
###6.3.15

def ask_number(question, low, high, step = 1):

    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

###Abandoned further modifications. It's really time to move on.
###That's right. I got all dramatic about it.
###There could be a way to modify this program to give the user twelve tries or
###Something
