import argparse
import os
import re

Pstring = '!"$%\'()*+,-./:;<=>?[\\]^_`{|}~—…'
 
parser = argparse.ArgumentParser()
parser.add_argument('english_dictionary', type=str, help = 'Enter dictionary path')
parser.add_argument('input_file', type=str, help = 'Enter input file path')
parser.add_argument('output_file', type=str, help = 'Enter input file path')
args = parser.parse_args()

eng_words=args.english_dictionary
input_file=args.input_file
output_file=args.output_file

files = os.listdir(input_file)
eng=open(eng_words,"r").read()
eng=eng.split()


for y in files:
    
    upper=0
    number=0
    symbol=0
    correct=0
    incorrect=0
    in_put=open(os.path.join(input_file,y)).read().split()

    for x in in_put:

        for z in x:
    
            if z in Pstring:
                symbol += 1
                x = re.sub('[!"$%\'()*+,-./:;<=>?\[\\]^_`{|}~—…]',"",x)

            elif z.isupper():
                upper += 1
                i = in_put.index(x)
                x = x.lower()
                
                in_put[i] = x

            elif z.isdigit():
                number += 1
                x = re.sub("[0-9]","",in_put)


        if x in eng:
            correct += 1

        else:
            incorrect += 1

    n_file=re.split("[.]",y)[0] + "_f66089ms.txt"
    result=open(os.path.join(output_file,n_file),"w")
    result.write("f66089ms\n")
    result.write("Formatting ###################\n")
    result.write("Number of upper case words changed: " + str(upper))
    result.write("\nNumber of punctuations removed: " + str(symbol))
    result.write("\nNumber of numbers removed: " + str(number))
    result.write("\nSpellchecking ###################")
    result.write("\nNumber of words: " + str(correct+incorrect))
    result.write("\nNumber of correct words: " + str(correct))
    result.write("\nNumber of incorrect words: " + str(incorrect))
    result.close()





        

