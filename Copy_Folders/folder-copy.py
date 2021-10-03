#program to copy/clone the folder with different names
import os, shutil

src = r"D:\scripts\someTests\file_to_be_copied"
dst = r"E:\scripts\someTests"

noOfCopies = 250
Name = "1000000ER"
count = 1 


for i in range(0, noOfCopies):
    someMaths = int(Name[:-2]) + i
    copyName = str(someMaths) + Name[-2:]

   
  # print(copyName)
    destName = os.path.join(dst, copyName)
    os.mkdir(destName)

    for folders, subfolders, files in os.walk(src):

        for file in files:
            #print(file)

            newFileName = copyName + file[-5:]
           # print("NEW FILE NAME = ", newFileName)

            src_file = os.path.join(folders, file)
            dst_file = os.path.join(destName, newFileName )
           # print(dst_file)

            print('COPYING --> {}/{}'.format(count, noOfCopies), newFileName)
            shutil.copy(src_file, dst_file)
    count += 1
