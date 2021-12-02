import sys, os
inputfilename = str(sys.argv[1])
print()
file = open(inputfilename,"r")
dict = file.read().splitlines()
file.close()

inputfoldername = str(sys.argv[2])
files = os.listdir(inputfoldername)
for filename in files:
    file = open("./"+inputfoldername+"/"+filename,"r")
    text = file.read()
    file.close()

    outputfoldername = str(sys.argv[3])
    file = open("./"+outputfoldername+"/"+filename[0:len(filename)-4]+'_n62189sd.txt',"w")
    file.truncate(0)
    file.write('n62189sd'+"\n")

    file.write('Formatting ###################'+"\n")
    print(text)
    letters = list(text)
    c=0
    letters2 = []
    while c<len(letters):
        if "".join(letters[c:c+5]) == ". . .":
            letters2.append("...")
            c=c+5
        elif "".join(letters[c:c+3]) == "...":
            letters2.append("...")
            c=c+3
        else:
            letters2.append(letters[c])
            c=c+1
    letters = letters2
    print(letters)

    c = 0
    uppercase = 0
    chk = {"A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    while c<len(letters):
        if letters[c] in chk:
            letters[c]=(str(letters[c])).lower()
            uppercase = uppercase+1
        c=c+1
    file.write('Number of upper case letters changed: '+str(uppercase)+"\n")

    c = 0
    punctuation=0
    chk = [".","?",'!',',',':',';','–','-','(',')','[',']','{','}',"\'",'\"','...',"…"]
    letters2 = []
    while c<len(letters):
        if letters[c] in chk:
            punctuation = punctuation+1
            letters2.append(" ")
        else:
            letters2.append(letters[c])
        c=c+1
    letters = letters2
    file.write('Number of punctuations removed: '+str(punctuation)+"\n")

    c = 0
    numbers=0
    chk = ["0","1",'2','3','4','5','6','7','8','9']
    letters2 = []
    while c<len(letters):
        if letters[c] in chk:
            numbers = numbers+1
        else:
            letters2.append(letters[c])
        c=c+1
    letters = letters2
    file.write('Number of numbers removed: '+str(numbers)+"\n")

    file.write('Spellchecking ###################'+"\n")
    text2 = []
    newlines = 0
    makingwords = ""
    for item in letters:
        if item == '\n':
            text2.append(item)
            newlines = newlines+1
            makingwords = ""
        elif item == ' ':
            text2.append(makingwords)
            makingwords = ''
        else:
            makingwords=makingwords+item
    text2.append(makingwords)



    allwords = 0
    rightwords = 0
    text3 = []
    for item in text2:
        if item != '\n' and item != '':
            allwords = allwords+1
            if item in dict:
                rightwords = rightwords+1
                text3.append(item)
    file.write('Number of words: '+str(allwords)+"\n")
    file.write('Number of correct words: '+str(rightwords)+"\n")
    file.write('Number of incorrect words: '+str(allwords-rightwords)+"\n")
    text3 = " ".join(text3)
    print(text3)
    file.close()
    print()
