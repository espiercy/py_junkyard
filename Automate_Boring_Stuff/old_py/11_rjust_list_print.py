#rjust(len) will right justify a word

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

rowLengths = []

#find longest string in each column ? The book is clunky, but I'll use it
for list in tableData:
    space = 0
    for item in list:
        if len(item) > space:
            space = len(item)
    rowLengths.append(space)

#now, print list
for list in tableData:
    printStr = ''
    for item in list:
        printStr += item.rjust(max(rowLengths)) + ' '
    print(printStr)
