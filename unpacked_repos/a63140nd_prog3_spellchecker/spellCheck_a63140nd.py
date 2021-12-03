import re
import os
d= os.getcwd()
fname= os.path.join(d, "midterm_files/Example_inputs/Example_inputs_program3/test_file4.txt")
file = open(fname, "r")
text= (file.read())
f2name= os.path.join(d, "midterm_files/EnglishWords.txt")
file_2 = open(f2name, "r")
words = (file_2.read())
count= 0
r = re.findall('([A-Z])', text)
text = text.lower()
my_matches = re.findall(r'[^\w\s]', text)
for ele in text:
    if ele in my_matches:
        text = text.replace(ele, " ")
temp = re.findall(r'\d', text)
res = list(map(int, temp))
wrongWords=[]
correctWords=[]

for i in str(res):
    if i in text:
        text = text.replace(i, " ")
oneByOne= text.split()
for i in range (0, len(text.split())):
    if oneByOne[count] not in words:
        wrongWords.append(oneByOne[count])
        count += 1
    else:
        correctWords.append(oneByOne[count])
        count += 1
outFileName= os.path.join(d, "midterm_files/output_files/output_program3/test_file4_a63140nd.txt")
with open(outFileName, 'w') as f:
    f.write('Formatting ###################  \n')
    f.write("Number of numbers removed: " + str(len(res)) + "\n")
    f.write("Number of upper case words transformed: " + str(len(r)) + "\n")
    f.write("Number of punctuation’s removed: " + str(len(my_matches))+ "\n")
    f.write("Spellchecking ###################  \n")
    f.write("Number of words in file: " + str(len(oneByOne))+ "\n")
    f.write("Number of incorrect words in file: " + str(len(wrongWords))+ "\n")
    f.write("Number of correct words in file: " + str(len(correctWords))+ "\n")

