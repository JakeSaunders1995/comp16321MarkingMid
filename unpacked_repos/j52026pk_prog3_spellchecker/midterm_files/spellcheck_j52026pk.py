import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('words')
parser.add_argument('originalfile')
parser.add_argument('spellcheckedfile')
args = parser.parse_args()

openf=os.listdir(args.originalfile)
printf= os.listdir(args.spellcheckedfile)
sCounter=0
while sCounter<len(openf):
    text = ""
    file = args.originalfile+"/"+openf[sCounter]
    giventext = open(file,"r")

    while True:
        x=giventext.read(1)
        if not x:
            break
        text += x

    giventext.close()

    numbers=0
    punctuation=0
    upper=0
    character1=0
    character2=0
    word=0
    nwords=0
    incorrect=0
    textnew = ""
    wordtext=""
    ellipsis="..."

    if ellipsis in text:
    	el=text.count(ellipsis)
    	punctuation-=(2*el)

    i=0
    while i <len(text):
        ascii = ord(text[i])
        wrongchr = False
        while wrongchr==False:
            if (ascii <=64 and ascii >=33) or (ascii <= 96 and ascii >= 91) or (ascii >= 123):
                if ascii>=48 and ascii<=57:
                    numbers+=1
                elif (ascii==33 or ascii==34) or (ascii>=39 and ascii<=41) or (ascii>=43 and ascii<=47) or (ascii==58 or ascii==59 or ascii==63) or (ascii>=91 and ascii<=93) or (ascii==123 or ascii==125):
                    punctuation +=1
                wrongchr = True
            else:
                if (ascii>=65 and ascii<=90):
                    upper+=1
                textnew += text[i].lower()
                wrongchr = True
        i+=1

    while character2<(len(textnew)-1):
        character2+=1
        found=False
        ch=0
        while found == False:
            if textnew[character1+ch] == " ":
                ch+=1
            else:
                found = True
                character1+=ch
                character2+=ch
        if textnew[character2]== " ":
            nwords+=1
            wordtext = textnew[character1:character2]
            character1=character2+1
            englishwordstxt = open(args.words,"r")
            while found == True:
                word = englishwordstxt.readline()
                if not word:
                    incorrect +=1
                    found = False
                word = word[0:len(word)-1]
                if wordtext == word:
                    found= False
            englishwordstxt.close()
    nwords += 1

    englishwordstxt = open(args.words,"r")
    while found==False:
        word = englishwordstxt.readline()
        wordtext = textnew[character2:len(textnew)]
        if not word:
            incorrect +=1
            found=True
        word = word[0:(len(word)-1)]

        if wordtext ==word:
            found = True

    englishwordstxt.close()
    correct = nwords - incorrect

    filename = openf[sCounter]
    newfilename = filename[0:len(filename) - 4] + "_j52026pk.txt"

    printf=open(newfilename, "w")
    printf.write(f"j52026pk\n")
    printf.write(f"Formatting ################### \n")
    printf.write(f"Number of upper case letters changed: {upper} \n")
    printf.write(f"Number of punctuations removed: {punctuation} \n")
    printf.write(f"Number of numbers removed: {numbers} \n")
    printf.write(f"Spellchecking ################### \n")
    printf.write(f"Number of words: {nwords} \n")
    printf.write(f"Number of correct words: {correct} \n")
    printf.write(f"Number of incorrect words: {incorrect} \n")
    printf.close()
    sCounter+=1
