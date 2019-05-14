#import os & shutil modules.
import os, shutil

#Define function called pptx_copy.
def pptx_copy():

    #Find files in ~/Downloads with the file extension .pptx or .ppt.
    for root, dirs, files in os.walk(os.path.expanduser("~/Downloads")):
        for file_name in files:
            if file_name.endswith(".ppt") or file_name.endswith(".pptx"):
            
    #Copy these files into the current working directory.
                shutil.copy(os.path.join(root, file_name), os.getcwd())

pptx_copy()