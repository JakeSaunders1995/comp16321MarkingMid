wordDirectory = str(sys.argv[1])
source = str(sys.argv[2])
destination = str(sys.argv[3])
sourceFiles = os.listdir(source)

invalidChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '"', "'", '@', '!', '&', '*', '(', ')', '_', '-', '+',
'=', '{', '}', ':', ';', '#', ',', '.', '?', '\', "/"]

i = 0
while(i < len(sourceFiles)):
    file = open(source + sourceFiles[i])
    content = file.read()



    i += 1
