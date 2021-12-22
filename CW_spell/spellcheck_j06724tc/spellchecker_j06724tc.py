import sys, os
a = sys.argv[1]
b = sys.argv[2]
c = os.listdir(b)
for d in c:
    e = b + "/" + d
    with open(a, 'r') as words:
        words=words.readlines()
        x = 0
        while x < len(words):
            words[x] = words[x].replace("\n","")
            x += 1

    with open(e, 'r') as spellchecker:
        spellchecker = spellchecker.read()
        y = 0
        z = 0
        uppercasechanged = 0
        punctuationsrem = 0
        numrem = 0
        word = ""
        numwords = 0
        incorrectwords = 0
        punctuation = ".?!,:;-—–()[]{}\'\"…"
        number = "1234567890"
        capalphabet = {'A': 'a', 'B': 'b', 'C': 'c',
                      'D': 'd', 'E': 'e', 'F': 'f',
                      'G': 'g', 'H': 'h', 'I': 'i',
                      'J': 'j', 'K': 'k', 'L': 'l',
                      'M': 'm', 'N': 'n', 'O': 'o',
                      'P': 'p', 'Q': 'q', 'R': 'r',
                      'S': 's', 'T': 't', 'U': 'u',
                      'V': 'v', 'W': 'w', 'X': 'x',
                      'Y': 'y', 'Z': 'z'
                      }
        while y < len(spellchecker):
            if spellchecker[y] in punctuation:
                punctuationsrem += 1
                spellchecker = spellchecker.replace(spellchecker[y],"")
                y += 1
            elif spellchecker[y] in number:
                numrem += 1
                spellchecker = spellchecker.replace(spellchecker[y],"")
                y += 1
            elif spellchecker[y] in capalphabet:
                uppercasechanged += 1
                spellchecker = spellchecker.replace(spellchecker[y],capalphabet[spellchecker[y]])
                y += 1
            else:
                y += 1
        while z < len(spellchecker):
            if spellchecker[z] == " ":
                if word == " ":
                    z += 1
                else:
                    if word not in words:
                        numwords += 1
                        incorrectwords += 1
                        word = ""
                        z += 1
                    else:
                        numwords += 1
                        word = ""
                        z += 1
            else:
                word = word + spellchecker[z]
                z += 1
        if word not in words:
            numwords += 1
            incorrectwords += 1
            word = ""
        else:
            numwords += 1
            word = ""

    output = "j06724tc \nFormatting ################### \nNumber of upper case letters changed:" + str(uppercasechanged) + "\nNumber of punctuations removed: " + str(punctuationsrem) + "\nNumber of numbers removed: " + str(numrem) + "\nSpellchecking ################### \nNumber of words: " + str(numwords) + "\nNumber of correct words: " + str(numwords - incorrectwords) + "\nNumber of incorrect words: " + str(incorrectwords)
    f = d.replace('.txt','')
    g = sys.argv[3] + "/" + f + "_j06724tc" + ".txt"
    h = open(g, 'w')
    h.write(output)
