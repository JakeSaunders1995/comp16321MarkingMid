# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os


def getScore():
    """获取指定文件夹下的txt文件并解析文件中的字符串统计得分，结果输出到指定的文件中

    """
    print("please input data dir  \n")
    dataDir = input()
    print("please input score out file \n")
    dirPath = input()
    for root, dirs, files in os.walk(dataDir):
        # 遍历所有文件
        for file in files:
            # 只获取文件名后缀为.txt的文件
            if os.path.splitext(file)[1] == '.txt':  # 想要保存的文件格式
                # 使用open方法打开文件r表示读取文件(w为写入文件)
                f = open(root + "/" + file, 'r')
                # 读取文件内容，字符串放入到scores变量中
                scores = f.read()
                # 统计各个字符串出现的次数
                t1 = scores.count('T1t')
                c1 = scores.count('T1c')
                p1 = scores.count('T1p')
                d1 = scores.count('T1d')
                t2 = scores.count('T2t')
                c2 = scores.count('T2c')
                p2 = scores.count('T2p')
                d2 = scores.count('T2d')
                # 累计得分
                T1 = (t1) * 5 + (c1) * 2 + (p1) * 3 + (d1) * 3
                T2 = (t2) * 5 + (c2) * 2 + (p2) * 3 + (d2) * 3
                #关闭文件
                f.close()
                if not os.path.exists(dirPath):
                        os.makedirs(dirPath)
                    # 以写的方式打开文件f为文件句柄
                with open(dirPath+"/"+file, "w") as f:
                        # 写入得分
                    text = f.write(str(T1) + ":" + str(T2))
   


    
    


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    getScore()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
