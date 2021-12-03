import re
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("folder", type = str, nargs = "+")
args = parser.parse_args()
folders = args.folder
files = os.listdir(folders[1])

with open(folders[0], 'r') as file:
    x = file.readlines()
    x_new = [newlines.replace("\n", "") for newlines in x]
file.close()


for file in files:
    f = open(folders[1] + '/' + file,'r')

    input_Str = f.read()
    # Checking for number of UpperCase alphabets:

    count_uppercase = 0

    for uppercase in input_Str:
        if (uppercase.isupper()):
            count_uppercase += 1

    # Checking for number of Punctuations:
    num_ellipse = input_Str.count('...')
    punc = ["!", "''", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",
            "[", "]", "^", "_", "`", "{", "|", "}", "~",'"', "..."]

    punc_count = 0

    q = len(input_Str)
    for pun in range(q):
        if input_Str[pun] in punc:
            punc_count += 1
    punc_count = punc_count - 2*num_ellipse

    # Checking for number of digits in the string:

    num_count = 0

    for num in input_Str:
        if num.isnumeric():
            num_count += 1


    # Reformating String to remove any numbers as well as  punctuations
    # and replace it with an empty string using re libraries to search for numeric values:

    numerals = r'[0-9]'

    new_string = re.sub(numerals, '', input_Str)

    # print(new_string)

    punctuation = r'[!”"#$%&\’()*+,-./:;<=>?@\\^_`{|}~’]'
    new_string = re.sub(punctuation, '', new_string)
    new_string = new_string.replace("[]","")

    q = len(new_string)
    # print(new_string)


    # Converting to lower case

    A = r'A'
    new_string = re.sub(A, 'a', new_string)

    B = r'B'
    new_string = re.sub(B, 'b', new_string)

    C = r'C'
    new_string = re.sub(C, 'c', new_string)

    D = r'D'
    new_string = re.sub(D, 'd', new_string)

    E = r'E'
    new_string = re.sub(E, 'e', new_string)

    F = r'F'
    new_string = re.sub(F, 'f', new_string)

    G = r'G'
    new_string = re.sub(G, 'g', new_string)

    H = r'H'
    new_string = re.sub(H, 'h', new_string)

    I = r'I'
    new_string = re.sub(I, 'i', new_string)

    J = r'J'
    new_string = re.sub(J, 'j', new_string)

    K = r'K'
    new_string = re.sub(K, 'k', new_string)

    L = r'L'
    new_string = re.sub(L, 'l', new_string)

    M = r'M'
    new_string = re.sub(M, 'm', new_string)

    N = r'N'
    new_string = re.sub(N, 'n', new_string)

    O = r'O'
    new_string = re.sub(O, 'o', new_string)

    P = r'P'
    new_string = re.sub(P, 'p', new_string)

    Q = r'Q'
    new_string = re.sub(Q, 'q', new_string)

    R = r'R'
    new_string = re.sub(R, 'r', new_string)

    S = r'S'
    new_string = re.sub(S, 's', new_string)

    T = r'T'
    new_string = re.sub(T, 't', new_string)

    U = r'U'
    new_string = re.sub(U, 'u', new_string)

    V = r'V'
    new_string = re.sub(V, 'v', new_string)

    W = r'W'
    new_string = re.sub(W, 'w', new_string)

    X = r'X'
    new_string = re.sub(X, 'x', new_string)

    Y = r'Y'
    new_string = re.sub(Y, 'y', new_string)

    Z = r'Z'
    new_string = re.sub(Z, 'z', new_string)

    #print(new_string)

    list_input_Str = new_string.split(' ')

    # Removing empty strings from list_input_str:
    if __name__ == '__main__':
        val = ''
        try:
            while True:
                list_input_Str.remove(val)
        except ValueError:
            pass

        #print(list_input_Str)

    if __name__ == '__main__':
        val = '\n'
        try:
            while True:
                list_input_Str.remove(val)
        except ValueError:
            pass

        #print(list_input_Str)

    # Spellchecking:
    count_correct = 0
    count_wrong = 0


    p = len(list_input_Str)
        # punc_count = len(input_Str) - p
    for r in range(p):
        if list_input_Str[r] in x_new:
            count_correct += 1
        else:
            count_wrong += 1

        # print(x_new)


    f.close()
    ind = file.index(".")
    f_name = file[0:ind]
    o = open(folders[2] + "/" + f_name + '_j96158ap.txt', 'w')

    o.write("j96158ap\n")
    o.write("Formatting ###################\n")
    o.write("Number of upper case words changed: " + str(count_uppercase) + "\n")
    o.write("Number of punctuations removed: " + str(punc_count) + "\n")
    o.write("Number of numbers removed: " + str(num_count) + "\n")
    o.write("Spellchecking" + " ###################" + "\n")
    o.write("Number of words: " + str(p) + "\n")
    o.write("Number of correct words: " + str(count_correct) + "\n")
    o.write("Numbers of incorrect words: " + str(count_wrong) + "\n")

    o.close()


