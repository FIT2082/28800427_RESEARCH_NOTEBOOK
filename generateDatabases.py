"""
generates the databases using the fzn files. Takes as its parameter the location of the fzn files (a dir)
uses the CPProfiler to profile the behaviour of each execution of the solver to generate the databases
images are not generated for all of them, since they will probably be irrelevant for most of them
"""

import os

# get the directory for the FZN files
directory = input("FZN files dir: ")

if (not directory[-1:] == "\\"):
    directory += "\\"

def cmdStr(str):
    return "\"" + str + "\""


fzns = []
subDirs = []

# get all the subdirectories created by the converter
files = os.listdir(directory)
for file in files:
    if os.path.isdir(directory + file):
        subDirs.append(directory + file)


# get all the .fzn files int a list for execution in cpp
# the fznFiles directory should contain no dirs but will check anyway
for i in range(len(subDirs)):
    fzns.append([])
    files = os.listdir(subDirs[i] + "\\")

    for file in files:
        if os.path.isfile(subDirs[i] + "\\" + file) and file[-4:] == ".fzn":
            fzns[i].append(file)

# truncate all of the lists of fzns to ten at max
for i in range(len(fzns)):
    fzns[i] = fzns[i][:10]


# generate the cmd code to cpp all of the fzns
outBAT = []
for i in range(len(subDirs)):
    for fzn in fzns[i]:
        outBAT.append("\nstart cpp --save_execution " + cmdStr(subDirs[i] + "\\" + fzn[:-4] + ".db") + "\n")
        outBAT.append("timeout 2\n")
        outBAT.append("gc -mode cpprofiler -cpprofiler-info true -t 10000 " + cmdStr(subDirs[i] + "\\" + fzn) + "\n")
        outBAT.append("timeout 4\n")
        #outBAT.append("TASKKILL /F /IM cpp.exe\n")

with open(os.path.join(directory, 'cppAll.bat'), 'w+') as BAT:
    BAT.writelines(outBAT)