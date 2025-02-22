print('lets do it :)')

import sys
sys.path.append("./work_dir")

from work_dir import kmd, common_functions, calc
from work_dir import calc


while True:
    cmd = input().split()

    if_list_exist = len(cmd)

    if if_list_exist == 0:
        print('Data incorrect')
    elif if_list_exist == 1:
        if cmd[0] == 'quit':
            break
        elif cmd[0] == 'pwd':
            kmd.pwd()
        elif cmd[0] == 'ls':
            kmd.get_list()
        elif cmd[0] == 'cd':
            print('The command requires at least one argument')
        elif cmd[0] == 'calc':
            print('The command requires at least one argument')

            calc.calc_main_func()

        else:
            print('I don\'t handle such a command sorry. Please after head gibe me a correct path')

    elif if_list_exist > 1:

        if cmd[0] == 'cd':

            try:
                kmd.cd(cmd[1])

            except FileNotFoundError:
                print('This path is incorrect')

        elif cmd[0] == 'head':
            # print('I am here :)')
            common_functions.read_first_file_portion(cmd[1])
