import argparse
import os


n = 1 # output in filename(n) in the loop

parser = argparse.ArgumentParser()
parser.add_argument('folder1')
parser.add_argument('folder2')
args = parser.parse_args()
folder_1 = args.folder1
folder_2 = args.folder2
a = os.listdir(folder_1)
a.sort(key = lambda x:int(x[-5:-4]))
os.chdir(folder_1)
for item in a:
    file = open(item, 'r')
    text = file.readline()

    list = text.split("T")
    list.pop(0)

    t1_score_way = []
    t2_score_way = []
    for element in list:
        if "1" in element:
            t1_score_way.append(element)
        else:
            t2_score_way.append(element)


    def calculate_t1_score():
        t1_total = 0
        for a in t1_score_way:
            if 't' in a:
                t1_total = t1_total + 5
            elif 'c' in a:
                t1_total = t1_total + 2
            elif 'p' in a:
                t1_total = t1_total + 3
            else:
                t1_total = t1_total + 3
        return t1_total


    def calculate_t2_score():
        t2_total = 0
        for a in t2_score_way:
            if 't' in a:
                t2_total = t2_total + 5
            elif 'c' in a:
                t2_total = t2_total + 2
            elif 'p' in a:
                t2_total = t2_total + 3
            else:
                t2_total = t2_total + 3
        return t2_total

    t1 = calculate_t1_score()
    t2 = calculate_t2_score()
    print(str(t1) + ":" + str(t2))

    pardir = os.path.abspath(os.path.join(os.path.dirname(folder_1),os.path.pardir))
    # print(os.listdir(pardir))
    # b = os.listdir(folder_2)
    os.chdir(pardir)
    os.chdir(folder_2)
    f = open(("%s%d_m50747jh.txt") %(item[:-5], n) , "w+")
    f.write(str(t1) + ":" + str(t2))
    f.close()
    n += 1

    pardir2 = os.path.abspath(os.path.join(os.path.dirname(folder_2),os.path.pardir))
    # print(pardir2)
    os.chdir(pardir2)
    os.chdir(folder_1)

# with open(args.filename2, "wt") as f:
#     f.write(str(t1) + ":" + str(t2))
