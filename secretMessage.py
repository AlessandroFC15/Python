import os

def stringWithoutDigits(string):
    resultString = ""
    for char in string:
        if not char.isdigit():
            resultString += char

    return resultString

def renameFile(file):
    newFileName = stringWithoutDigits(file)
    
    os.rename(folderLocation + file, folderLocation + newFileName)

    print file + " was renamed to " + newFileName
    

folderLocation = r"C:/Users/Alessandro/Dropbox/Personal Growth/Areas/Career/1. National Recognition/1. Solid Foundation/1st Code-Mini-Camp/Python/prank/"

for file in os.listdir(folderLocation):
            
    print file
    renameFile(file)


