# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:21:56 2011

@author: Nathan
"""

class Problem:
    def __init__(self, name, diff, tags, descr='None'):
        self.name = name
        self.diff = diff
        self.tags = tags
        self.descr = descr

class PSet:
    def __init__(self, problems):
        self.probs = problems

class Hierarchy:
    def __init__(self):
        pass
