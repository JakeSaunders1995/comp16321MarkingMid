
#/home/csimage/Program3/input files
import os
def format (check):
    
    n=0
    u=0
    p=0
    a=0
    w=0
    incorrect=0
    correct=0
    list_1 = list(check)
    list_n=['0','1','2','3','4','5','6','7','8','9']
    list_u=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    list_p=[".", "?","!", "-","(",")","[","]","{","}", ":",";","'",'"',"/",","]
    list_space=[" "]
    list_1_new=[]
    for c in list_1:
        if c in list_n:
            n=n+1   
            #数字不需要往新列表中添加
            continue
        elif c in list_u:
            u=u+1
            #把转换后的小写字母添加进去
            list_1_new.append(c.lower())
        elif c in list_p: 
            p=p+1
            #标点符号不需要添加到新列表
            continue
        else :
            list_1_new.append(c.lower())

    str="".join(list_1_new)
    list_2=str.split(' ')
    list_2_new=[i for i in list_2]

    with open("EnglishWords.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件    
        list_d=list(data)
        str="".join(list_d)
        list_d=str.split('\n')
        for c in list_2_new:
            #判断是否为空字符串或者空格,则跳过不统计
            if len(c)==0 or c.isspace():
                continue
            if c in list_d:
                correct=correct+1
                w=w+1
            else:
                incorrect=incorrect+1
                w=w+1


    list_3=[u,p,n,w,correct,incorrect]
    return list_3





print("please input input files dir  \n")
dataDir = input()
print("please input output files dir  \n")
dirPath = input()
for root, dirs, files in os.walk(dataDir):
    for file in files:
        if os.path.splitext(file)[1] == '.txt':
            f=open(root+"/"+file,'r')
            check=f.read()             
            final=format(check)
            
           
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)
            with open(dirPath+"/"+file,"w") as f:
                test = f.write('z03463sy\nFormatting ###################\n'+
                    'Number of upper case words transformed:'+str(final[0])+
                    '\nNumber of punctuation’s removed:'+str(final[1])+
                    '\nNumber of numbers removed:'+str(final[2])+
                    '\nFormatting ###################'+
                    '\nNumber of words:'+str(final[3])+
                    '\nNumber of correct words:'+str(final[4])+
                    '\nNumber of incorrect words:'+str(final[5]))
                
                