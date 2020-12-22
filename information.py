import os

x=0
y=0
z=0

filename = input ('what is the name of his file?  ')
filepath = input (r'where is the file located? example C:\Users\directory\Desktop   ')
compath = filepath + "/" + filename

open = open(filename, 'w')#this will create the file
open.close()



if os.path.isfile(filename):
    x =1
else:
    print('that file does not exist')

if os.path.isdir(filepath):   #check if filepath exists
    y = 1
else:
    print('that path does not exist')

if os.path.exists(compath):   #check if complete path exists
    z=1
else:
    print('that file is not in that path')

if x+y+z == 3:
    name = input('what is your name? ')
    pnumber = input('what is your phone number? ')
    address = input('whats your address? ')
    words = name + '\n' + str(pnumber) + '\n' + str(address)
    with open(compath,'w') as file_handle:
        file_handle.write(words)
