import argparse
import os
parser= argparse.ArgumentParser()
parser.add_argument('ePath', type=str)
parser.add_argument('iPath', type=str)
parser.add_argument('oPath', type=str)
args = parser.parse_args()

Dict     = [line.rstrip("\n") for line in open(args.ePath)]

FileList=os.listdir(args.iPath)
FilenameList=[]
for item in FileList:
    if ".txt" in item:
        FilenameList.append(item)
for Filename in FilenameList:
    Text = [line.rstrip("\n") for line in open(args.iPath+"/"+Filename,"r")]
    Text = "".join(Text)
    def CheckEmpty(item):
        global EoN
        if not item:
            EoN="Empty"
        else:
            EoN="Not Empty" 
    CheckEmpty(Text)
    if EoN == "Not Empty":
        Text1= Text
        def removingUnnecessaryItem():
            global Text, UpperCaseNum,Number,Numbers,punctuationNum
            Number  = ["1","2","3","4","5","6","7","8","9","0"]
            Numbers = 0
            UpperCaseNum=0
            for x in Text:
                if x.isupper()==True:
                    UpperCaseNum+=1

            Text=Text.lower()

            Textlist = list(Text)
            for i in range(len(Textlist)):
                for l in range(len(Number)):
                    if Textlist[i]==Number[l]:
                        Numbers+=1
                        Textlist[i] = ""

            punctuation=[".","?","!",",",":",";","—","-","[","]","(",")","{","}","'",'"',"…"]
            punctuationNum=0
            for i in range(len(Textlist)):
                x = Textlist[i]
                if x != "":
                    if x in punctuation:
                        Textlist[i] = ""
                        punctuationNum+=1
                    else:
                        y =ord(Textlist[i])
                        if y<97:
                            if y!=32:
                                Textlist[i] = ""
                        if y>122:
                            Textlist[i] = ""
            Text="".join(Textlist)

        removingUnnecessaryItem()
        Text = Text + " "
        NumberofWords=0
        Num_Co=0
        Num_In=0
        TextforProcess  = Text
        while TextforProcess != "":
            Space = " "
            Word = TextforProcess[0:TextforProcess.index(" ")]
            if Word=="":
                pass
            else:
                NumberofWords+=1
                if Word in Dict:
                    Num_Co  +=1
                else: 
                    Num_In+=1

            TextforProcess = TextforProcess[TextforProcess.index(" ")+1:]
        
        Eclipse="..."
        Eclipse2=". . ."
        EclipseNum=0
        Text2 = Text1
        while True :
            if Eclipse in Text1:
                EclipseNum += 1 
                Text1 = Text1[Text1.index(Eclipse)+3:]
            if Eclipse2 in Text2:
                EclipseNum += 1 
                Text2 = Text2[Text2.index(Eclipse2)+5:]
            else:
                break
        punctuationNum = punctuationNum - EclipseNum*2
            
        output = open(args.oPath+"/"+Filename[:-4]+"_s23522ym.txt","w")
        output.write("s23522ym"+"\n")
        output.write("Formatting ###################"+"\n")
        output.write("Number of upper case letters changed: "+str(UpperCaseNum)+"\n")
        output.write("Number of punctuations removed: "+str(punctuationNum)+"\n")
        output.write("Number of numbers removed: "+str(Numbers)+"\n")
        output.write("Spellchecking ###################"+"\n")
        output.write("Number of words: "+str(NumberofWords)+"\n")
        output.write("Number of correct words: "+str(Num_Co)+"\n")
        output.write("Number of incorrect words: "+str(Num_In)+"\n")