#madlibs

#turn keywords into vars
A = 'ADJECTIVE'
V = 'VERB'
N = 'NOUN'

#I'd like to keep the order of replacement intact, so how?
#this is just one line. A file will have mults

mad_lib_file = open('mad_lib.txt') # open file

mad_lib_lines = mad_lib_file.readlines() #read

mad_lib_file.close() #close file

mad_lib_ans = [] #hold the response lines

for line in mad_lib_lines:
    new_line_str = ''
    splits = line.split()
    for word in splits:
        if A in word:
            word = word.replace(A, input('Enter an adjective: ')) #replace word
        elif V in word:
            word = word.replace(V, input('Enter a verb: ')) #replace word
        elif N in word:
            word = word.replace(N, input('Enter a noun: ')) #replace word
        new_line_str += word + ' '
    mad_lib_ans.append(new_line_str)

ans_file = open('ml_ans.txt', 'w')
for line in mad_lib_ans:
    ans_file.write(line)

ans_file.close()
