import os
import string
def rename_files():
    #get file names from a folder
    fileList = os.listdir("F:\FSNanodegree\prank")
    print fileList
    #must change the working directory to the directory of the pictures.
    os.chdir("F:\FSNanodegree\prank")

    #for each file, rename filename
    for fileName in fileList:
       # print os.getcwd()
        #(old filename, new filename devoid of any numbers)
        os.rename(fileName,fileName.translate(None, "0123456789") )

rename_files()