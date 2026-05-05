# write a python program to print the contests of the directory using the os module search online for the function which does that

import os

# for current directory
# path = "." 
path='/' # list all the files and folders in the root directory
contents = os.listdir(path)

for item in contents:
    print(item)