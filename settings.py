"""
settings - Helpers

2020 maschhoff github.com/maschhoff

"""

import json

def loadConfig():
    #print("loadConfig()")
    res={}
    with open('./config.json', 'r') as fp:
        res = json.load(fp)
    return res
   

def writeConfig(config):
	with open('./config.json', 'w') as fp:
	    json.dump(config, fp)