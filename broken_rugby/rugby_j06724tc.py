import sys, os
a = sys.argv[1]
b = os.listdir(a)
for c in b:
    d = a + "/" + c
    with open(d, 'r') as rugbyprogram:
        rugbyprogram = rugbyprogram.read()
        t1score = 0
        t2score = 0
        i = 0
        while i < len(rugbyprogram):
            if rugbyprogram[i] == "T":
                i += 1
                if rugbyprogram[i] == "1":
                    i += 1
                    if rugbyprogram[i] == "t":
                        t1score += 5
                        i += 1
                    elif rugbyprogram[i] == "c":
                        t1score += 2
                        i += 1
                    elif rugbyprogram[i] == "p":
                        t1score += 3
                        i += 1
                    elif rugbyprogram[i] == "d":
                        t1score += 3
                        i += 1
                    else:
                        break
                elif rugbyprogram[i] == "2":
                    i += 1
                    if rugbyprogram[i] == "t":
                        t2score += 5
                        i += 1
                    elif rugbyprogram[i] == "c":
                        t2score += 2
                        i += 1
                    elif rugbyprogram[i] == "p":
                        t2score += 3
                        i += 1
                    elif rugbyprogram[i] == "d":
                        t2score += 3
                        i += 1
                    else:
                        break
                else:
                    break
        output = str(t1score) + ":" + str(t2score)
    e = c.replace('.txt','')
    f = sys.argv[2] + "/" + e + "_j06724tc" + ".txt"
    g = open(f, 'w')
    g.write(output)
