#Triva Challenge Text
#Trivia Game that reads a plain text file
#This file is similar to the previous one, except a different, python-based quiz is used
#Evan Piercy
#6.3.15

import sys

py_high_scores = open("phs.txt", "w")

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("Press the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)
    score = next_line(the_file)

    return category, question, answers, correct, explanation, score

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

def main():
    trivia_file = open_file("py_trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score_tot = 0
    #get first block
    category, question, answers, correct, explanation, score = next_block(trivia_file)
    while category:
        #ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i+1, "-", answers[i])
        #get answer
        answer = input("What's your answer? ")
        #check answer
        if answer == correct:
            print("\nRight! This answer is worth ", score , " points.", end=" ")
            score_tot += int(score)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score_tot, "\n\n")
        #get next block
        category, question, answers, correct, explanation, score = next_block(trivia_file)

    trivia_file.close()
    print("That was the last question!")
    print("Your final score is", score_tot)
    if(score_tot > 4):
        print("Congratulations! This score is high enough to make the high score list!")
        name = input("Enter your name: ")
        high_score = name + " " + str(score_tot)
        py_high_scores.write(high_score)
        py_high_scores.close()

main()
input("\n\nPress the enter key to exit.")
