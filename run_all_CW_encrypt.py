import subprocess
import os

if __name__ == '__main__':
    default_path = os.getcwd()
    #format the files into folders and add test files and reuslt folder
    cw_list = os.listdir("CW_encrypt")

    for cw in cw_list:
        stripped_cw = cw.replace('.py', '')
        if not os.path.exists(f'./CW_encrypt/{stripped_cw}'):
            os.mkdir(f'./CW_encrypt/{stripped_cw}')
            move_input = ['mv', f'./CW_encrypt/{cw}', f'./CW_encrypt/{stripped_cw}']
            subprocess.call(move_input)
            make_input = ['mkdir', f'./CW_encrypt/{stripped_cw}/test_files_encrypt', ]
            subprocess.call(make_input)
            make_input2 = ['mkdir', f'./CW_encrypt/{stripped_cw}/results_encrypt', ]
            subprocess.call(make_input2)
            copy_input = ['cp', '-r', f'./test_files_encrypt', f'./CW_encrypt/{stripped_cw}/test_files_encrypt', ]
            subprocess.call(copy_input)

    for cw in cw_list:
        print(cw)
        stripped_cw = cw.replace('.py', '')
        os.chdir(f'./CW_encrypt/{stripped_cw}')


        inputs= ['python3', f'./{cw}.py', './test_files_encrypt/test_files_encrypt', f'./results_encrypt' ]
        subprocess.run(inputs)

        #returns to default chdir
        os.chdir(default_path)



