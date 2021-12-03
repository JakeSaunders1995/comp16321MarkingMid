import argparse
import re


def read_file(in_file):
    in_f = open(in_file, 'r')
    txt = in_f.readline()  # read the first line
    in_f.close()
    return txt


def determine_scores(txt,points):
    T1= []
    T2= []
    T1_POINTS,T2_POINTS=0,0
    teams_scores= re.findall('...',txt)

    for point in teams_scores:
        if point[0:-1] == 'T1':
            T1.append(point[-1])
        else:
            T2.append(point[-1])

    for i in T1:
        T1_POINTS+= points[i]

    for i in T2:
        T2_POINTS+= points[i]

    return [T1_POINTS,T2_POINTS]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Game of Rugby')
    parser.add_argument('in_file', type=str, help='Input file')
    parser.add_argument('out_file', type=str, help='Output file')
    args = parser.parse_args()

    txt_content = read_file(args.in_file)

    points_dictionary = {
        't': 5,
        'c': 2,
        'p': 3,
        'd': 3
    }

    T1_POINTS,T2_POINTS= determine_scores(txt_content, points_dictionary)


    out_file= open(args.out_file,'w')
    out_file.write(str(T1_POINTS) + ':' + str(T2_POINTS))
    out_file.close()
