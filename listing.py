#!/usr/bin/env python3

import subprocess
import os

path = input("Enter the path of the directory: ")
path1 = 'ls ' + path + ' | sort'
res = subprocess.run(path1, shell=True, stdout=subprocess.PIPE)

lis = res.stdout.decode().split('\n')


for file in lis:
    p = path +'/' + file
    if os.path.isfile(p):
        print(f"{p} it is file\n")
    else:
        print(f"{p} it is directory\n")


