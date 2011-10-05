from NetworkServer import Server
from Data import Problem, Bank
import random

#framework keeps a list of all the servers and passes requests between them. This models the complex networking between the servers.
class Framework:
    def __init__(self, numServers, numProbs):
        self.servers = dict([('Server%i' % i, Server('Server%i' % i, self.problems('Server%i'%i, i*numProbs,numProbs), self, Bank([], 'psets bank'))) for i in xrange(numServers)])
        self.loggedIn = 'Server0'
        
    #creates a bunch of problem banks, one for each server
    def problems(self, serverName, startNum, entries = 0):
        tags = ['kinematics', 'energy', 'rotation', 'conservation', 'motion', 'potential', 'kinetic']
        diffs = range(10)
        problems = []
        for i in xrange(entries):
            tag = tags[random.randint(0, len(tags)-1)]
            name = "Problem%i" % (startNum+i)
            diff = diffs[random.randint(0, len(diffs) - 1)]
            prob = Problem(name, diff, tag)
            problems.append(prob)
        result = Bank(problems, '%s Problem Bank' %serverName)
        return result

    def sendReq(self, name, req):
        if name in self.servers:
            return self.servers[name].processRequest(req)
    
    def sendReqToAll(self, req):
        return [self.sendReq(server, req) for server in self.servers]
    
    def mainLoop(self):
        inp = ['']
        print '\nLogged in as %s\n' % self.loggedIn
        
        while inp[0] != 'exit':
            rawInp = raw_input('>')
            inp = rawInp.split()

            if not len(inp) > 0:
                inp.append('')
            elif inp[0] == 'list' and inp[1] == 'servers':
                print "%i servers running:\n"
                for name in self.servers:
                    print name
                print "\n"
            #elif inp[0] == 'logout':
            #    print 'logged out of %s' % self.loggedIn
            #    self.loggedIn = None
            elif inp[0] == 'login':
                if inp[1] in self.servers:
                    self.loggedIn = inp[1]
                    print 'logged in to %s' % self.loggedIn
                else:
                    print "%s is not a valid server name" % inp[1]
            elif inp[0] == 'exit':
                pass
            else:
                if self.loggedIn in self.servers:
                    self.servers[self.loggedIn].command(rawInp)
                else:
                    print "Not logged into a valid server!"
        print 'Exiting'
                

if __name__ == '__main__':
    defaultNumServers = 5
    defaultNumProblems = 7
    numServers = raw_input('Input number of servers: ')
    numServers = int(numServers) if numServers.isdigit() else defaultNumServers
    numProblems = raw_input('Input number of problems on each server: ')
    numProblems = int(numProblems) if numProblems.isdigit() else defaultNumProblems

    print "Starting servers%s...\n" % (' with defaults' if numServers==defaultNumServers and numProblems == defaultNumProblems else '')
    
    framework = Framework(numServers, numProblems)
    print "Servers started:"
    for x in framework.servers.values():
        print x
    framework.mainLoop()
