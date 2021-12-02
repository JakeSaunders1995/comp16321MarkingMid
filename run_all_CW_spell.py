import subprocess
import os
from contextlib import redirect_stdout

if __name__ == '__main__':
    default_path = os.getcwd()
    #format the files into folders and add test files and reuslt folder
    cw_list = os.listdir("CW_spell")

    for cw in cw_list:
        stripped_cw = cw.replace('.py', '')
        if not os.path.exists(f'./CW_spell/{stripped_cw}'):
            os.mkdir(f'./CW_spell/{stripped_cw}')
            move_input = ['mv', f'./CW_spell/{cw}', f'./CW_spell/{stripped_cw}']
            subprocess.call(move_input)
            make_input2 = ['mkdir', f'./CW_spell/{stripped_cw}/results_spell', ]
            subprocess.call(make_input2)
            dict_input = ['cp', f'./EnglishWords.txt', f'./CW_spell/{stripped_cw}']
            subprocess.call(dict_input)
        make_input = ['mkdir', f'./CW_spell/{stripped_cw}/test_files_spell', ]
        subprocess.call(make_input)

        copy_input = ['cp', '-r', f'./test_files_spell', f'./CW_spell/{stripped_cw}/test_files_spell', ]
        subprocess.call(copy_input)



    for cw in cw_list:

        print(cw)

        stripped_cw = cw.replace('.py', '')
        os.chdir(f'./CW_spell/{stripped_cw}')


        inputs= ['python3', f'./{cw}.py', './EnglishWords.txt', './test_files_spell/test_files_spell', f'./results_spell' ]
        subprocess.run(inputs)

        #returns to default chdir
        os.chdir(default_path)