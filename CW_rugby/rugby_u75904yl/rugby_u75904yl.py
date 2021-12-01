import os
import sys
filenames = os.listdir(sys.argv[1])
for filename in filenames:
    file = open(sys.argv[1]+"/"+filename, "rb")
    first = file.read().decode('ISO-8859-1')
    team1 = []
    team2 = []
    points1 = []
    points2 = []
    T1t = (first.count("T1t"))
    T1d = (first.count("T1d"))
    T1c = (first.count("T1c"))
    T1p = (first.count("T1p"))
    team1.append(T1t)
    team1.append(T1d)
    team1.append(T1c)
    team1.append(T1p)
    t1t = 5 * team1[0]
    points1.append(t1t)
    t1d = 3 * team1[1]
    points1.append(t1d)
    t1c = 2 * team1[2]
    points1.append(t1c)
    t1p = 3 * team1[3]
    points1.append(t1p)
    T2t = (first.count("T2t"))
    T2d = (first.count("T2d"))
    T2c = (first.count("T2c"))
    T2p = (first.count("T2p"))
    team2.append(T2t)
    team2.append(T2d)
    team2.append(T2c)
    team2.append(T2p)
    t2t = 5 * team2[0]
    points2.append(t2t)
    t2d = 3 * team2[1]
    points2.append(t2d)
    t2c = 2 * team2[2]
    points2.append(t2c)
    t2p = 3 * team2[3]
    points2.append(t2p)
    total1 = sum(points1)
    total2 = sum(points2)
    final =  str(total1) + ":" + str(total2)
    file = open(sys.argv[2] + "/" + filename[:-4] + "_u75904yl.txt", "w")
    file.write(str(final))
    file.close()