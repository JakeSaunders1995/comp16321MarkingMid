import sys
import os
import argparse


INPUT_FOLDER = sys.argv[1]
OUTPUT_FOLDER = sys.argv[2]
DIRECTORY = os.listdir(INPUT_FOLDER)

for i in range(len(DIRECTORY)):
    file = open(INPUT_FOLDER + "/" + DIRECTORY[i])
    text = file.readline()

def calculate_scores(text):


    T1 = 0
    T2 = 0

    start = 0
    end = 3
    while start < len(text):
        
        team, point = text[start:end-1], text[end-1:end][0]

        if "T1" == team:
            if point == "t":
                T1 = T1 + 5
            if point == "c":
                T1 = T1 + 2
            if point == "p":
                T1 = T1 + 3
            if point == "d":
                T1 = T1 + 3
        if "T2" == team:
            if point == "t":
                T2 = T2 + 5
            if point == "c":
                T2 = T2 + 2
            if point == "p":
                T2 = T2 + 3
            if point == "d":
                T2 = T2 + 3
        
        start, end = start + 3, end + 3
    
    return (T1,T2)

if __name__ == "__main__":
    for i in range(0,len(DIRECTORY)):
        T1, T2 = calculate_scores(text)
        t = open(INPUT_FOLDER + "/" + DIRECTORY[i])
        text = t.readline()
        t.close()
        output_file = "test_file"+str(i+1)+"_p29365al.txt"
        output_file = OUTPUT_FOLDER + "/" + output_file
        with open (output_file, "a") as file:
            file.write(str(T1)+":"+str(T2))