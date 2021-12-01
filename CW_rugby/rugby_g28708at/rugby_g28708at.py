import sys, os

inputoutput = sys.argv
print(inputoutput[1:])

#input/output should be the whole dir including root 
inpath = sys.argv[1]
outpath = sys.argv[2]

os.chdir(inpath)

def read_text_file(file_path):
    with open(file_path, 'r') as f:
    	scoreDict = {
    	"t" : 5,
    	"c" : 2,
    	"p" : 3,
    	"d" : 3
    	}
    	sepdata = []
    	data = f.read()
    	for i in range(0, len(data), 3):
       		sepdata.append(data[i : i + 3])

    	T1 = 0
    	T2 = 0
    	for i in sepdata:
    		if i[0:2] == 'T1':
    			T1 += scoreDict[i[2]]
    		else:
    			T2 += scoreDict[i[2]]
    res = f'{T1} : {T2}'
    return res
    	
for file in os.listdir():
	if file.endswith(".txt"):
	    file_path = f"{inpath}/{file}"
	    res = read_text_file(file_path)
	    os.chdir(outpath)
	    f = open(f'{file} output', "w")
	    f.write(res)




	    
