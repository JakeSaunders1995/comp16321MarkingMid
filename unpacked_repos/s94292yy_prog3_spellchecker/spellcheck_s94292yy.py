#Program 3 - spellchecker#
#
#
#Import the contents of the text into Python for subsequent operations.
input_file_name = str (input("Please type the file name: "))
file = open ("./input_folder/" + input_file_name, "r")
filerecord = file.read()
#Import the contents of the EnglishWords into Python for correcting input words.
EnglishWords = open ("EnglishWords.txt","r")
En_record = EnglishWords.read()
En_record = ' '.join(En_record.split())
En_record = En_record.split(' ')
# # #
# # #
# # #
#create dictionary for subsequent operations.
punctuation = [ '。','，','、','＇','：','∶','；','?','‘','’','“','”','〝','〞','ˆ','ˇ','﹕','︰','﹔','﹖','﹑','·','¨','…','.','¸',';','！','´',
                '？','！','～','—','ˉ','｜','‖','＂','〃','｀','@','﹫','¡','¿','﹏','#','﹩','$','﹠','﹪','%','*','￣','¯',
                '―','+','=','＿','_','-','~','（','）','〈','〉','‹''›','﹛','﹜',"...",',',"[","]","&",":","'",'"','.'] #the punctuation dict

number = ['1','2','3','4','5','6','7','8','9','0'] #the number dict

Caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #the caps letter dict
Upper = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #the upper letter dict
# # #
# # #
# # #
#crate loop for calculating punctuations.
pun_count = 0
pun_stat = 0
while pun_count < len(filerecord): #while loop for have a correct circle.
    if filerecord[pun_count] in punctuation:
        #if our position of filerecord equal ', we dont need to put space in this, beacuse it includes wrods right and left.
        if filerecord[pun_count] != "'":
            filerecord = filerecord.replace(filerecord[pun_count], " ", 1)
            pun_count += 1
            pun_stat += 1
        elif filerecord[pun_count] == "'":
            filerecord = filerecord.replace(filerecord[pun_count], "", 1)
            pun_count += 1
            pun_stat += 1
    #to let pun_count has increment.
    else:
        pun_count +=1

#create loop for calculating numbers
num_count = 0
num_stat = 0
while num_count < len(filerecord):
    if filerecord[num_count] in number:
        filerecord = filerecord.replace(filerecord[num_count], " ", 1)
        num_count += 1
        num_stat += 1
    else:
        num_count +=1

#create loop for calculating letters.
letter_stat = 0 #create the letter_stat for calculating numbers of letters.
for i in range(len(filerecord)):
    if filerecord[i] in Caps:
        letter_stat += 1

#we now change the Caps letter to Upper letter.
chan = 0
for chan_count in range(len(Caps)):
    caps_letter = Caps[chan]
    upper_letter = Upper[chan]
    filerecord = filerecord.replace(caps_letter, upper_letter)
    chan += 1

#to let filerecord become the list.
filerecord = ' '.join(filerecord.split())
filerecord = filerecord.split(' ')
words_count = len(filerecord) #here we get the words_count

#Then we need to distinguish which words are correct and which words are wrong.
wrong_num = 0
correct_num = 0
for correction in range(len(filerecord)):
    if filerecord[correction] in En_record:
        correct_num += 1
    else:
        wrong_num += 1

#output the answer to output file.
input_file_name = input_file_name.replace(".txt","") #at here I need to delete the string ".txt" which users typed in
file_creation = open ("./output_folder/" + input_file_name + "_s94292yy.txt", "a")
file_creation.write ("s94292yy" + "\nFormatting ###################" + "\nNumber of upper case letters changed: " + str(letter_stat)
                        + "\nNumber of punctuations removed: " + str(pun_stat) + "\nNumber of numbers removed: " + str(num_stat)
                        + "\nSpellchecking ###################" + "\nNumber of words: " + str(words_count) + "\nNumber of correct words: "
                        + str(correct_num) + "\nNumber of incorrect words: " + str(wrong_num))
file_creation.close ()
#close the file to do new loop.
file.close()
EnglishWords.close()
