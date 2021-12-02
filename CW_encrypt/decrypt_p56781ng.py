alphabet = [
    ['a','.-'],['b','-...'],['c','-.-.'],['d','-..'],       #0-3x
    ['e','.'],['f','..-.'],['g','--.'],['h','....'],        #4-7
    ['i','..'],['j','.---'],['k','-.-'],['l','.-..'],       #8-11
    ['m','--'],['n','-.'],['o','---'],['p','.--.'],         #12-15
    ['q','--.-'],['r','.-.'],['s','...'],['t','-'],         #16-19
    ['u','..-'],['v','...-'],['w','.--'],['x','-..-'],      #20-23
    ['y','-.--'],['z','--..'],['0','-----'],['1','.----'],  #24-27
    ['2','..---'],['3','...--'],['4','....-'],['5','.....'],#28-31
    ['6','-....'],['7','--...'],['8','---..'],['9','----.'],#32-35
    ['.','.-.-.-'],['?','..--..'],['!','-.-.--'],[',','--..--'],#36-39
    [':','---...'],[';','-.-.-.'],['--',''],['-','-...-'],         #40-43
    ['[',''],[']',''],['{',''],['}',''],[' ','/'],                                 #44-48
    ['(','-.--.'],[')','-.--.-'],["'",'.----.'],['"','.-..-.'],['...','']#49-53
]
caesar = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
import argparse, os, os.path, re
parser = argparse.ArgumentParser()
parser.add_argument("inputfolder")
parser.add_argument("outputfolder")
args = parser.parse_args()
infile = args.inputfolder
pathlist = os.listdir(infile)
for file in pathlist:
    filepath = os.path.join(infile, file)
    f=open(filepath, 'r')
    str = f.read()
    algorithm = re.split(r':', str)
    answer=""
    if algorithm[0] == "Morse Code":   #[][1]
        sentence = algorithm[1]
        words = re.split(r' ', sentence)
        for w in range(0,len(words)):
            for x in range (0,len(alphabet)):
                if words[w] == alphabet[x][1]:
                    answer += alphabet[x][0]
    if algorithm[0] == "Caesar Cipher(+3)":
        sentence2 = algorithm[1]
        for t in range(0, len(sentence2)):
            if sentence2[t] == " ":
                answer += " "
            else:
                for y in range(0, len(caesar)):
                    if sentence2[t] == caesar[y]:
                        answer += caesar[y-3]
                #ASCIIValue = ord(sentence2[t])
                #ASCIIValue -= 3
                #answer += chr(ASCIIValue)
    if algorithm[0] == "Hex":
        sentence3 = algorithm[1]
        words3 = re.split(r' ', sentence3)
        for a in range(0,len(words3)):
            answer += chr(int(words3[a],16))
    f.close() 
    name, ext = os.path.splitext(file)
    name += "_p56781ng" + ext
    output = os.path.join(args.outputfolder, name)
    plaintext = open(output, 'w')
    plaintext.write(answer)
    plaintext.close()

                




