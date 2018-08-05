#epiercy
#large_file_find.py
#Program that walks through a folder tree
#and searches for exceptionally large files
# if file > 100MB, Print these files with their absolute paths
#AND filesize in MBs to the console

import os

def large_file_find():
    #get filepath:
    parent_name = input('Enter the absolute path of the folder you wish to scan for large files and folders: ')
    for folderName, subfolders, filenames in os.walk(parent_name):
        total_file_size = 0;
        for filename in filenames:
            #first, if big enough, mark an exceptionally large file
            file_path = os.path.join(folderName, filename)
            file_size = os.path.getsize(file_path)
            if  file_size >= 104857600:
                print("Large file found @: " + file_path + '\n size (in bytes): ' + str(file_size))
            total_file_size += file_size
        if total_file_size >= 104857600:
            print("Large folder found @: " + folderName + 't\n size (in bytes): ' + str(total_file_size))

    print('All Finished!')
