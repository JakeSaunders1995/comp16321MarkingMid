import os
import os.path
import shutil
def find_and_open(filename):
    for rf, folders, files in os.walk('.'):
        if filename in files:
            with open(rf + '/' + filename) as f:
            	f.read()
def create_and_write(filename):
    for rf, folders, files in os.walk('.'):
        if filename in files:
            with open(rf + '/' + filename) as w:
            	w.write()

files_and_directories = os.listdir("input_folder")
sortedfiles = sorted(files_and_directories)

for filename in sortedfiles:
    with open(os.path.join("input_folder", filename),'r') as f:
        with open(filename, "a") as newline:
	        newline.write("\n")
	        rd = f.read()
	        count =0
	        while count<len(rd):
		        if (rd[count]!="\n"):
		        	count=count+1
		        else:
		        	break
	        T1 = 0
        	T2 = 0
        	lt = list(rd)
       		i=0
        	while i<count:
        		if(lt[i]=="1"):
        			if(lt[i+1]=="t"):
        				T1 = T1 + 5
        			if(lt[i+1]=="c"):
        				T1 = T1 + 2
        			if(lt[i+1]=="p"):
        				T1 = T1 + 3
        			if(lt[i+1]=="d"):
        				T1 = T1 + 3
        			i=i+1
        		elif(lt[i]=="2"):
        			if(lt[i+1]=="t"):
        				T2 = T2 + 5
        			if(lt[i+1]=="c"):
        				T2 = T2 + 2
        			if(lt[i+1]=="p"):
        				T2 = T2 + 3
        			if(lt[i+1]=="d"):
        				T2 = T2 + 3
        			i=i+1
        		else:
        			i=i+1
        	output = str(T1)+":"+str(T2)
        	print(output)
        	print(filename)
        	os.path.splitext(filename)
        	filename = os.path.splitext(filename)[0]
        	print(filename)
        	with open(filename+"_n66837sm.txt", "w") as f:
        		f.write(output)
        		filename = filename+"_n66837sm.txt"
        		change = shutil.move(filename, 'output_folder')
        	
        	
