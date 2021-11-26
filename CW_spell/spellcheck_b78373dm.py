import sys
import os

#functions

def check(x):
    global num_removed, punc_removed, upper_changed
    if x.isdigit():
        num_removed+=1
        return("")
    elif not x.isalpha() and x!=" " and x!="\n" and not x.isdigit() :
        punc_removed+=1
        return("")
    else:
        asc=ord(x)
        if asc>64 and asc<91:
            asc+=32
            x=chr(asc)
            upper_changed+=1
        return(x)
    
        
    
        
dictionary=sys.argv[1]  
folder_to_read = sys.argv[2]
folder_to_write = sys.argv[3]

try:
    os.mkdir(folder_to_write)
except OSError:
    print("")

file=open(dictionary).read()

for filename in os.listdir(folder_to_read):
    if filename.endswith(".txt"):


    



        to_check=open(folder_to_read+"/"+filename).read()
        num_removed=0
        punc_removed=0
        upper_changed=0



        #formatting
        formatted=""
        for letters in to_check:
            letter=check(letters)
            formatted+=letter

        #checking

        original=[]
        final=[]
        file_words=file.splitlines()



        index=0

        to_check+=" "
        formatted+=" "

        file+=" "

        while index<len(formatted):
            word=""
            while formatted[index]!=" ":
                word+=formatted[index]
                index+=1
            if word!="" and word!="\n":
                original.append(word)
            index+=1

        index=0

        while index<len(formatted):
            word=""
            while formatted[index]!=" ":
                word+=formatted[index]
                index+=1
            if word!="":
                final.append(word)
            index+=1

        for word in final:
            if word not in file_words:
                final.remove(word)


        words_in_file=len(original)
        correct_words=len(final)
        incorrect_words=len(original)-len(final)

      


        result=open(folder_to_write+"/"+filename[0:-4]+"_b78373dm.txt","w")

        result.write("""b78373dm\nFormatting ###################
Number of upper case letters changed: """+str(upper_changed)+
        """\nNumber of punctuations removed: """+str(punc_removed)+
        """\nNumber of numbers removed: """+str(num_removed)+
        """\nSpellchecking ###################
Number of words: """+str(words_in_file)+
        """\nNumber of correct words: """ + str(correct_words)+
        """\nNumber of incorrect words: """ + str(incorrect_words))


