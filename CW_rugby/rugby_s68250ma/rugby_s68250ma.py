import argparse,os
parser = argparse.ArgumentParser()
parser.add_argument("input_dir")
parser.add_argument("output_dir")
args = parser.parse_args()
def rugbyScores(scores):
    T1 = 0
    T2 = 0
    for i in range(len(scores)):
        if(scores[i] == 't'):
            if(scores[i-1] == '1'):
                T1 += 5
            elif(scores[i-1] == '2'):
                T2 += 5
        elif(scores[i] == 'c'):
            if(scores[i-1] == '1'):
                T1 += 2
            elif(scores[i-1] == '2'):
                T2 += 2
        elif(scores[i] == 'p'):
            if(scores[i-1] == '1'):
                T1 += 3
            elif(scores[i-1] == '2'):
                T2 += 3
        elif(scores[i] == 'd'):
            if(scores[i-1] == '1'):
                T1 += 3
            elif(scores[i-1] == '2'):
                T2 += 3
    return str(T1) + ":" + str(T2)
if(os.path.isdir(args.input_dir)):
    for files in os.listdir(args.input_dir):
        inputFile = os.path.join(args.input_dir, files)
        outputFile = os.path.join(args.output_dir,str(files.replace(".txt","_s68250ma.txt")))
        with open(inputFile, 'r') as file:
            with open(outputFile, 'w') as file2:
                file2.write(rugbyScores(file.read()))
                
