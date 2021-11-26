import argparse,os

parser = argparse.ArgumentParser()
parser.add_argument('input_directory')
parser.add_argument('output_directory')
args = parser.parse_args()

input_directory = args.input_directory
output_directory = args.output_directory

i = 1
for filename in os.scandir(input_directory):
    if filename.is_file():
        f = open(filename.path)
        text = f.read()

        encryption = ""
        for char in text:
            if char != ":":
                encryption += char
            else:
                ind = text.index(char) + 1
                text = text[ind:]
                break

        answer = ""

        if encryption == 'Hex':
            answer = bytes.fromhex(text).decode('utf-8')

        elif encryption == 'Caesar Cipher(+3)':
            for code in text:
                if code == " ":
                    answer += code
                else:
                    ASCIIValue = ord(code)
                    ASCIIValue -= 3
                    answer += chr(ASCIIValue)
        else:
            morse = {'..-.': 'F', '-..-': 'X', '/': ' ', '.--.': 'P', '-': 'T', '..---': '2',
                        '....-': '4', '-----': '0', '--...': '7', '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                        '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                        '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                        '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                        '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                        '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}
            text += " "
            temp = ""
            for code in text:
                if code == '/':
                    answer += " "
                elif code != " ":
                    temp += code
                elif type(morse.get(temp)) == str:
                    answer += str(morse.get(temp))
                    temp = ""
            answer = answer.lower()
        cwd = os.getcwd()
        os.chdir(output_directory)
        outputname  = "test_file" + str(i) + "_b64065ab.txt"
        output = open(outputname, "w")
        output.write(answer)
        output.close()
        i += 1
        os.chdir(cwd)
        cwd = ""