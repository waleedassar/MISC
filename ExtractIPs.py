import os,sys,time,re


#\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b


def main(input_file):
    AnyFound = False
    AnyFound_full = False
    fOut = 0
    fOut_full = 0
    if os.path.exists(input_file):
        fIn = open(input_file,"r")
        for fLine in fIn:
            xxx = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",fLine)
            if xxx:
                if AnyFound_full == False:
                    fOut_full = open("ips_full.txt","w")
                    fOut_full.write(fLine + "\r\n")
                    AnyFound_full = True
                else:
                    fOut_full.write(fLine + "\r\n")
                    
                for x in xxx:
                    if x:
                        if AnyFound == False:
                            fOut = open("ips.txt","w")
                            fOut.write(x + "\r\n")
                            AnyFound = True
                        else:
                            fOut.write(x + "\r\n")
                        print x
        if fOut:
            fOut.close()
        if fOut_full:
            fOut_full.close()
        if fIn:
            fIn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: ExtractIPs.py Input_File\r\n"
        sys.exit(-1)
    else:
        main(sys.argv[1])
