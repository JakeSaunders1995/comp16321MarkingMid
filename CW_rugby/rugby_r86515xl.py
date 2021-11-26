def make_out(name, out):
    path1 = os.path.abspath(output_folder)
    path2 = path1 + '/' + name.replace('.txt','') + '_r86515xl' + '.txt'
    file = open(path2,'w')
    file.write(out)

def final_score(file):
    ot = len(re.findall(r'1t',file))
    oc = len(re.findall(r'1c', file))
    op = len(re.findall(r'1p', file))
    od = len(re.findall(r'1d', file))
    tt = len(re.findall(r'2t', file))
    tc = len(re.findall(r'2c', file))
    tp = len(re.findall(r'2p', file))
    td = len(re.findall(r'2d', file))
    T1 = 5 * ot + 2 * oc + 3 * op + 3 * od
    T2 = 5 * tt + 2 * tc + 3 * tp + 3 * td
    out = str(T1) + ':' + str(T2)
    return out


import sys,os,re
script, input_folder, output_folder = sys.argv
dirs = os.listdir(input_folder)
for file_name in dirs:
    path = os.path.abspath(input_folder)
    file = open(path + '/' + file_name,'r')
    file = file.read()
    out = final_score(file)
    make_out(file_name,out)
