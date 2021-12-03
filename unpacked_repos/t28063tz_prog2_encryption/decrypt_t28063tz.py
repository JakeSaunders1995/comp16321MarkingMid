import sys
import os

map = dict()
map['.-'] = 'a'
map['-...'] = 'b'
map['-.-.'] = 'c'
map['-..'] = 'd'
map['.'] = 'e'
map['..-.'] = 'f'
map['--.'] = 'g'
map['....'] = 'h'
map['..'] = 'i'
map['.---'] = 'j'
map['-.-'] = 'k'
map['.-..'] = 'l'
map['--'] = 'm'
map['-.'] = 'n'
map['---'] = 'o'
map['.--.'] = 'p'
map['--.-'] = 'q'
map['.-.'] = 'r'
map['...'] = 's'
map['-'] = 't'
map['..-'] = 'u'
map['...-'] = 'v'
map['.--'] = 'w'
map['-..-'] = 'x'
map['-.--'] = 'y'
map['--..'] = 'z'
map['.----'] = '1'
map['..---'] = '2'
map['...--'] = '3'
map['....-'] = '4'
map['.....'] = '5'
map['-....'] = '6'
map['--...'] = '7'
map['---..'] = '8'
map['----.'] = '9'
map['-----'] = '0'
map['------'] = '.'
map['/'] = ' '

def solveMorse(input):
    ans = ''
    # print(input)
    now = ''
    flag = 0
    for i in input:
        if (i == ' '):
            flag = 1
        else :
            if (flag == 1):
                ans += map[now]
                flag = 0
                now = i
            else :
                now += i
    if (len(now) > 0) : ans += map[now]
    # print (ans)
    return ans

def solveHex(input):
    ans = ''
    # print(input)
    for i in range(0, len(input), 3):
        # print(input[i:i+2])
        # print(chr(int(input[i:i+2], 16)))
        ans += chr(int(input[i:i+2], 16)).lower()
    # print(ans)
    return ans

def solveCaesar(input):
    ans = ''
    # print(input)
    for i in input:
        if (i != ' '):
            ans += chr(ord(i)-3).lower()
        else :
            ans += i
    # print(ans)
    return ans

def solve(input):
    ans = ''
    if (input[0] == 'H'):
        ans = solveHex(input[4:])
    elif (input[0] == 'C'):
        ans = solveCaesar(input[18:])
    elif (input[0] == 'M'):
        ans = solveMorse(input[11:])
    else : ans = 'input error'
    return ans

if __name__ == '__main__':
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    myName = 't28063tz' 
    # print(input_folder, output_folder)
    all_files = []
    for i in os.listdir(os.getcwd() +'/' + input_folder):
        all_files.append(i)
    for fileName in all_files:
        file = open(os.getcwd() + '/' + input_folder + '/' + fileName , "r")
        input_str = file.read()
        file.close()
        ans = solve(input_str)
        output_file = fileName.split('.txt')[0] + '_' + myName + '.txt'
        file = open(os.getcwd() + '/' + output_folder + '/' + output_file, "w")
        file.write(ans)
        file.close()

#python3 decrypt_t28063tz.py ./Example_inputs_program2 ./test_out
