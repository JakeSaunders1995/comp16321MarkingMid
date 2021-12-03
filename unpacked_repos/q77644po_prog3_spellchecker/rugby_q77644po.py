import sys
inputpath=sys.argv[1]
outputpath=sys.argv[2]



def score(s):
    s=s.split("T")
    pointlist=['p','d']
    points=[0,0]
    
    for i in range(1,len(s)):
        if s[i][1] in pointlist:
            points[int(s[i][0])-1] = points[int(s[i][0])-1] + 3
        if s[i][1] == 'c':
            points[int(s[i][0])-1] = points[int(s[i][0])-1] + 2     
        if s[i][1] == 't':
            points[int(s[i][0])-1] = points[int(s[i][0])-1] + 5
    return(str(points[0]) + ':' + str(points[1]))



import os
files=os.listdir(inputpath)
for i in range(len(files)):
    if files[i].endswith(".txt"):
        inputname=inputpath+'/'+files[i]
        inputfile=open(inputname)
        outputname=files[i][:-4]+'_q77644po.txt'
        outputfile=open(outputpath+'/'+outputname,'w')
        outputfile.write(score(inputfile.read()))
        
        


    
