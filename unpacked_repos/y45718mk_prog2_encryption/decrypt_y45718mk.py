import os, argparse, re, string

parser = argparse.ArgumentParser()
#parser.add_argument("english", type=open)
parser.add_argument("inputpath", type=str, help= "paste path to inout files")
parser.add_argument("outputpath", type=str, help= "paste path to output files")

originalpath = os.getcwd()

args = parser.parse_args()
path = args.inputpath
output_path = args.outputpath
os.chdir(args.inputpath)
cwd = os.getcwd()

input_file_names = os.listdir()
txt = ".txt"
counter = 0
list_of_files = []
for n in range(len(input_file_names)):
    if re.search(txt, input_file_names[n]):
        counter += 1
        list_of_files.append(input_file_names[n])
        #print(input_file_names[n])
        #print(type(input_file_names[n]))
        x = open(str(input_file_names[n]), "r").readlines()
        #print(x)

for n in range(len(input_file_names)):
    input_file_names[n] = re.split(r'\.txt', input_file_names[n])
    #print(input_file_names[n])
result = []
#print(list_of_files)
list_of_files.sort()
#print(list_of_files)

for n1 in list_of_files:
    open_file = open(n1, "r").readlines()
    #print(open_file)

    eachone = list(open_file[0])
    #print(eachone)


    for item in eachone:
        if item == ":":
            #print ("It is found!")
            index = eachone.index(":")
            #print("The index of ':' is:", index)
            break

    start_index_of_the_encripted_code = index + 1
    encripted_list = eachone[start_index_of_the_encripted_code : ]
    #print(encripted_list)

    the_whole_encripted_code_as_a_single_list = open_file[0][(index + 1) : ]
    #print(the_whole_encripted_code_as_a_single_list)
    if open_file[0][0] == "H":
        # print("This is Hexadecimal!")
        hex = bytes.fromhex(the_whole_encripted_code_as_a_single_list)
        string = hex.decode("ASCII")
        # print(string)
        print(string.lower())
        answer = string.lower()
        result.append(answer)
        #list2 = open("list2.txt", "w")
        #list2.write(string.lower())


    elif open_file[0][0] == "C":
        # print("This is caesar +3!")
        ciphertext = the_whole_encripted_code_as_a_single_list
        #print(ciphertext)
        plainTest = ""
        ciphertextPosition = 0
        x = ciphertext.replace(" ", "32")
        while ciphertextPosition < len(x):
	        ciphertextChar = x[ciphertextPosition]
	        ASCIIValue = ord(ciphertextChar)
	        ASCIIValue -= 3
	        plainTest += chr(ASCIIValue)
	        ciphertextPosition += 1
        # print(plainTest)
        y = plainTest.replace("0/", " ")
        # print(y)
        w = y.replace("_", "y")
        i = w.replace("`", "z")
        bia = i.replace("^", "x")
        print(bia.lower())
        answer2 = bia.lower()

        result.append(answer2)
        #list2 = open("list2.txt", "w")
        #list2.write(y.lower())
    else:
        # print("This is morseCode!")
        z = the_whole_encripted_code_as_a_single_list #.replace("/", ".....")
        #print(the_whole_encripted_code_as_a_single_list)
        #print(z)
        morse_to_plaintext = {'..-.': 'F', '-..-': 'X', '.--.': 'P', '-': 'T', '..---': '2', '....-': '4', '-----': '0', '--...': '7', '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J', '---': 'O', '-.-': 'K', '----.': '9', '..': 'I', '.-..': 'L', '.....': ' ', '...--': '3', '-.--': 'Y', '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R', '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q', '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1', "......": "5"}
        morse_code = z.split()
        #print(morse_code)
        #for temp in range(0, len(morse_code)):
            #print(morse_to_plaintext.get(morse_code[temp]).lower(), end = "")
        def morse_to_plaintext2(text):
            morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', ' ': '/'}
            Mehdi = {value: key for key, value in morse.items()}

            if '-' in text:
                return ''.join(Mehdi[i] for i in text.split())
            return ' '.join(morse[i] for i in text.upper())
        f = morse_to_plaintext2(z)
        print(f.lower())
        answer3 = f.lower()
        result.append(answer3)
        #list2 = open("list2.txt", "w")
        #list2.write(f.lower())
name = []
#print(list_of_files)
for i in list_of_files:
    #print(i)
    for ii in i:
        if ii == ".":
            index = i.index(".")
            #print(index)
            name.append(i[0:index])
            break
#print(name)
for i in range(len(list_of_files)):
    filename = name[i] + "_y45718mk"+ ".txt"
    outfile = open(filename, "w")
    outfile.write(str(result[i]))
    outfile.write("\n")
    outfile.close()





print(result)
