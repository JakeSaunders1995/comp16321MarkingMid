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
morsecode = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-', ';':'-.-.-.', ':':'---...', "'":'.----.', '"':'.-..-.','_':'..--.-', '!':'-.-.--'}

files_and_directories = os.listdir("input_folder")
sortedfiles = sorted(files_and_directories)
print(sortedfiles)
j=0
k=0
l=0
length=0

allcontent=""

for filename in sortedfiles:
    with open(os.path.join("input_folder", filename),'r') as f:
    	with open(filename,"r") as stripping:
    		string_without_line_breaks=""
	    	for line in stripping:
	    		stripped_line = line.rstrip()
	    		string_without_line_breaks +=stripped_line
	    		#print(string_without_line_breakss)
    	with open(filename, "a") as newline:
	        newline.write("\n\n")
	        rd = f.read()
	        content = str(rd)
	        allcontent+=content 
	        print(len(rd))
	        count =0
	        while count<len(rd):
		        if (rd[count]!="\n\n"):
		        	count=count+1
		        else:
		        	break 
	        '''with open(os.path.join("input_folder", filename),'r') as f:
	        	allcontent=f.read()
	        	length += len(allcontent)
	        	print(len(allcontent))'''

	        #print(rd)
	        #print(j)
    #print(len(content))
    print(list(allcontent))
    if k<len(allcontent):
	    if (allcontent[j]=="H" or allcontent[k]=="H" or allcontent[l]=="H"):
	    	print("hex")
	    	i=0
	    	while i<count:
	    		if (allcontent[i]==":"):
	    			code= "".join(allcontent[i+1:count])
	    			break
	    		else:
	    			i = i+1
	    	print(code)
	    	ans  = bytes.fromhex(code)
	    	ans = ans.decode()
	    	output = ans 
	    	print(ans)
    if (allcontent[j]=="C" or allcontent[k]=="C" or allcontent[l]=="C"):
	    	content=list(rd)
	    	print(content)
	    	i=0
	    	while i<len(content):
	    		if (content[i]==":"):
	    			break
	    		else:
	    			i = i+1
	    	print(i)
	    	ASCIIValue = str("VWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEF")
	    	ctposition = i+1
	    	encrypted=''
	    	while (ctposition< len(content)-1):
	    		ctchar = content[int(ctposition)]
	    		if (ctchar != " "):
	    			ASCIIValue = ord(ctchar)
	    			ASCIIValue = ASCIIValue - 3
	    			encrypted = encrypted + chr(ASCIIValue)
	    			ctposition = ctposition +1
	    		else:
	    			encrypted = encrypted + " "
	    			ctposition = ctposition +1
	    	i=0
	    	encrypted=list(encrypted)
	    	while (i<len(encrypted)):
	    		if encrypted[i]=="`":
	    			encrypted[i] = "z"
	    		if encrypted[i]=="_":
	    			encrypted[i] ="y"
	    		if encrypted[i]=="^":
	    			encrypted[i] ="x"
	    		else:
	    			i+=1
	    	encrypted=''.join(encrypted)
	    	print(encrypted)
	    	output = encrypted
    if k<len(allcontent):
	    if (allcontent[j]=="M" or allcontent[k]=="M" or allcontent[l]=="M"):
	    	content = list(rd)
	    	print("morsecode")
	    	i=0
	    	while i<len(content):
	    		if (content[i]==":"):
	    			code= "".join(content[i+1:count])
	    			print(code)
	    			break
	    		else:
	    			i = i+1
	    		cryptedtxt = ''
	    		decryptedtxt = ''
	    		code = code + " "
	    		for character in code:
	    			if (character != " " and character != "/"):
	    				cryptedtxt = cryptedtxt + character
	    				i=0
	    				print(cryptedtxt)
	    			else:
	    				i = i+1
	    				print(cryptedtxt)
	    				if (character=="/"):
	    					decryptedtxt = decryptedtxt + " "
	    				else:
	    					i=0
	    					while i<len(cryptedtxt):
	    						for letter, code in morsecode.items():
	    							if code == cryptedtxt:
	    								decryptedtxt = decryptedtxt + letter
	    								cryptedtxt = cryptedtxt[len(cryptedtxt):count]
	    								i = i+len(code)
	    	print(decryptedtxt.lower())
	    	output = decryptedtxt.lower() 

    j=count
    k=j+count
    l=k+count+count-2
    os.path.splitext(filename)
    filename = os.path.splitext(filename)[0]
    print(filename)
    with open(filename+"_n66837sm.txt", "w") as f:
        f.write(output)
        filename = filename+"_n66837sm.txt"
        change = shutil.move(filename, 'output_folder')

    #print(j)
#print(len(allcontent))	       
