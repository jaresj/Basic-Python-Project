import os


fName = os.listdir(path='C:\\Users\\carls\\Desktop\\Python\\Drill\\')


fPath = 'C:\\Users\\carls\\Desktop\\Python\\Drill\\'

paths = os.path.join(fPath, fName[5])

for filename in os.listdir(path='C:\\Users\\carls\\Desktop\\Python\\Drill\\'):
    if filename.endswith('.txt'):
        print(filename)
        print(os.path.getmtime('C:\\Users\\carls\\Desktop\\Python\\Drill\\'))
        continue
    else:
        continue


