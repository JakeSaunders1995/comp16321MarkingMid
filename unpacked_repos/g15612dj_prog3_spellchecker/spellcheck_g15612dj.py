import string
import sys
import os

def spell(st,dicIn):
	dicArr = dicIn.split("\n")
	capcount = sum([1 for let in st if let in string.ascii_uppercase])
	numcount = sum([1 for char in st if char in string.digits])
	puncstring = str(string.punctuation)
	puncstring = puncstring.translate({ord('#'):None,ord('@'):None})
	punclist = list((puncstring))
	punclist.append('...')
	prepunc = ([st.count(char) for char in punclist])
	elipseidx = punclist.index('...')
	periodidx = punclist.index('.')
	elipsecount = prepunc[elipseidx]
	prepunc[periodidx] -= (3*elipsecount)
	newfile = st
	puncount = sum(prepunc)
	mydic = dict([(ord(x),None) for x in (puncstring+string.digits+'\n')])
	newfile = st.translate(mydic)
	newfile = newfile.lower()
	wwc = 0
	rwc = 0
	newArr = newfile.split(" ")
	while '' in newArr:
		newArr.remove('')
	wwl = []
	for wrd in newArr:
		if dicArr.count(wrd) == 0:
			wwc += 1
			wwl.append(wrd)
	output = ('g15612dj\
\nFormatting ###################\
\nNumber of upper case words transformed: %d\
\nNumber of punctuation’s removed: %d\
\nNumber of numbers removed: %d\
\nSpellchecking ###################\
\nNumber of words in file: %d\
\nNumber of correct words in file: %d\
\nNumber of incorrect words in file: %d' % (capcount,puncount,numcount,len(newArr),len(newArr)-wwc,wwc,))
	return output
owd = os.getcwd()

diction = open(sys.argv[1]).read()
try:
	os.chdir(sys.argv[2])
except:
	os.chdir(owd+"/"+sys.argv[2])
	print('relative folderpath used as argument[1]')
inputfolderpath = os.getcwd()
try:
	os.chdir(sys.argv[3])
except:
	try:
		os.chdir(owd+"/"+sys.argv[3])
		print('relative folderpath used as argument[1]')
	except:
		os.chdir(owd)
		os.mkdir(sys.argv[3])
		os.chdir(sys.argv[3])
outputfolderpath = os.getcwd()
for cwd, dirnames, files in os.walk(inputfolderpath):
	for filename in files:
		fileIn = open(cwd+"/"+filename).read()
		output = spell(fileIn,diction)
		newfilename = filename[:-3]+'_g15612dj.txt'
		os.chdir(outputfolderpath)
		newfile = open(newfilename,'w')
		newfile.write(output)
		newfile.close()