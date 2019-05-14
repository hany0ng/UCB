#Import os & shutil modules.
import os, shutil

#Define function called stu_activities.
def stu_activities():

    #Find files in ~/Downloads that contain the string "Stu_".
    for root, dirs, files in os.walk(os.path.expanduser("~/Downloads")):
        for file_name in files:
            if 'Stu_' in file_name:
            
    #Copy these files into the current working directory.
                shutil.copy(os.path.join(root, file_name), os.getcwd())

stu_activities()

#Can use glob module for case insensitive wildcard search.