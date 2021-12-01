import sys
import os
input_folder = sys.argv[1]
output_folder = sys.argv[2]
input = os.path.realpath(input_folder)
sum = os.listdir(input)
for i in sum:
    scoring = open(input + "/" + i, 'r')
    x = scoring.read()
    scoring.close()
    list = []
    def split_text(text,length):
        tmp = text[0:int(length)]
        list.append(tmp)
        text = text[3:]
        if len(text) < length + 1:
            list.append(text)
        else:
            split_text(text, length)
        return list

    split_text(x, 3)

    def compareS1(text):
        if text == 'T1t':
            score1 = 5
        elif text == 'T1p' or text == 'T1d':
            score1 = 3
        elif text == 'T1c':
            score1 = 2
        else:
            score1 = 0
        return int(score1)

    def compareS2(text):
        if text == 'T2t':
            score2 = 5
        elif text == 'T2p' or text == 'T2d':
            score2 = 3
        elif text == 'T2c':
            score2 = 2
        else:
            score2 = 0
        return int(score2)

    total1 = 0
    total2 = 0
    for aa in list:
        total1 += compareS1(aa)
        total2 += compareS2(aa)
    value = ("%s:%i" % (total1, total2))
    output = os.path.realpath(output_folder)
    name = os.path.basename(i)
    name1 = name.replace(".txt", "_q83438yw.txt")
    outcome = open(os.path.join(output, name1), 'w')
    s = str(value)
    outcome.write(s)
    outcome.close()



