#!C:\Python34\python.exe

#epiercy
#selective_copy.py - walk through folder tree
#search for files of a particular extension
#copy these files into new folder

#need parent directory's name
#give instructions to traverse the folders and files inside that dir

#for each file that ends in the extension, write it to a folder,
#user can specify: extension, folder, and place to write new folder

import os, shutil

def selective_copy():
    #need absolute path
    parent_name = input('Enter the absolute path of the folder tree to copy: ')
    #no '.' since that's implied
    extension = input('Enter the file extension you wish to copy (e.g. txt, xml): ')
    #get new path to copy files to
    new_path = input('Enter the absolute path of a new folder to write files to: ')
    os.mkdir(new_path)
    #newp, that doesn't work. No wonder. They don't give an adequate explanation
    #in text

    for folderName, subfolders, filenames in os.walk(parent_name):
        for filename in filenames:
            if filename.endswith(extension):
                file_path = os.path.join(folderName, filename)
                print('Copying: ' + file_path)
                shutil.copy(file_path, os.path.join(new_path, filename))

    print('All Finished!')

#so, the issue was that subfolders doesn't seem to have any concrete meaning
#also, practically speaking, I find having to constantly join paths like above
#to be very impractical

selective_copy()
    
