import os,argparse,re

argv = argparse.ArgumentParser()
argv.add_argument("a")
argv.add_argument("b")
argv_list = argv.parse_args()

f = open(argv_list.a,'r')
content = f.read()
flag = 0
score_1 = 0
score_2 = 0
t_1 = content.count("T1t")
c_1 = content.count("T1c")
p_1 = content.count("T1p")
d_1 = content.count("T1d")
t_2 = content.count("T2t")
c_2 = content.count("T2c")
p_2 = content.count("T2p")
d_2 = content.count("T2d")
score_1 = (t_1 * 5) + (c_1 * 2) + (p_1 * 3) + (d_1 * 3)
score_2 = (t_2 * 5) + (c_2 * 2) + (p_2 * 3) + (d_2 * 3)
with open(argv_list.b,"w") as f:
    text = f.write(str(score_1)+":"+str(score_2))
f.close()
