#Contains all data structures

#Represents a single problem
class Problem:
    def __init__(self, name, diff, tags, descr='None'):
        self.name = name
        self.diff = diff
        self.tags = tags
        self.descr = descr
    
    def __repr__(self):
        return '%s: Difficulty %s, Tags %s, Desciption %s' % (self.name, self.diff, self.tags, self.descr)
    
#represents a question or pset bank
class Bank:
    def __init__(self, data=[], name=None, verbose=False):
        self.data = dict([(d.name.lower(), d ) for d in data])
        self.name = name
        self.verbose = verbose
        
    def __repr__(self):
        s = '%s' % self.name if self.verbose else ''
        for p in self.data.values():
            s += str(p) + '\n'
        return s
        
    def __len__(self):
        return len(self.data.values())

    #merge another bank with this bank 
    def add(self, other):
        for d in other.data.values():
            self.data[d.name.lower()] = d

    #add a bank as a data entry into this bank
    def addBankAsData(self, bank):
        self.data[bank.name] = bank
    
    def search(self, query):
         return Bank([d for d in self.data.values() if query in d.tags])

    def has_key(self, key):
        return True if self.data.has_key(key) else False

    def __getitem__(self, item):
        return self.data[item] if self.data.has_key(item) else None
        
class Hierarchy:
    def __init__(self):
        pass

class RecommenderResult:
    def __init__(self, name, amazonDistance):
        self.name = name
        self.amazonDistance = amazonDistance

    def __cmp__(self, other):
        return self.amazonDistance.__cmp__(other.amazonDistance)

    def __repr__(self):
        return "RecommenderResult Name:%s, AmazonDistance:%i" % (self.name, self.amazonDistance)
