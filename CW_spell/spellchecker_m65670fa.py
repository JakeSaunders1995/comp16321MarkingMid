import os, sys, re

input_folder = sys.argv[1]
output_folder = sys.argv[2]
dir_list = os.listdir(input_folder)
print(dir_list)

def Function():
    NumberOfUbber = 0
    newText = ""
    for i in mylist:
        if i.isupper() == True:
             NumberOfUbber += 1
             newText += (i.lower())
        elif i.isupper() == False:
            newText += i
    print("Number of upper case letters changed: ", NumberOfUbber)
    pattern = '[0-9]'
    numbers = "123456789"
    new_text = ""
    NumberOfNumbers = 0
    for j in mylist:
        if j not in numbers:
            new_text = new_text
        else:
            new_text = re.sub(pattern, '', mylist)
            NumberOfNumbers += 1
    print("Number of numbers removed: ", NumberOfNumbers)
    punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    NumberOfPunctuations = 0
    new_string = ""
    for char in mylist:
        if char not in punctuations:
            new_string = new_string + char

        else:
            NumberOfPunctuations += 1
    print("Number of punctuations removed: ", NumberOfPunctuations)

    output_file = dir_list[x].replace("txt", "_m65670fa.txt")
    output_file = output_folder + "/" + output_file
    with open(output_file, "a")as file:
        file.write(f'Number of upper case letters changed: {NumberOfUbber}')
        file.write(f'\nNumber of numbers changed: {NumberOfNumbers}')
        file.write(f'\nNumber of punctuations removed: {NumberOfPunctuations}')
        


x = 0

for x in range (x, len(dir_list),1):
    file = open(input_folder +"/"+ dir_list[x])
    print("\n")
    mylist=file.readline()
    Function()

