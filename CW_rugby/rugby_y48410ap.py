import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
parser = parser.parse_args()

input_folder = parser.input + '/'
output_folder = parser.output + '/'


for input_file in os.scandir(input_folder):
    input_file = input_file.path
    
    output_file = open(output_folder + os.path.basename(input_file)[:-4] + "_y48410ap.txt", 'w')
    input_file = open(input_file, 'r')
    
    text = input_file.read()
    text = text.split('T')
    text.pop(0)

    t = [0, 0]
    def evaluate_point(c):
        if c == 't':
            return 5
        elif c == 'c': 
            return 2
        elif c == 'd' or c == 'p':
            return 3

    for point in text:
        t[ int(point[0]) - 1 ] += evaluate_point(point[1])

    output_file.write(str(t[0]) + ':' + str(t[1]))

    input_file.close()
    output_file.close()