import os,sys
path = sys.argv[2]
FileList = os.listdir(path)
LowerCaseLetters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
UpperCaseLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Punctuation = ['.','?','!',',',':',';','–','-' ,'[',']' ,'{','}','(',')', "'",'"']
Numbers = ['0','1','2','3','4','5','6','7','8','9']
FormattingDict = {
	"A":"a","B":"b","C":"c","D":"d",
	"E":"e","F":"f","G":"g","H":"h","I":"i","J":"j",
	"K":"k","L":"l","M":"m","N":"n","0":"o","P":"p",
	"Q":"q","R":"r","S":"s","T":"t","U":"u","V":"v",
	"W":"w","X":"x","Y":"y","Z":"z",
	"1":"","2":"","3":"","4":"","5":"","6":"",
	"7":"","8":"","9":"","0":"",
	".":"","?":"","!":"",",":"",":":"",";":"",
	"–":"","-":"","{":"","}":"","(":"",")":"",
	"[":"","]":"","'":"",'"':"","...":""
}
for file in FileList:
	print(file[-9999:-4]+"_y59276ma.txt")
	OutputFile = sys.argv[3] +"/"+file[-999:-4]+"_y59276ma.txt"
	InputFile = sys.argv[2] + "/" +file
	EnglishWords = sys.argv[1] + "/EnglishWords.txt"
	WordFile = open(InputFile,"r")
	DataInWordFile = WordFile.read().split()
	WordFile.close()
	AllEnglishWords = open(EnglishWords,"r")
	AllWords = AllEnglishWords.read().split()
	AllEnglishWords.close()
	FormattedText = ""
	ElipsesCount,NumbersRemoved,PunctuationRemoved,CountUpperToLower = 0,0,0,0
	CorrectWordCount, IncorrectWordCount = 0,0
	for item in DataInWordFile:
		for c in item:
			if(c not in LowerCaseLetters):
				if(c =='.'):
					ElipsesCount += 1
				else:
					ElipsesCount = 0
				FormattedText = FormattedText + FormattingDict[c]
				if(c in UpperCaseLetters):
					CountUpperToLower += 1
				elif(c in Punctuation):
					if(ElipsesCount==3):
						PunctuationRemoved -= 2
						ElipsesCount = 0
					else:
						 PunctuationRemoved += 1
				elif(c in Numbers):
					NumbersRemoved += 1
			else:
				FormattedText = FormattedText + c
		FormattedText = FormattedText + " "
	for word in FormattedText.split():
		if(word in AllWords):
			CorrectWordCount += 1
		else:
			IncorrectWordCount +=1
	ChangesMade = open(OutputFile,"x")
	ChangesMade.write("y59276ma\n"+"Formatting ###################\n"+"Number of upper case letters changed:"+str(CountUpperToLower)+"\nNumber of punctuations removed:"+str(PunctuationRemoved)+ "\nNumber of numbers removed: "+str(NumbersRemoved)+"\nSpellchecking ###################\n"+ "Number of words:"+str(len(FormattedText.split()))+"\nNumber of correct words: "+str(CorrectWordCount)+"\nNumber of incorrect words: "+str(IncorrectWordCount))
	ChangesMade.close()	