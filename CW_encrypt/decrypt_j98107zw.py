MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-','!': '-.-.--',
                   ';': '-.-.-.', '_': '..--.-'}
file_path = input("please enter the test file path here")
message_file = open(file_path,'r')
message = message_file.read()
# C:\Users\骁骁\Desktop\midterm_files_data\midterm_files\Example_inputs\Example_inputs_program2\test_file3.txt

cipher= []
plain = []
cipher = list(MORSE_CODE_DICT.values())
plain = list(MORSE_CODE_DICT.keys())
real_message = message.split('/')[1:]
print(real_message)
cipherposition = 0
plaintext_total = []
for i in real_message:
    single = i.split(' ')[1:]
    for j in single:
