# -*- coding: utf-8 -*-
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Path')
    parser.add_argument('inputpath', type=str, help='input file path')
    parser.add_argument('outputpath', type=str, help='output file path')
    args = parser.parse_args()

    InputPath = args.inputpath
    OutputPath = args.outputpath
    path_1 = InputPath
    path_2 = OutputPath
    count1 = 0
    count2 = 0
    dic = {'t':5,'c':2,'p':3,'d':3} 
    try:
        with open(path_1) as fp:
            data =fp.read()
            index = data.find("T1")
            while  index != -1:
                res = data[index + 2]
                if res not in dic.keys():
                    raise 
                count1 += dic[res]
                index = data.find("T1", index + 1)
            
            index = data.find("T2")
            while  index != -1:
                res = data[index + 2]
                if res not in dic.keys():
                    raise
                count2 += dic[res]
                index = data.find("T2", index + 1)
    except:
        print("Wrong Input")
    
    with open(path_2,'w+') as fp:
        fp.write("{}:{}".format(count1,count2))
