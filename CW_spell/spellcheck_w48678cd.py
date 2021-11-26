import argparse,re,os,sys

parser = argparse.ArgumentParser()
parser.add_argument(dest='argument1', help="This is the English word file")
parser.add_argument(dest='argument2', help="This is the Input folder")
parser.add_argument(dest='argument3', help="This is the Output folder")
args = parser.parse_args()
Filewords=args.argument1
FolderInput=args.argument2
FolderOutput=args.argument3

def Format(texts):
	global num_uppers,num_nums,num_puncs
	uppers=re.findall(r'[A-Z]',texts)
	nums=re.findall(r'[0-9]',texts)
	puncs=re.findall(r'[^\w\s]',texts)
	while "_" in texts:
		puncs.append("_")
		texts = texts.replace("_", "", 1)
	num_uppers=len(uppers)
	num_nums=len(nums)
	num_puncs=len(puncs)
	OnePara=re.sub(r'[\n]'," ",texts)
	noNum=re.sub(r'[0-9]',"",OnePara)
	noPun=re.sub(r'[^\w\s]',"",noNum)
	Formatedtext=noPun.lower()
	words=Formatedtext.split(" ")
	while "" in words:
		words.remove("")
	return words
def Check():
	global num_correct,num_incorrect
	for n in range(0,num_words):
		found=False
		for line in dictionary:
			if (checks[n]==line.strip()):
				num_correct=num_correct+1
				found=True
				break
		if found==False:
			num_incorrect=num_incorrect+1
		dictionary.seek(0)
def Write():
	Outfname=os.path.basename(FileInput)
	filename, file_extension = os.path.splitext(Outfname)
	fname=filename+"_w48678cd"+file_extension
	filepath = os.path.join(FolderOutput, fname)
	outFile=open(filepath,"w")
	outFile.write(	"w48678cd\n"
					"Formatting ###################\n"+
					"Number of upper case letters changed: "+str(num_uppers)+"\n"+
					"Number of punctuations removed: "+str(num_puncs)+"\n"+
					"Number of numbers removed: "+str(num_nums)+"\n"+
					"Spellchecking ###################"+"\n"+
					"Number of words: "+str(num_words)+"\n"+
					"Number of correct words: "+str(num_correct)+"\n"+
					"Number of incorrect words: "+str(num_incorrect)
					)
	outFile.close()


for FileInput in os.listdir(FolderInput):
	In_fname=os.path.basename(FileInput)
	In_filepath = os.path.join(FolderInput, In_fname)

	fileIn, extension = os.path.splitext(FileInput)

	enFile=open(In_filepath,"r")
	raw=enFile.read()
	raw=raw.strip()
	enFile.close()

	num_correct=0
	num_incorrect=0
	checks=Format(raw)
	num_words=len(checks)
	found_words=[]

	dictionary=open(Filewords,"r")
	Check()
	dictionary.close()
	Write()


