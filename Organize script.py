# file organizer for windows with python 
import time 
import shutil
import os

# General path in which script will work [can be anything of your desire]
pathFrom = 'C:\\Users\\Administrator\\Downloads\\'

# Check the following folders if they exist and can make them
folders = ['Videos','Documents', 'Images', 'Zip Files']


def begin():
    checkFileDestinationPath()

def checkFileDestinationPath():
    for a in folders:
        if not (os.path.exists(pathFrom + a)):
            os.makedirs(pathFrom + a)
            print("File Created!")

        else: print("File already exists")

     
begin()