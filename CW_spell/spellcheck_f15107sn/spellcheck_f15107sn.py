import argparse

def read_file(in_file):
    in_f= open(in_file,'r')
    txt= in_f.read() # read file
    in_f.close()
    return txt

def format_text(txt_file):
    # remove no from the txt_file
    n_cnt,n_punc,n_upcase= 0,0,0
    tmp_file= str(txt_file) # make a copy of the tmp_file
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for txt in tmp_file:
        if txt.isdigit(): #removing the digits
            tmp_file= tmp_file.replace(txt,'')
            n_cnt+=1

        if txt in punc: #removing the punctuations
            tmp_file = tmp_file.replace(txt, '')
            n_punc+=1

        if txt.isupper():
            tmp_file = tmp_file.replace(txt,txt.lower())
            n_upcase+=1
    return [tmp_file,n_cnt,n_punc,n_upcase]


def check_file(txt_file,dictionary):
    # open and read the dictionary
    tmp_file= open(dictionary,'r')
    w_dictionary= tmp_file.readlines() # read all the lines from the dictionary

    #stripping "\n" from the dictionary
    for i, d in enumerate(w_dictionary):
        w_dictionary[i] = d.strip()

    # total words in the txt in_file
    w_tot= len(txt_file.split()) # total words

    c_wc,i_wc= 0,0

    for txt in txt_file.split():
        if txt in w_dictionary:
            c_wc+=1
        else:
            i_wc+=1

    return [w_tot,c_wc,i_wc]



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encryption Decryption')
    parser.add_argument('dictionary', type=str, help='English Dictionary')
    parser.add_argument('in_file', type=str, help='Input file')
    parser.add_argument('out_file', type=str, help='Output file')
    args = parser.parse_args()
    username= parser.prog

    # 2.Read in a .txt file containing a string of text:
    txt_content= read_file(args.in_file)

    # 3.formatting the text read
    formated_txt,n_cnt,n_punc,n_upcase= format_text(txt_content)

    # 4. Splitting and checking spellings
    w_tot,c_wc,i_wc= check_file(formated_txt,args.dictionary)

    # Dumping the values to the file
    fp= open(args.out_file,'w')
    fp.write(username.split('_')[1].split('.')[0] + "\n")
    fp.write("Formatting ################### \n")
    fp.write("Number of upper case words changed: "+ str(n_upcase) + '\n')
    fp.write("Number of punctuations removed: "+ str(n_punc) + '\n')
    fp.write("Number of numbers removed: "+ str(n_cnt) + '\n')
    fp.write("Spellchecking ################### \n")
    fp.write("Number of words: "+ str(w_tot) + '\n')
    fp.write("Number of correct words: "+ str(c_wc) + '\n')
    fp.write("Number of incorrect words: "+ str(i_wc) + '\n')
    fp.close()