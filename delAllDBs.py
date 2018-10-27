import os

directory = "C:\\adamJuddFiles\\academic\\Year2\\Sem2\\Research Project\\fznFiles\\"

files = os.listdir(directory)
subdirs = []
for file in files:
    if os.path.isdir(directory + file):
        subdirs.append(directory + file + "\\")

for subdir in subdirs:
    files = os.listdir(subdir)
    for file in files:
        if file.endswith(".db") or file.endswith(".db-journal"):
            os.remove(subdir + file)