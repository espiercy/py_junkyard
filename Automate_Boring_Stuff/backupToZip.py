#!C:\Python34\python.exe

#epiercy -
#backupToZip.py - copy folder and cont => .zip,
#file ids increment

import zipfile, os

def backupToZip(folder):
    #backup folder cont => .zip
    #req's absolute path, must be decoupled from current dir
    folder = os.path.abspath(folder)

    #what files already exist?
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break #if I didn't find this .zip, I found my new id number
        number = number + 1

    #Create zip file

    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    #traverse folder tree, compress everything
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files %s...' % (foldername))
        #add folder to .zip
        backupZip.write(foldername)
        #add folder files to .zip
        for filename in filenames:
            newBase = os.path.basename(folder) + '_' #!!! see below
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
        
    print('Finished backupToZip')

backupToZip(r'C:\Users\Evan\Desktop\Automate_Boring_Stuff') 

#!!! THIS LINE ORIGINALLY READ: newBase / os.path.basename(folder) + '_'
#A blatant error in the text. Peeve
#And I have to admit, I'm not seeing the elegenace here

