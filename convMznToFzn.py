"""
produces a .BAT file which converts all MZN files within a given directory including all subdirectories (recursively)
executing it on cmd will produce a FZN for all of the found files, in a new folder within the topmost directory
runs with arg -G as both std and gecode compilation
"""

import os
from pathlib import Path

directory = input("Top-lv dir: ")

if not directory[-1:] == "\\":
    directory += "\\"


def cmdStr(str):
    return "\"" + str + "\""


# function to create directories in a given existing dir
def createDirectory(parentDir, dirName):
    if not parentDir[-1:] == "\\":
        parentDir += "\\"
    if not os.path.exists(os.path.dirname(parentDir)):
        return -1
    dirName = dirName.strip("\\")
    newDir = parentDir + dirName + "\\"
    if not os.path.exists(os.path.dirname(newDir)):
        try:
            os.makedirs(os.path.dirname(newDir))
        except OSError as exc: # Guard against race condition
            if exc.errno != exc.errno.EEXIST:
                raise
    return newDir


# generate the topmost out dir
parentOutDir = createDirectory(str(Path(directory).parent), "fznFiles")

# get a list of all the subfiles/dirs in the TL dir
filesInDir = os.listdir(directory)
subDirs = []
subSubDirs = []

# generate all the subDirs
for i in range(len(filesInDir)):
    if os.path.isdir(directory + filesInDir[i]):
        subDirs.append(directory + filesInDir[i])
        # also check for second level subdirectories
        subSubDirs.append([])
        files = os.listdir(directory + filesInDir[i] + "\\")
        for file in files:
            if os.path.isdir(directory + filesInDir[i] + "\\" + file):
                subSubDirs[i].append(directory + filesInDir[i] + "\\" + file)

mdznFiles = []
for i in range(len(subDirs)):
    # collect all the mzns and associated dzns and pair them in lists
    files = os.listdir(subDirs[i])

    localMzns = []
    localDzns = []

    # search first level subdirectory (i.e. problem)
    for file in files:
        if os.path.isfile(subDirs[i] + "\\" + file):
            ext = file[-4:]
            if ext == ".mzn":
                localMzns.append([subDirs[i] + "\\" + file, False])
            elif ext == ".dzn":
                localDzns.append([subDirs[i] + "\\" + file, False])

    # search second level subdirectory (i.e. specific problem instance)
    for subSubDir in subSubDirs[i]:
        files = os.listdir(subSubDir)

        for file in files:
            if os.path.isfile(subSubDir + "\\" + file):
                ext = file[-4:]
                if ext == ".mzn":
                    localMzns.append([subSubDir + "\\" + file, True])
                elif ext == ".dzn":
                    localDzns.append([subSubDir + "\\" + file, True])

    mdznFiles.append([subDirs[i], localMzns, localDzns])

# generate a subdir for all of the different problem classes
outDirs = []
for dir, mzns, dzns in mdznFiles:
    outDirs.append(createDirectory(parentOutDir, dir[dir.rindex("\\"):]))


# generate the output BAT code which converts all the MZNs
outBAT = []
for i in range(len(mdznFiles)):
    originDir = mdznFiles[i][0]
    mzns = mdznFiles[i][1]
    dzns = mdznFiles[i][2]
    outDir = outDirs[i]

    for mzn, mIsSubSub in mzns:
        mznCut = mzn[len(originDir) + 1:-4]
        if mIsSubSub:
            mznCut = mznCut.replace("\\", "__")
        cmdMzn = cmdStr(mzn)

        for dzn, dIsSubSub in dzns:
            dznCut = dzn[len(originDir) + 1:-4]
            if dIsSubSub:
                dznCut = dznCut.replace("\\", "__")
            cmdDzn = cmdStr(dzn)

            retCode = "mzn2fzn -G gecode --fzn " + cmdStr(outDir + "gc__" + mznCut + "__" + dznCut + ".fzn") \
                      + " " + cmdMzn + " " + cmdDzn + "\n"
            retCode += "echo " + mznCut + "_" + dznCut + " gecode fzn done" + "\n\n"
            retCode += "mzn2fzn -G std --fzn " + cmdStr(outDir + "std__" + mznCut + "__" + dznCut + ".fzn") \
                       + " " + cmdMzn + " " + cmdDzn + "\n"
            retCode += "echo " + mznCut + "_" + dznCut + " std fzn done" + "\n\n"
            outBAT.append(retCode)

        if len(dzns) == 0:
            retCode = "mzn2fzn -G gecode --fzn " + cmdStr(outDir + "gc__" + mznCut + ".fzn") + " " + cmdMzn + "\n"
            retCode += "echo " + mznCut + " gecode fzn done" + "\n\n"
            retCode += "mzn2fzn -G std --fzn " + cmdStr(outDir + "std__" + mznCut + ".fzn") + " " + cmdMzn + "\n"
            retCode += "echo " + mznCut + " std fzn done" + "\n\n"
            outBAT.append(retCode)

# produce the BAT and save to the new directory
with open(os.path.join(parentOutDir, 'mzn2fznAll.bat'), 'w+') as BAT:
    BAT.writelines(outBAT)

