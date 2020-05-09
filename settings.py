"""
settings - Helpers

2020 maschhoff github.com/maschhoff

"""

import json
import os
import getpass
import platform



def loadConfig():
    confDir=directory+"/config.json"
    print("loadConfig() "+confDir)
    res={}
    with open(confDir, 'r') as fp:
        res = json.load(fp)
    return res
   

def writeConfig(config):
    confDir=directory+"/config.json"
    with open(confDir, 'w') as fp:
        json.dump(config, fp)
        
        
        
USER_NAME = getpass.getuser()
osvar = platform.system()

directory=os.path.dirname(__file__)
if osvar == "Windows": 
        directory = r'C:\Users\%s\AppData\Local\unsplashipy' % USER_NAME
else:
        directory=os.path.dirname(__file__)
 
if not os.path.exists(directory):
        os.makedirs(directory)
        config={}
        config["updatetime"]=500
        config["collection"]="wallpaper"
        writeConfig(config)
        print("\r[+] Status: Create directory", end="") 