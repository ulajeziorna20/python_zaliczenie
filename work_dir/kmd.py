import os
from msilib.text import dirname

def pwd():
    print(os.getcwd())

def get_list():

    list = os.listdir()
    # print(list)

    for el in list:
        print(el)

def cd(path):
    os.chdir(path)