from NetworkServer import Server
from Data import Problem, Bank
import random, cmd, readline

#framework keeps a list of all the servers and passes requests between them. This models the complex networking between the servers.
class Framework(cmd.Cmd):
    def __init__(self, numServers, numProbs):
        self.servers = dict([('Server%i' % i, Server('Server%i' % i, self.problems('Server%i'%i, i*numProbs,numProbs), self)) for i in xrange(numServers)])
        self.loggedIn = self.servers[self.servers.keys()[0]]
        cmd.Cmd.__init__(self)
        self.prompt = '\n>'
        
    #creates a bunch of random problem banks, one for each server
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

    def do_login(self, name):
        if name in self.servers.keys():
            self.loggedIn = self.servers[name]
            print 'logged in to {0:s}'.format(self.loggedIn)
        else:
            print "{0:s} is not a valid server name".format(name)

    def help_login(self):
        print 'Usage: login <ServerName>\nChanges the active server'

    def do_loggedIn(self, args):
        print self.loggedIn

    def help_loggedIn(self):
        print 'Usage: loggedIn\nLists the name of the active server'

    def do_sproblems(self, args):
        self.loggedIn.listServerProblems()

    def help_sproblems(self):
        print "Usage: sproblems\nLists all problems on the server"

    def do_problems(self, args):
        self.loggedIn.listAllProblems()

    def help_problems(self):
        print "Usage: problems\nLists all problems on the network"

    def do_search(self, args):
        self.loggedIn.searchAllProblems(args.strip())

    def help_search(self):
        print "Usage: search <query>\nLists all problems on the network that match query tag"

    def do_ssearch(self, args):
        self.loggedIn.searchServerProblems(args.strip())

    def help_ssearch(self):
        print "Usage: ssearch <query>\nLists all problems on server that match query tag"

    def do_exit(self, line):
        return True

    #shortcuts
    #do_quit = do_exit
    #do_q = do_exit
    
if __name__ == '__main__':
    defaultNumServers = 5
    defaultNumProblems = 10
    numServers = raw_input('Input number of servers: ')
    numServers = int(numServers) if numServers.isdigit() else defaultNumServers
    numProblems = raw_input('Input number of problems on each server: ')
    numProblems = int(numProblems) if numProblems.isdigit() else defaultNumProblems

    print "Starting servers%s...\n" % (' with defaults' if numServers==defaultNumServers and numProblems == defaultNumProblems else '')
    
    framework = Framework(numServers, numProblems)
    print "Servers started:"
    for x in framework.servers.values():
        print x
    framework.cmdloop()
