# file organizer for windows with python 
from importlib.resources import path
import time 
import shutil
import os

# General path in which script will work [can be anything of your desire]
pathFrom = 'C:\\Users\\Administrator\\Downloads\\'

# Check the following folders if they exist and can make them
folders = ['Videos','Documents', 'Images', 'Zip Files','Text Files','Sounds','UnRegistered','Torrents']


def begin():
    checkFileDestinationPath()
    

def checkFileDestinationPath():
    for a in folders:
        if not (os.path.exists(pathFrom + a)):
            os.makedirs(pathFrom + a)
            print("File Created!")
        else: print("File already exists")
    time.sleep(5)
    organizeByExt()

def organizeByExt():
    files = os.listdir(pathFrom)
    for a in files:
        #Image files
        if (a.endswith("jpg")):
            shutil.move(pathFrom + a, pathFrom + "Images\\")
        if (a.endswith("jpeg")):
            shutil.move(pathFrom + a, pathFrom + "Images\\")
        if (a.endswith("png")):
            shutil.move(pathFrom + a, pathFrom + "Images\\")
        if (a.endswith("gif")):
            shutil.move(pathFrom + a, pathFrom + "Images\\")

       # Video Files
        if (a.endswith("mp4")):
            shutil.move(pathFrom + a, pathFrom + "Videos\\")
        if (a.endswith("mov")):
            shutil.move(pathFrom + a, pathFrom + "Videos\\")

        # Music 
        if (a.endswith("mp3")):
            shutil.move(pathFrom + a, pathFrom + "Sounds\\")
        if (a.endswith("m4a")):
            shutil.move(pathFrom + a, pathFrom + "Sounds\\")
        
        # Zip files trash can
        if (a.endswith("zip")):
            shutil.move(pathFrom + a, pathFrom + "Zip Files\\")

        #Docs 
        if (a.endswith("pdf")):
            shutil.move(pathFrom + a, pathFrom + "Documents\\")
        if (a.endswith("docx")):
            shutil.move(pathFrom + a, pathFrom + "Documents\\")
        if (a.endswith("pptx")):
            shutil.move(pathFrom + a, pathFrom + "Documents\\")
        if (a.endswith("doc")):
            shutil.move(pathFrom + a, pathFrom + "Documents\\")
        
        #txt
        if (a.endswith("txt")):
            shutil.move(pathFrom + a, pathFrom + "Text Files\\")
        
        #exe
        if (a.endswith("exe")):
            shutil.move(pathFrom + a, pathFrom + "UnRegistered\\")
        if (a.endswith("msi")):
            shutil.move(pathFrom + a, pathFrom + "UnRegistered\\")
        #Torrents
        if (a.endswith("torrent")):
            shutil.move(pathFrom + a, pathFrom + "Torrents\\")

        
        
        
begin()