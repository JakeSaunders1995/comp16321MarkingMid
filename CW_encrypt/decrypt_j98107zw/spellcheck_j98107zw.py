file_path = input("please entry the test file here")
f = open(file_path, 'r')
message = f.read()
# print(message)
file_path2 = input('please enter the english words file here')
f2 = open(file_path2,'r')
EnglishWords = f2.readlines()
englishwords_list = []
for i in EnglishWords:
    if i[-1]=='\n':
        englishwords_list.append(i[:-1])
    else:
        englishwords_list.append(i)
text = ''
Upper = 0
number = 0
removed = 0
correct_words = 0
not_words = 0
for i in range(len(message)):
    for j in message[i]:
        if ('a'<=j<='z' ):
            text += j
        elif j ==' ' :
            text += j
        elif'A'<=j<='Z':
            Upper += 1
            text +=j.lower()
        elif '0'<=j<='9':
            number +=1
        else:
            removed +=1
    low_text = text.split(' ')

    sentence=''
    for ii in low_text:
        if ii!='':
            sentence+=ii+' '
    sentence=sentence[:-1]
words = len(low_text)
words_correct = sentence.split(' ')
for j in words_correct:
    if j in englishwords_list:
        correct_words +=1

    else:
        not_words +=1
output = []
output.append('j98107zw\n')
output.append('Formatting ###################\n')
output.append('Number of upper case letters changed:' + str(Upper) +'\n')
output.append('Number of punctuations removed:' + str(removed) +'\n')
output.append('Number of numbers removed:' + str(number) +'\n')
output.append('Spellchecking ###################\n')
output.append('Number of words:' + str(words) +'\n')
output.append('Number of  correct words:' + str(correct_words) +'\n')
output.append('Number of incorrect words:' + str(not_words) +'\n')

output_path = input('please enter the output file path here')
f_output = open(output_path, "w", encoding='utf-8')
for texts in output:
    f_output.write(texts)
f_output.close()
