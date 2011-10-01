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

        if (cmd[0] == 'search' and cmd[1] == 'server' and cmd[2] == 'problems'):
            print  [x for x in self.bank if cmd[3] in x.tags]

        elif (cmd[0] == 'search' and cmd[1] == 'all' and cmd[2] == 'problems'):
            print self.sendRequest(('search',cmd[3]))

        elif (cmd[0] == 'list' and cmd[1] == 'server' and cmd[2] = 'problems'):
            print self.bank

        elif (cmd[0] == 'list' and cmd[1] == 'all' and cmd[2] == 'problems'):
            print  self.sendRequest(('list', ''))

        else:
            print "Usage: 'search <server/all> problems <query>' or 'list <server/all> problems'" 

    def sendRequest(self, data):
        return self.framework.sendRequest(data)

    def processRequest(self, data):
        type, query = data
        if (type == 'search'):
            return [x for x in self.bank if query in x.tags]
        elif (type = 'list'):
            return self.bank
        else:
            return None
