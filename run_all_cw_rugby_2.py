import os
import subprocess

count = 0

broken_files =[]



if __name__ == '__main__':
    default_path = os.getcwd()
    #format the files into folders and add test files and reuslt folder
    cw_list = os.listdir("CW_rugby")

    for cw in cw_list:
        stripped_cw = cw.replace('.py', '')
        if not os.path.exists(f'./CW_rugby/{stripped_cw}'):
            os.mkdir(f'./CW_rugby/{stripped_cw}')
            move_input = ['mv', f'./CW_rugby/{cw}', f'./CW_rugby/{stripped_cw}']
            subprocess.call(move_input)
            make_input = ['mkdir', f'./CW_rugby/{stripped_cw}/test_files_rugby', ]
            subprocess.call(make_input)
            make_input2 = ['mkdir', f'./CW_rugby/{stripped_cw}/results_rugby', ]
            subprocess.call(make_input2)
            copy_input = ['cp', '-r', f'./test_files_rugby', f'./CW_rugby/{stripped_cw}/test_files_rugby', ]
            subprocess.call(copy_input)


    for cw in cw_list:
        print(cw)
        stripped_cw = cw.replace('.py', '')
        os.chdir(f'./CW_rugby/{stripped_cw}')


        inputs= ['python3', f'./{cw}.py', './test_files_rugby/test_files_rugby', f'./results_rugby' ]
        subprocess.run(inputs)

        #returns to default chdir
        os.chdir(default_path)











