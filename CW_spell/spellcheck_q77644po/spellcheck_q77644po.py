import sys
dicpath=sys.argv[1]
inputpath=sys.argv[2]
outputpath=sys.argv[3]




def spell(s,dic):
    puncNum=0
    numNum=0
    upNum=0
    #--------------------------------------removing punctuations--------------------------------------------
    #: the period, question mark, exclamation point, comma, colon, semicolon, dash, hyphen, brackets, braces, parentheses, apostrophe, quotation mark, and ellipsis
    symbs=['.','?','!',',',':',';','–','—','-','[',']','{','}','(',')',"'",'"','…']    

    s2=''    
    for i in range(len(s)):
        if s[i] in symbs:
            puncNum=puncNum+1
        else:
            s2=s2+s[i]
    
    #---------------------------------------removing numbers-------------------------------------------------
    numbers=['1','2','3','4','5','6','7','8','9','0']
    s3=''
    for i in range(len(s2)):
        if s2[i] in numbers:
            numNum=numNum+1
        else:
            s3=s3+s2[i]
    
    #----------------------------------------lowercasing----------------------------------------------------
    finalString=''
    for i in range(len(s3)):
        if s3[i].lower() != s3[i]:
            finalString=finalString+s3[i].lower()
            upNum=upNum+1
        else:
            finalString=finalString+s3[i]
    
    #--------------------------------------------removing ''  and '\n' out of words array-----------------------------------------------------------
    words_s=finalString.split(' ')
    words=[]
    for i in range(len(words_s)):
        if words_s[i]!='' and words_s[i]!='\n':
            words.append(words_s[i])
    #--------------------------------------------checking the dictioanry-----------------------------------------------------
    
            
    dic=dic.split('\n')
    incorrect=0
    correct=0
    for i in range(len(words)):
        if words[i] in dic :
            correct=correct+1
            
        else:
            incorrect=incorrect+1
            
            
    message1='q77644po\nFormatting ###################\nNumber of upper case letters changed: ' + str(upNum) + '\nNumber of punctuations removed: ' + str(puncNum) + '\nNumber of numbers removed: ' + str(numNum) +'\n'
    message2='Spellchecking ###################\nNumber of words: ' + str(len(words)) + '\nNumber of correct words: ' + str(correct) + '\nNumber of incorrect words: ' + str(incorrect) 
    
    return(message1+message2)
            

    
    



import os
files=os.listdir(inputpath)
for i in range(len(files)):
    if files[i].endswith(".txt"):
        inputname=inputpath+'/'+files[i]
        inputfile=open(inputname)
        dicfile=open(dicpath)
        outputname=files[i][:-4]+'_q77644po'+'.txt'
        outputfile=open(outputpath+'/'+outputname,'w')
        outputfile.write(spell(inputfile.read(),dicfile.read()))
        
        


    
