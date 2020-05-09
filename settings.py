"""
settings - Helpers

2020 maschhoff github.com/maschhoff

"""

import json
import os

def loadConfig():
    confDir=os.path.dirname(__file__)+"/config.json"
    print("loadConfig() "+confDir)
    res={}
    with open(confDir, 'r') as fp:
        res = json.load(fp)
    return res
   

def writeConfig(config):
    confDir=os.path.dirname(__file__)+"/config.json"
    with open(confDir, 'w') as fp:
        json.dump(config, fp)