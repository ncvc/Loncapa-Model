# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:18:49 2011

@author: Nathan
"""

class Server:
    def __init__(self, name, bank, framework):
        self.name = name
        self.bank = bank
        self.framework = framework
    
    def command(self, cmd):
        cmd = cmd.lower().split()
        if (cmd[0] == 'search' and len(cmd) == 2):
            print [x for x in self.bank if cmd[1] in x.tags]
        elif (cmd[0] == 'list'):
            print self.bank
        else:
            print  "Usage: 'search <query>' or 'list'" 

    def sendRequest(self, data):
        print self.framework.sendRequest(data)

    def processRequest(self, data):
        return self.command('search '+ str(data))
