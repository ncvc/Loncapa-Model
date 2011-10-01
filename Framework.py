# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:49:15 2011

@author: Nathan
"""

import Server

class Framework:
    def __init__(self, numServers):
        self.servers = [Server('Server %i' % i, Bank()) for i in xrange(numServers)]