# file organizer for windows with python 
from importlib.resources import path
import time 
import shutil
import os

# General path in which script will work [can be anything of your desire]
pathFrom = 'C:\\Users\\Administrator\\Downloads\\'

# Check the following folders if they exist and can make them
folders = ['Videos','Documents', 'Images', 'Zip Files','Text Files']




def begin():
    checkFileDestinationPath()
    organizeByExt()

def checkFileDestinationPath():
    for a in folders:
        if not (os.path.exists(pathFrom + a)):
            os.makedirs(pathFrom + a)
            print("File Created!")

        else: print("File already exists")

def organizeByExt():
    files = os.listdir(pathFrom)
    for a in files:
        if (a.endswith("jpg")):
            shutil.move(pathFrom + a, pathFrom + "Images\\")
        if (a.endswith("jpeg")):
            shutil.move(pathFrom + a, pathFrom + "Images\\")
        if (a.endswith("png")):
            shutil.move(pathFrom + a, pathFrom + "Images\\")
        if (a.endswith("gif")):
            shutil.move(pathFrom + a, pathFrom + "Images\\")
            
organizeByExt()