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
        #search, list bank
        if (cmd[0:6] == 'search'):
            pass
        if (cmd[0:3] == 'list'):
            pass

    def sendRequest(self, name, data):
        pass

    def processRequest(self, data):
        pass
