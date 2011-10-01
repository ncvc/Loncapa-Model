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


tags = ['lol', 'wat', 'sup', 'chris can suck a dick']
names = ['test name 1', 'name', 'not a name']
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
            