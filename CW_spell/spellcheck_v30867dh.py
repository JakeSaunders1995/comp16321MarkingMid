import sys
import os
def spell(a, b1):
    d = open(b1)
    b = k.read()
    a = a + " "
    punctuation = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
    pun = 0 #punctuations
    num = 0 #numbers
    u = 0 #upper
    no_punctuation = ""
    for char in a:
        if char not in punctuation:
            no_punctuation = no_punctuation + char
        else:
            pun = pun + 1

    a = no_punctuation
    no_number = ""
    for char in a:
        if char.isalpha() or char == " ":
            no_number = no_number + char
        else:
            num = num + 1
    w = 0 #words
    cow = 0 #correct words
    inw = 0 #incorrect words
    a = no_number
    no_upper = ""
    for char in a:
        if char.isupper() or char == " ":
            no_upper = no_upper + char.lower()
            if char.isupper():
                u = u + 1
        else:
           no_upper = no_upper + char
    format = no_upper
    word = ""
    
    lines = []
    with open(b1) as b:
        lines = [line.strip() for line in b]
    word = ""
    for char in format:
        if char != " ":
            word = word + char
        else:
            w = w + 1
            if word in lines:
                cow = cow + 1
            else :
                inw = inw + 1
            word = ""


    output = str(sys.argv[3]) + "/" + str("output")
    o = open(output , "w") #output file
    o.write("m03777am\n")
    o.write("Formatting ###################\n")
    o.write("Number of upper case words transformed: "+ str(u)  +"\n")
    o.write("Number of punctuation’s removed: "+ str(pun) +"\n")
    o.write("Number of numbers removed: "+ str(num) +"\n")
    o.write("Spellchecking ###################\n")
    o.write("Number of words in file: "+ str(w) +"\n")
    o.write("Number of correct words in file: "+ str(cow) + "\n")
    o.write("Number of incorrect words in file: "+ str(inw) + "\n")

def main():
    y = sys.argv[1]
    z = sys.argv[2]
    filesy = os.listdir(y)
    filesz = os.listdir(z)
    a1 = ""
    for x in filesy:
        str(x)
        if str(x) == "EnglishWords.txt":
            z1 = str(y) + "/" + str(x) 
            a1 = z1
            break
    b1 = ""
    for i in filesz:
        z1 = str(z) + "/" + str(i)
        if z1[-3:] == "txt":
            g = open(z1)
            b1 = g.read()
            spell(b1,a1)
    

if __name__ == "__main__":
    main()
