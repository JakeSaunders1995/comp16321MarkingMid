import argparse
import os

def parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('input' , type = str, help = "Your input folder path to be processed.")
	parser.add_argument('output' , type = str, help = "The output folder path where the processed data will be stored in.")
	args = parser.parse_args()
	return str(args.input), str(args.output)
def Morse(text):
    plainText = ""
    cipher = {'.-': 'a','-...': 'b','-.-.': 'c','-..': 'd','.': 'e',
    '..-.': 'f','--.': 'g','....': 'h','..': 'i','.---': 'j','-.-': 'k',
    '.-..': 'l','--': 'm','-.': 'n','---': 'o','.--.': 'p','--.-': 'q','.-.': 'r',
    '...': 's','-': 't','..-': 'u','...-': 'v','.--': 'w','-..-': 'x',
    '-.--': 'y','--..': 'z', 
    #Punctionatoion
    '/':" ", '.-.-.-': ".", '..--..':"?",'-.-.--':"!",'--..--':",",'---...':":",
    '_._._.':";",'_...._':"-",".____.":"'",'_.__.':"(",'_.__._':")",'._.._.':""}
    
    text = text.split()
    for word in text:
        plainText+=cipher[word]
    return (plainText)
def Hex(text):
    plainText = ""
    text = text.split()
    for word in text:
        plainText+= chr(int(word,16))
    return(plainText.lower())

def Ceasar(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = ""
    pointer1 , pointer2 = 0 ,0

    while pointer1 < len(text):
        cipherAlpha = text[pointer1]
        if cipherAlpha == " ":
            plainText+= " "
        else:
            while cipherAlpha != alphabet[pointer2]:
                pointer2+=1
            pointer2 = pointer2-3
            if pointer2 < 0:
                pointer2 = len(alphabet)  + pointer2
            plainText+=alphabet[pointer2]

        pointer2 = 0 
        pointer1+=1

    return plainText 

def main():
    inputFolder , outputFolder = parser()
    algorithms = {'Hex':Hex,'Caesar Cipher(+3)':Ceasar,'Morse Code':Morse}
#Open File to Read
    txt_arr = sorted([x for x in os.listdir(inputFolder) if x.endswith(".txt")])
    for inputFile in txt_arr:
        with open (os.path.join(inputFolder,inputFile),'r') as data:
            data = data.read()

        #Split Data
        algorithm , ciphertext = data.split(":")

        #Process
        plainText = algorithms[algorithm](ciphertext)
        #Output
        outputFile = inputFile.split(".")[0]+"_x62165ih.txt"
        outputPath = os.path.join(outputFolder,outputFile)
        with open(outputPath,'w') as out:
            out.write(plainText)
if __name__ == '__main__':
	main()
