import os, re, string, sys
from posix import listdir

running_dir = __file__

main_dir, py_file =   os.path.split(running_dir)

txtfile=  sys.argv[1]
start = sys.argv[2]
end = sys.argv[3]

input_dir = os.path.join( main_dir,start)
output_dir = os.path.join( main_dir, end)
list_file = os.listdir(input_dir)


# spellchecking

open_file= open(txtfile) 
eng = open_file.read()
open_file.close()

for i in list_file:
    single_file = open(os.path.join(start,i), "r", encoding='windows-1252')
    get_data = single_file.read()
    single_file.close()
 

    #values

    punc=0
    num=0
    up=0
    correct=0
    incorrect=0
    count=0
    list_int = [0,1,2,3,4,5,6,7,8,9]
    punctuation = [".", "?", "!", ",", ":", ";", "-", "—", "[", "]", "{", "}", "(", ")", "'", '"']


    #Formatting
    
    import string
    from string import digits
    while ". . ." in get_data:
          count+=1
          get_data= get_data.replace(". . .","")
    newtext= re.sub(r'[^\w\s]','',get_data)
    newtext1=re.sub(r'[0-9]','',newtext)
    newtext2= newtext1.lower()



    #Count_for_formatting

    num= get_data.count('0')+ get_data.count('1')+get_data.count('2')+get_data.count('3')+get_data.count('4')+get_data.count('5')+get_data.count('6')+get_data.count('7')+get_data.count('8')+get_data.count('9')

    for char in get_data:
        if char in punctuation:
            punc=punc+1

    for char in get_data:
        if char.isupper():
            up=up+1

    
    #formatting_results:
    p1= "t02231ss"
    p2= "\nFormatting ###################"
    p3= "\nNumber of upper case letters changed:"+" "+str(up)
    p4= "\nNumber of punctuations removed:"+" "+str(punc+count)
    p5= "\nNumber of numbers removed:"+" "+str(num)
    

    #splitting

    words= newtext2.split()
    english= eng.split()
  
    #SpellChecking
    for word in words:
        if word in english:
            correct = correct +1
    wordcount= len(words)
    incorrect = wordcount - correct
  

    #spellchecking_results

    p6= "\nSpellchecking ###################"
    p7= "\nNumber of words:"+" "+str(wordcount)
    p8= "\nNumber of correct words:"+" "+str(correct)
    p9= "\nNumber of incorrect words:"+" "+str(incorrect)

    # save outputs

    new_i = i.replace('.txt', '_t02231ss.txt')
    
    target_output = open(os.path.join(output_dir, new_i),"wt")

    target_output.write(p1),target_output.write(p2),target_output.write(p3),target_output.write(p4),target_output.write(p5),target_output.write(p6),target_output.write(p7),target_output.write(p8),target_output.write(p9)
    target_output.close()

        


   
    
