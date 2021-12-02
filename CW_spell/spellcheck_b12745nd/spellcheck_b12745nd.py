import argparse
import os


punctuations = ['?', '!', ',', ':', ';', '-', '–', '(', ')', '{', '}', '[',
                ']', '\'', '"', '...', '.' ]


parser = argparse.ArgumentParser()
parser.add_argument('english_words',type=str)
parser.add_argument('inputfile', type=str)
parser.add_argument('outputfile', type=str)
args = parser.parse_args()


input_folder = args.inputfile+'/'
output_folder = args.outputfile+'/'
english_words = open(args.english_words).read().split('\n')

for filename in os.listdir(input_folder):
    infile_address = input_folder+filename
    outfile_address = output_folder+filename[:-4]+'_b12745nd.txt'
    if '.txt' in filename:
        no_of_upper=0
        no_of_punctuations=0
        no_of_numbers=0
        no_of_words=0
        no_of_wrong_words=0
        formatted_string=''
        infile_handle = open(infile_address)
        outfile_handle = open(outfile_address, 'w')
        for i in infile_handle.read():
            if i.isnumeric():
                no_of_numbers+=1
            elif i in punctuations:
                no_of_punctuations+=1
            elif i.isupper():
                no_of_upper+=1
                formatted_string+=i.lower()
            else:
                formatted_string+=i
        formatted_string=formatted_string.split()
        no_of_words = len(formatted_string)
        for i in formatted_string:
            if i not in english_words:
                no_of_wrong_words+=1
        no_of_correct_words = no_of_words-no_of_wrong_words
        write_lines=['b12745nd'+'\n', 'Formatting ###################'+'\n',
            'Number of upper case letters changed:'+str(no_of_upper)+'\n',
            'Number of punctuations removed:'+str(no_of_punctuations)+'\n',
            'Number of numbers removed:'+str(no_of_numbers)+'\n',
            'Spellchecking ###################'+'\n',
            'Number of words:'+str(no_of_words)+'\n',
            'Number of correct words:'+str(no_of_correct_words)+'\n',
            'Number of incorrect words:'+str(no_of_wrong_words)]
        outfile_handle.writelines(write_lines)
        outfile_handle.close()
        infile_handle.close()







      
