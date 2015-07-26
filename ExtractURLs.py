import os,sys,time


if len(sys.argv) != 2:
    print "Usage: FindURLs.py input.txt\r\n"
    sys.exit(-1)
else:
    inF = sys.argv[1]
    if os.path.exists(inF)==False:
        print "File does not exist\r\n"
        sys.exit(-1)
    FileSize = os.path.getsize(inF)
    if FileSize == 0:
        print "File of zero length\r\n"
        sys.exit(-1)
    fIn = open(sys.argv[1],"r")
    fOut = open("URLs.txt","w")
    for f in fIn:
        Line = f
        if Line.find("http://")!=-1 or Line.find("https://")!=-1:
            print Line
            fOut.write(Line + "\r\n")
    fOut.close()
    
