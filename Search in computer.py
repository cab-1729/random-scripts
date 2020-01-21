v=True #True if you want to find more than exact matches
c=True #True if you want the output to be colored
import os
if c:
    from colorama import *
    init(convert=True)
    print(Style.BRIGHT)
if c:
    print(Fore.BLUE)
st=input('Enter the folder to start with : ')
en=input('Enter the thing to search for : ')
matches=[[],[]]
def search(start):
    global matches
    if v:
        for i in os.walk(start):
            for j in i[1]:
                if en in j:
                    matches[0].append(i[0]+'\\'+j)
            for j in i[2]:
                if en in j:
                    matches[1].append(i[0]+'\\'+j)
    else:
        for i in os.walk(start):
            if en in i[1]:
                matches[0].append(i[0]+'\\'+en)
            if en in i[2]:
                matches[1].append(i[0]+'\\'+en)
if c:
    print(Fore.YELLOW)
if st=='':
    print('Searching whole computer ...')
    search('C:')
    search('D:')
elif os.path.exists(st):
    print('Searching the folder ...')
    search(st)
else:
    if c:
        print(Fore.RED)
    print('Original folder does not exist')
    sys.exit(0)
if c:
    print(Fore.CYAN)
if len(matches[0])==0:
    print('No folders found')
else:
    print('Folders :')
    for l in matches[0]:
        print(l)
if c:
    print(Fore.GREEN)
if len(matches[1])==0:
    print('No files found')
else:
    print('Files : ')
    for l in matches[1]:
        print(l)
input()