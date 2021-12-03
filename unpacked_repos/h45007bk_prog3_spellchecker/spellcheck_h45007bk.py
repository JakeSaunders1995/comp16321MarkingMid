
def main(words_filepath,input_filepath,output_filepath):
    stats_uppercase=0
    stats_punctuation=0
    stats_numbers=0
    stats_words=0
    stats_correct=0
    stats_misspelt=0

    punctuations=['?','!',',',':',';','-','(',')','[',']','{','}','\'','"','…'] #punctuation, not included dot . as ellipsis is counted as 3 dots in code, special check
    file=open(words_filepath)
    english_words=file.read().splitlines()
    file.close()

    file=open(input_filepath)
    maintext=file.read()+' '
    text_words=[]
    word=''
    dot_count=0 #count for consecutive dots when counting ellipsis as punctuation
    for char in maintext:
        if char=='.':
            dot_count+=1
        else:
            if dot_count==3: #ellipsis
                stats_punctuation+=1
                dot_count=0
            elif dot_count!=0:
                stats_punctuation+=dot_count
                dot_count=0

            if char.isupper():
                char=char.lower()
                word+=char
                stats_uppercase+=1
                
            elif char.isspace():
                if word.isalpha():
                    text_words.append(word)
                    stats_words+=1
                    word=''

            elif '0'<=char<='9':
                stats_numbers+=1

            elif char in punctuations:
                stats_punctuation+=1
            
            else:
                word+=char

    for word in text_words:
        if word in english_words:
            stats_correct+=1
        else:
            stats_misspelt+=1

    file=open(output_filepath,'w')
    file.write(username[1:]+'\n')
    file.write('Formatting ###################\n')
    file.write('Number of upper case letters changed: '+str(stats_uppercase)+'\n')
    file.write('Number of punctuation’s removed: '+str(stats_punctuation)+'\n')
    file.write('Number of numbers removed: '+str(stats_numbers)+'\n')
    file.write('Spellchecking ###################\n')
    file.write('Number of words in file: '+str(stats_words)+'\n')
    file.write('Number of correct words in file: '+str(stats_correct)+'\n')
    file.write('Number of incorrect words in file: '+str(stats_misspelt)+'\n')
    file.close()

#---------

#to iterate over txt files in a directory, (non recusrively)
#or just files if given paths to files

import argparse, os
parser=argparse.ArgumentParser(description="Script to spellcheck and gather statistics on a file")
parser.add_argument('word_path',type=str,help="Path to file containing english words")
parser.add_argument('input_path',type=str,help="Input path to file or folder")
parser.add_argument('output_path',type=str,help="Output path to file or folder")

args=parser.parse_args()

username='_h45007bk'

def dir_txtlist(dirpath):
	f_list=[]
	for f_obj in os.scandir(dirpath):
		if f_obj.is_file(follow_symlinks=True):
			f_list.append(f_obj.path)
	return f_list

if not os.path.exists(args.input_path):
	print("Error: cannot access or find the input path at this time.")
	exit()

if os.path.isdir(args.input_path):
	if not os.path.exists(args.output_path):
		os.makedirs(args.output_path)
	if os.path.isdir(args.output_path):
		fin_lst=dir_txtlist(args.input_path)
		for fileout in fin_lst:
			fout=os.path.join(args.output_path,os.path.basename(fileout))
			ext_i=fout.rfind('.')
			fout=fout[:ext_i]+username+fout[ext_i:]
			fin=os.path.join(args.input_path,os.path.basename(fileout))
			main(args.word_path, fin, fout)
	else:
		print('Error: output path must be to a directory if the input path is also to a directory')
		exit()
elif os.path.isfile(args.input_path):
	if os.path.isdir(args.output_path):
		fout=os.path.join(args.output_path,os.path.basename(args.input_path))
		ext_i=fout.rfind('.')
		fout=fout[:ext_i]+username+fout[ext_i:]
		main(args.word_path, args.input_path, fout)
	elif os.path.isfile(args.output_path) or (not os.path.exists(args.output_path)):
		main(args.word_path, args.input_path, args.output_path)

else:
	print("Error: provided path(s) are not to a file or directory")
	exit()