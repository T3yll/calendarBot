def makeBetter():
    fileM = open('final.txt', 'w',)
    for line in open('test.txt', 'r'):
        fileM.write(line + '\n')