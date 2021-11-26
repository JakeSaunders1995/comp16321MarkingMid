import argparse
import os


parser=argparse.ArgumentParser()
parser.add_argument('inputfile',type=str)
parser.add_argument('outputfile',type=str)
args=parser.parse_args()

scores={'t':5,'c':2,'p':3,'d':3}

input_folder=args.inputfile+'/'
output_folder=args.outputfile+'/'

for filename in os.listdir(input_folder):
    T1=0
    T2=0
    infile_address = input_folder+filename
    outfile_address = output_folder+filename[:-4]+'_b12745nd.txt'
    if '.txt' in filename:
        infile_handle = open(infile_address)
        outfile_handle = open(outfile_address,'w')
        for z in (infile_handle.read().split('T')[1:]):
            if z[0]=='1':
                T1+=scores[z[1]]
            else:
                T2+=scores[z[1]]
        outfile_handle.write(str(T1))
        outfile_handle.write(':')
        outfile_handle.write(str(T2))
        infile_handle.close()
        outfile_handle.close()
        

    


