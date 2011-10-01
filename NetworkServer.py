# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:18:49 2011

@author: Nathan
"""

from Data import Problem
import random

class Server:
    def __init__(self, name, bank, framework):
        self.name = name
        self.bank = bank
        self.framework = framework
    
    def command(self, cmd):
        cmd = cmd.lower().split()

        if cmd[0] == 'search' and cmd[1] == 'server' and cmd[2] == 'problems':
            print  [x for x in self.bank if cmd[3] in x.tags]

        elif cmd[0] == 'search' and cmd[1] == 'all' and cmd[2] == 'problems':
            print self.sendRequest(('search',cmd[3]))

        elif cmd[0] == 'list' and cmd[1] == 'server' and cmd[2] == 'problems':
            print self.bank

        elif cmd[0] == 'list' and cmd[1] == 'all' and cmd[2] == 'problems':
            print  self.sendRequest(('list', ''))

        else:
            print "Usage: 'search <server/all> problems <query>' or 'list <server/all> problems'" 

    def sendRequest(self, data):
        return self.framework.sendRequest(data)

    def processRequest(self, data):
        reqType, query = data
        if reqType == 'search':
            return [x for x in self.bank if query in x.tags]
        elif reqType == 'list':
            return self.bank
        else:
            return None


tags = ['lol', 'wat', 'sup', 'chriscansuckadick']
names = ['testname1', 'name', 'notaname']
diffs = range(10)

class Bank:
    def __init__(self, randEntries=0):
        probs = []
        
        for i in xrange(randEntries):
            tag = tags[random.randint(0, len(tags)-1)]
            
            name = names[random.randint(0, len(names) - 1)]
            diff = diffs[random.randint(0, len(diffs) - 1)]
            prob = Problem(name, diff, tag)
            
            probs.append((tag, prob))
            
        self.problems = dict(probs)
    
    def __repr__(self):
        return '\n'.join([str(prob) for prob in self.problems.values()])
