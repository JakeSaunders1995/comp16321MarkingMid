import sys
username = "_e00336tj"
fileList = []
index = 0
for file in sys.argv[1:]:
    if username in file:
        index = sys.argv[1:].index(file.replace(username,""))
        filePair = [sys.argv[1:][index],file]
        fileList.append(filePair)
for pair in fileList:
	inputFile = open(pair[0],'r')
	inputstring = inputFile.read()
	outputFile = open(pair[1],'w')
	decodeList = [["20"," "],["2a","*"],["2b","+"],["2c",","],["2d","-"],["2e","."],["2f","/"],["30","0","-----"],["31","1",".----"],["32","2","..---"],["33","3","...--"],["34","4","....-"],["35","5","....."],["36","6","-...."],["37","7","--..."],["38","8","---.."],["39","9","----."],["3a",":"],["3b",";"],["3c","<"],["3d","="],["3e",">"],["3f","?"],["40","@"],["41","A"],["42","B"],["43","C"],["44","D"],["45","E"],["46","F"],["47","G"],["48","H"],["49","I"],["4a","J"],["4b","K"],["4c","L"],["4d","M"],["4e","N"],["4f","O"],["50","P"],["51","Q"],["52","R"],["53","S"],["54","T"],["55","U"],["56","V"],["57","W"],["58","X"],["59","Y"],["5a","Z"],["5b","["],["5c","\\"],["5d","]"],["5e","^"],["5f","_"],["60","`"],["61","a",".-"],["62","b","-..."],["63","c","-.-."],["64","d","-.."],["65","e","."],["66","f","..-."],["67","g","--."],["68","h","...."],["69","i",".."],["6a","j",".---"],["6b","k","-.-"],["6c","l",".-.."],["6d","m","--"],["6e","n","-."],["6f","o","---"],["70","p",".--."],["71","q","--.-"],["72","r",".-."],["73","s","..."],["74","t","-"],["75","u","..-"],["76","v","...-"],["77","w",".--"],["78","x","-..-"],["79","y","-.--"],["7a","z","--.."]]
	codedString = inputstring[(inputstring.find(":"))+1:].lower()
	alg = inputstring[:(inputstring.find(":"))].lower()
	decodedText=""
	codedArray=[]
	if "hex" in alg:
		codedString = codedString.replace(" ","")
		for i in range(0, len(codedString), 2):
			codedArray.append(codedString[i:i+2])
		for i in codedArray:
			for j in decodeList:
				if str(i)==j[0]:
					decodedText += j[1]
	if "morse" in alg:
		codedArray = codedString.split(" ")
		for i in codedArray:
			if str(i) == "/":
				decodedText+=" " 
			for j in decodeList:
				if len(j)==3:
					if str(i)==j[2]:
						decodedText += j[1]
	if "caesar" in alg:
		for i in range(0, len(codedString)):
			codedArray.append(codedString[i])
		for i in codedArray:
			if i == " ":
				decodedText += i
			elif i in ["a","b","c"]:
				index = 'cba'.find(i)+1
				decodedText+= decodeList[-index][1]
			else:
				for j in range(len(decodeList)):
					if i == decodeList[j][1]:
						decodedText+=decodeList[j-3][1]
	outputFile.write(decodedText.lower())
	inputFile.close()
	outputFile.close()