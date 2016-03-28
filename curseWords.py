import urllib

def isCursedWord(word):
    curseWords = ["shit", "asshole", "ass", "bitch", "damn", "fuck", \
                  "motherfucker", "son of a bitch"]

    word = word.lower()
               
    if word in curseWords:
        return True

    return False

def checkFileForCurseWords(file):
    for word in file.split():
        if isCursedWord(word):
            print "Profanity detected"
            return

    print ".: FILE IS CLEAN :."

def check2(file):
    try:
        connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + file);

        response = connection.read()
        
        if response == "false":
            print ".: FILE IS CLEAN :."
        elif response == "true":
            print "Profanity detected"
        else:
            print "Error reading the webpage. Program is finished!"
    except:
        print "Error with the connection. Program is finished!"
    
        

def readFile():
    path = "C:\Users\Alessandro\Desktop\sample.txt"
    
    try:
        return open(path).read()
    except:
        print "Couldn't open file"
        return False

file = readFile()

if file != False:
    check2(file)


