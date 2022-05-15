import os

# print(os.path)
import pathlib
currentPath = pathlib.Path().resolve()
print(currentPath)
with open(str(currentPath)+'/FileReport.csv', 'w') as f:
    f.write(f"FileName,Extension,DirPath"+"\n")
    for dirpath, subdirs, files in os.walk(currentPath):
        for x in files:
            fileName = x
            currentdirPath = dirpath
            fileExtension = os.path.splitext(x)[1]
            f.write(f"{fileName},{fileExtension},{currentdirPath}"+"\n")
            print(fileName, currentdirPath, fileExtension)