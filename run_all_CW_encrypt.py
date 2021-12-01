import subprocess
import os

if __name__ == '__main__':
    #Get list of all cw's
    cw_list = os.listdir("CW_encrypt")

    for cw in cw_list:
        print(cw)
        #Use subprocess to run the courseworks on all the directory files
        command = subprocess.Popen(f'python3 ./CW_encrypt/{cw} ./test_files_encrypt ./results_encrypt ',
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        command.wait()
        command.communicate()
        command.wait()
        command.kill()