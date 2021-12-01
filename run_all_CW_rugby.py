import subprocess
import os
import glob
import shutil
count = 0

broken_files =[]
if __name__ == '__main__':



    #Get list of all cw's
    cw_list = os.listdir("CW_rugby")

    for cw in cw_list:

        if not os.path.exists(f'./results_rugby/{cw}'):
            os.mkdir(f'./results_rugby/{cw}')

    for cw in cw_list:

        #clear any works from the test-files folder
        test_list = os.listdir("test_files_rugby")

        for file in test_list:
            if file != 'test_file1.txt' and file != "test_file2.txt" and file != "test_file3.txt":
                os.remove(f'./test_files_rugby/{file}')



        print(cw)



        inputs= ['python3', f'./CW_rugby/{cw}', './test_files_rugby', f'./results_rugby/{cw}' ]


        #Use subprocess to run the courseworks on all the directory files
        try:
            subprocess.check_call(inputs )
        except subprocess.CalledProcessError:
            broken_files.append(cw)


        move_inputs = ['mv', f'./CW_rugby/{cw}', f'./broken_rugby']

        print(len(broken_files))


        #t = os.system(f'python3 ./CW_rugby/{cw} ./test_files_rugby ./results_rugby/{cw}')


        count +=1

        #print('Return code:', command.returncode)







    print(f'{count} courseworks run')
    print(broken_files)