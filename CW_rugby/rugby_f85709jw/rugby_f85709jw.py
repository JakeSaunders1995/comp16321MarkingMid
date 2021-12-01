import sys
import os

user = 'f85709jw'

inputPath = sys.argv[1]
outputPath = sys.argv[2]

points =   {"t": 5,
            "c": 2,
            "p": 3,
            "d": 3}


def main():
    for inp in os.listdir(inputPath):
        events = []
        score = {"T1": 0,
                "T2": 0}
        with open(inputPath + '/' + inp) as f:
            for line in f:
                events = [line[x:x+3] for x in range(0,len(line),3)]

        for event in events:
            score[event[0:2]] += points[event[2]]
        
        output = str(score["T1"]) + ":" + str(score["T2"])
        outputfile(output, inp)

def outputfile(output, inputName):
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    with open(outputPath + '/' + inputName[0:-4] + '_' + user + '.txt', "w") as f:
        f.write(output)

if __name__ == "__main__":
    main()