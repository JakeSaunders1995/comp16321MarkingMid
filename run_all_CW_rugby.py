import subprocess
import os

if __name__ == '__main__':
    #Get list of all cw's
    cw_list = os.listdir("CW_rugby")

    for cw in cw_list:
        print(cw)

        inputs= ["python3", "./CW_rugby/"+cw, "./test_files_rugby", "./results_rugby" ]

        #Use subprocess to run the courseworks on all the directory files
        command = subprocess.Popen(inputs,
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        command.wait()
        command.communicate()
        command.wait()
        command.kill()