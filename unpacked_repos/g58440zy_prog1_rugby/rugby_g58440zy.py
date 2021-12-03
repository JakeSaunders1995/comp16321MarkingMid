import sys
import os

def listdir_nohidden(path): 
    for f in os.listdir(path): 
        if not f.startswith('.'): 
            yield f 
  
def main():
    inputPath=sys.argv[1]
    outputPath=sys.argv[2]
    filesPath=listdir_nohidden(inputPath)
    for i in filesPath:
        file_object = open(inputPath+'/'+i)
        line = file_object.readlines()
        x=i[:-4]
        T1 = 0
        T2 = 0
        for n in range(0,len(line[0])):
            if line[0][n:n+2] == 'T1':
                letter = line[0][n+2]
                if letter == 't':
                    T1 += 5
                elif letter == 'c':
                    T1 += 2
                elif letter == 'p':
                    T1 += 3
                elif letter == 'd':
                    T1 +=3
            elif line[0][n:n+2] == 'T2':
                letter = line[0][n+2]
                if letter == 't':
                    T2 += 5
                elif letter == 'c':
                    T2 += 2
                elif letter == 'p':
                    T2 += 3
                elif letter == 'd':
                    T2 +=3
        output_object=open(outputPath+'/'+x+'_g58440zy.txt','w+')
        output_object.write(f'{T1}:{T2}')
if __name__ == '__main__':
	main()





