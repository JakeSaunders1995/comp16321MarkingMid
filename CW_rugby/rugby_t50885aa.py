import argparse
import os
import codecs
def score_counter(s):

    i=1
    t1s=0
    t2s=0
    while i < len(s):
        if s[i]=='1':
            if s[i+1]=='t':
                t1s=t1s+5
            if s[i+1]=='c':
                t1s=t1s+2
            if s[i+1]=='p':
                t1s=t1s+3
            if s[i+1]=='d':
                t1s=t1s+3
        if s[i]=='2':
            if s[i+1]=='t':
                t2s=t2s+5
            if s[i+1]=='c':
                t2s=t2s+2
            if s[i+1]=='p':
                t2s=t2s+3
            if s[i+1]=='d':
                t2s=t2s+3
        i=i+3

    return (str(t1s)+":"+str(t2s))
if __name__=="__main__":
	f=argparse.ArgumentParser()
	f.add_argument('input')
	f.add_argument('output')
	args = f.parse_args()
	s=str(args.input)
	outs=str(args.output)
	tfile=os.listdir(s)
	tfile.sort()
	for path in tfile:
		fname= os.path.join(s,path)
		tpos=path.find(".txt")
		outputf=path[0:tpos]
		with codecs.open(fname, 'r', encoding='utf-8',errors='ignore') as infile:
		  s_in=infile.read()
		  output=score_counter(s_in)
		  with open(os.path.join(outs,f'{outputf}_t50885aa.txt'),"w") as w:
		       print(outs)
		       w.write(output)
