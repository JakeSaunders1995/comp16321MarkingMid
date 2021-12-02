import os
import argparse
import re

# 执行命令：
# .\venv\Scripts\python.exe .\Descrypt\descrypt_u82766jh.py .\Descrypt\input\ .\Descrypt\output

# 解密
def descrypt(input_file, output_file):
    file1 = open(input_file, 'r')
    content = file1.read()
    check = 0
    if content[0] == "H":
        check = 1
    elif content[0] == "C":
        check = 2
    elif content[0] == "M":
        check = 3
    index = content.find(':') + 1
    content = content[index:]
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    codes = """.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-..
    -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
    .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"""
    DD = dict(zip(codes.split(), chars.lower()))
    i = 0

    def morse2chars(morse):
        return DD.get(morse, ' ')

    if check == 1:
        result = content.split()
        file2 = open(output_file, 'w')
        for i in range(0, len(result)):
            result[i] = int(result[i], 16)
            result[i] = chr(result[i])
            s = (re.sub(r"['{},]*", '', str(result[i]))).replace(':', ',')
            file2.write(s)
        file2.close
    if check == 2:
        flag = 0
        file2 = open(output_file, 'w')
        for i in range(0, len(content)):
            num = ord(content[i])
            if num == 32:
                s = (re.sub(r"['{},]*", '', str(chr(num)))).replace(':', ',')
                file2.write(s)
                continue
            num = num - 3
            if num <= 96:
                flag = 96 - num
                num = 120 - flag
            s = (re.sub(r"['{},]*", '', str(chr(num)))).replace(':', ',')
            file2.write(s)
        file2.close
    elif check == 3:
        result = content.split()
        file2 = open(output_file, 'w')
        for i in range(0, len(result)):
            if re.match('/', result[i]):
                file2.write(str(' '))
                continue
            else:
                ans = ''.join(morse2chars(result[i]))
            s = (re.sub(r"['{},]*", '', str(ans))).replace(':', ',')
            file2.write(s)
        file2.close


# 读取目录下所有的文件
def list_dir(start_dir):
    file_list = []
    dir_res = os.listdir(start_dir)
    for path in dir_res:
        temp_path = start_dir + path
        if os.path.isfile(temp_path):
            file_list.append(temp_path)
    return file_list


if __name__ == '__main__':
    argv = argparse.ArgumentParser()
    argv.add_argument("test_folder")
    argv.add_argument("target_folder")
    argv_list = argv.parse_args()

    # 获取所有文件列表
    test_file_list = list_dir(argv_list.test_folder)
    # print(test_file_list)

    # 判断目录是否存在
    output_path = argv_list.target_folder
    if os.path.exists(output_path) == False:
        os.mkdir(output_path)

    # 遍历所有文件
    for test_file in test_file_list:
        output_file = output_path + '/' + test_file.replace(argv_list.test_folder, '')
        descrypt(test_file, output_file)
