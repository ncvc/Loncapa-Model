from Data import Problem, Bank
import random

class Server:
    def __init__(self, name, bank, framework, psets):
        self.name = name
        self.bank = bank
        self.framework = framework
        self.psets = psets
    
    def command(self, cmd):
        cmd = cmd.lower().split()

        if cmd[0] == 'help':
            print '\
            login [server] - change the active server\n\
            list servers - see the names of all servers in the simulated network\n\
            problems - see all problems on network\n\
            sproblems - see all problems on simulated server\n\
            search [query] - see all matches on the network\n\
            ssearch [query] - see all matches on the active server\n\
            psets - see all psets on network [NOT IMPLEMENTED]\n\
            spsets - see all psets on active server\n\
            mkpset [name] - create a new pset on the active server\n\
            rmpset [name] - delete pset from the active server [NOT IMPLEMENTED]\n\
            vpset [name] - view pset questions [NOT IMPLEMENTED]\n\
            aqpset [name] [problem] - add question to a pset on the active server [NOT IMPLEMENTED]\n\
            rmqpset [name] [problem] - remove question from a pset on the active server [NOT IMPLEMENTED]\n\
            rec [problem] - recommend similar problems [NOT IMPLEMENTED]\n'

        elif cmd[0] == 'ssearch' and len(cmd) == 2:
            self.searchServerProblems(cmd[1])
            
        elif cmd[0] == 'search' and len(cmd) == 2:
            self.searchAllProblems(cmd[1])
            
        elif cmd[0] == 'sproblems' and len(cmd) == 1:
            self.listServerProblems()

        elif cmd[0] == 'problems' and len(cmd) == 1:
           self.listAllProblems()

        elif cmd[0] == 'spsets' and len(cmd) == 1:
            print "\n" + str(self.psets)

        elif cmd[0] == 'mkpset' and len(cmd) > 1:
            print ''
            self.makePset(cmd[1], cmd[2:] if len(cmd) > 2 else [])

        elif cmd[0] == 'rmpset' and len(cmd) == 2:
            #del self.psets[cmd[1]]
            pass

        elif cmd[0] == 'aqpset' and len(cmd) > 2:
            #self.makePset(cmd[1], cmd[2:])
            pass

        elif cmd[0] == 'vpset' and len(cmd) == 2:
            #for x in self.psets[cmd[1]]:
            #    print x
            pass
                
        elif cmd[0] == 'rmqpset' and len(cmd) > 2:
            #if self.psets.has_key(cmd[1]):
            #    for x in cmd[2:]:
            #        self.psets[cmd[1]].remove(x)
            pass
            
        else:
            print "type 'help' for valid commands" 

    def sendRequestToAll(self, reqType, query = None):
        #print "%s sending %s request to all servers" % (self.name, reqType)
        return self.framework.sendReqToAll((reqType, query))

    def processRequest(self, data):
        reqType, query = data
        #print "%s responding to %s request" % (self.name, reqType)
        if reqType == 'search':
            return self.bank.search(query)
        elif reqType == 'list':
            return self.bank
        else:
            return None
        
    #Listing Problems
    def listServerProblems(self):
        print "\nListing %i problems on %s" % (len(self.bank), self.name)
        print self.bank

    def listAllProblems(self):
        bank = self.unpackBanks(self.sendRequestToAll('list', ''),'All Problems')
        print '\nListing %i problems across all servers' % len(bank)
        print bank

    #Searching Problems
    def searchServerProblems(self, query):
        matches = self.bank.search(query)
        print "\nShowing %i search results for %s on %s" % (len(matches), query, self.name)
        print matches

    def searchAllProblems(self, query):
        bank = self.unpackBanks(self.sendRequestToAll('search',query))
        print '\nShowing %i search results for %s across all servers' % (len(bank), query)
        print bank

    #Listing PSets
    def listServerPsets(self):
        print "Listing %i psets on %s" % (len(self.psets), self.name)
        print self.pset.name
        #print self.pset.data.keys()
        #print self.pset.data.values()
        #print self.pset.data

    def listAllPsets(self):
        pass

    #PSet Operations
    def makePset(self, pset, questions):
        #questions is an array of strings of the question names
        if (not self.psets.has_key(pset.lower())):
            newBank = Bank([], pset.lower(), True)
            self.psets.addBankAsData(newBank)
        if len(questions) > 0:
            #self.psets.addBankAsData(self.getProblemsByName(questions, pset))
            pass
        
    def deletePset(self, pset, questions):
        pass

    #util functions
    def unpackBanks(self, banks, name=None):
        fullBank = Bank([], name)
        for bank in banks:
           fullBank.add(bank)
        return fullBank

    #look up a problem by a name and return the associated problem object
    def getProblemsByName(self, problemNames, bankName):
        result = []
        allProblems = self.unpackBanks(self.sendRequestToAll('list'))
        print allProblems
        for n in problemNames:
            if allProblems.has_key(n.lower()):
                result.append(allProblems[n.lower()])
        return Bank(result, bankName)

    def __repr__(self):
        return "%s with %i Problems" % (self.name, len(self.bank))

