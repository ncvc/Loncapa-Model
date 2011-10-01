# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:49:15 2011

@author: Nathan
"""

import Server

class Framework:
    def __init__(self, numServers):
        self.servers = dict([('Server%i', Server('Server%i' % i, Bank(), self)) for i in xrange(numServers)])
        self.loggedIn = None
    
    def sendReq(self, name, req):
        if name in self.servers:
            return self.servers[name].processRequest(req)
    
    def sendReqToAll(self, req):
        return [self.sendReq(server, req) for server in self.servers]
    
    def mainLoop(self):
        inp = ''
        
        while inp[0] != 'exit':
            inp = raw_input('>').split()
            
            if inp[0] == 'list' and inp[1] == 'servers':
                for name in self.servers:
                    print name
            elif inp[0] == 'logout':
                print 'logged out of %s' % self.loggedIn
                self.loggedIn = None
            elif inp[0] == 'login':
                self.loggedIn = inp[1]
                print 'logged in to %s' % self.loggedIn
            else:
                if self.loggedIn in self.servers:
                    self.servers[self.loggedIn].command(inp)
        
        print 'Exiting'
                

if __name__ == '__main__':
    framework = Framework(5)
    framework.mainLoop()