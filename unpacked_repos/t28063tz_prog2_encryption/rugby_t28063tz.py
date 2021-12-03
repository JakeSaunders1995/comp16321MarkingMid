import sys
import os
def solve(input_str):
    T1 = 0
    T2 = 0
    for b in [input_str[i:i+3] for i in range(0, len(input_str), 3)] :
        add = 0
        if (b[2] == 't') : add = 5
        if (b[2] == 'c') : add = 2
        if (b[2] == 'p') : add = 3
        if (b[2] == 'd') : add = 3
        if (b[1] == '1') : T1 += add
        if (b[1] == '2') : T2 += add
    return T1, T2

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
        T1,T2 = solve(input_str)
        output_file = fileName.split('.txt')[0] + '_' + myName + '.txt'
        file = open(os.getcwd() + '/' + output_folder + '/' + output_file, "w")
        file.write('{}:{}'.format(T1, T2))
        file.close()
        # print(output_file)
        # print('{}:{}'.format(T1, T2))
#python3 rugby_t28063tz.py ./Example_inputs_program1 ./test_out
