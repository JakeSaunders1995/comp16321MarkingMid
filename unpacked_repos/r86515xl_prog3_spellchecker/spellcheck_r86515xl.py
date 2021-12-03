


def make_out(name, out):
    path1 = os.path.abspath(output_folder)
    path2 = path1 + '/' + name.replace('.txt','') + '_r86515xl' + '.txt'
    file = open(path2,'w')
    file.write(out)

def formatting(file):
    upper = 0
    punctuation = 0
    number = 0
    words = 0
    correct = 0
    incorrect = 0
    if '...' in file:
        punctuation = punctuation - 2
    for i in file:
        if str.isupper(i) == True:
            upper += 1
        elif i in '1234567890':
            number += 1
            file = file.replace(i, '')
        elif i in {'?','!',',', ':', ';', '——', '-', '[', ']', '{', '}', '(', ')', '\'', '\"', '.'}:
            punctuation += 1
            file = file.replace(i, '')


    file = file.lower()
    file_split = list(file.split(' '))
    for i in file_split:
        if i != '' and i != '\n':
            words += 1
            if re.search('\\b' + i + '\\b',dictionary) != None:
                correct += 1
            else:
                incorrect += 1

    a= ('r86515xl \n' +
        'Formatting ################### \n'+
        'Number of upper case letters changed: ' + str(upper) + '\n'+
        'Number of punctuations removed: ' + str(punctuation) + '\n'+
        'Number of numbers removed: ' + str(number) + '\n'+
        'Spellchecking ################### \n'+
        'Number of words: ' + str(words) + '\n'+
        'Number of correct words: ' + str(correct) + '\n'+
        'Number of incorrect words: ' + str(incorrect) + '\n'
        )
    return a




import sys,os,re
script, dictionary, input_folder, output_folder = sys.argv
dirs = os.listdir(input_folder)
dictionary = open(dictionary)
dictionary = dictionary.read()
for file_name in dirs:

    path = os.path.abspath(input_folder)
    file = open(path + '/' + file_name,'r')
    file = file.read()
    a = formatting(file)
    make_out(file_name,str(a))
