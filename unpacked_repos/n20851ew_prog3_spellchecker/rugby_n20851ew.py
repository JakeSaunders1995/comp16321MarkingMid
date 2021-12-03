import argparse
import sys
import os

filein = sys.argv[1]
fileout = sys.argv[2]

for filename in os.listdir(filein): 
    g = os.path.join(filein, filename)
    if os.path.isfile(g):
        filr = open(g, 'r')
        filen = os.path.basename(g)
        sfn = os.path.splitext(filen)[0]
        if  os.path.isdir(fileout):

            dname = os.path.join(fileout, sfn + "_n20851ew.txt")
            fn = open(dname, 'a')
            text = filr.read()
            
            t1_t = text.count("1t")
            t1_c = text.count("1c")
            t1_p = text.count("1p")
            t1_d = text.count("1d")
            
            t2_t = text.count("2t")
            t2_c = text.count("2c")
            t2_p = text.count("2p")
            t2_d = text.count("2d")
            
            T1 = (t1_t * 5) + (t1_c * 2) + (t1_p * 3) + (t1_d * 3)
            
            T2 = (t2_t * 5) + (t2_c * 2) + (t2_p * 3) + (t2_d * 3)
            

            
            fn.write(str(T1) + ":" + str(T2))
        else:
            os.mkdir(fileout)