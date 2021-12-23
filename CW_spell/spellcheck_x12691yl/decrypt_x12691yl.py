import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()
input_folder, output_folder = args.input_folder, args.output_folder
input_folder = os.getcwd()+input_folder[1:] if input_folder[0] == '.' else input_folder
output_folder = os.getcwd()+output_folder[1:] if output_folder[0] == '.' else output_folder

def encryption(data):
    morse_dictionary = {'/': ' ', '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '.-.-.-': '.', '---...': ':', '--..--': ',', '-.-.-.': ';', '..--..': '?', '-...-': '=', '.----.': "'", '-..-.': '/', '-.-.--': '!', '-....-': '-', '..--.-': '_', '.-..-.': '"', '-.--.': '(', '-.--.-': ')', '...-..-': '$', '.-...': '&', '.--.-.': '@', '.-.-.': '+'}

    caesar = lambda cipher: "".join((' ' if i == ' ' else chr(ord(i)-3) if ord(i)>99 else chr(ord(i)+23) for i in cipher))
    morse = lambda cipher: "".join((morse_dictionary[i] for i in cipher.split()))
    hexa = lambda cipher: "".join((chr(int(i, 16)) for i in cipher.split()))

    method, cipher = data.strip().split(":")
    return hexa(cipher) if method == "Hex" else morse(cipher) if method == "Morse Code" else caesar(cipher)


for file in filter(lambda x: x.endswith(".txt"), os.listdir(args.input_folder)):

    output = encryption(open(f'{args.input_folder}/{file}', "r").read().strip())
    file = file.replace('.txt', '')
    w = open(f'{args.output_folder}/{file}_x12691yl.txt', "w")
    w.write(output)
    w.close()
