import heapq, sys, time
import matplotlib
matplotlib.use('macosx')
import matplotlib.pyplot as pl

class Recommender:
    def __init__(self, courseList):
        start = time.clock()
        courseList = open(courseList)
        #matrix keys will be resource numbers, matrix values are sets of course names that a particular resource appeared in
        self.matrix = {}
        self.numCourses = 0
        courses = set([])

        #process the file line by line
        for line in courseList:
            resourceNumber, courseName = line.strip().split("\t")

            #add the courseName to the dictionary entry for the resourceNumber
            if resourceNumber not in self.matrix:
                self.matrix[resourceNumber] = set([courseName]) 
            else:
                self.matrix[resourceNumber].add(courseName)

            if courseName not in courses:
                courses.add(courseName)
                
        self.numCourses = len(courses)
        courseList.close()
        print 'File Loaded'
        print "Time to load the file: %.3f seconds" % (time.clock()-start)
        
    def recommend(self, seedItem, numRecommendations):
        #check that the seedItem is a valid problem
        if not seedItem in self.matrix:
            return None
        
        #make an empty heap
        amazonResults = []
        
        #calculate the amazonDistance for every item in the matrix (except the recommender seed)
        for key in self.matrix.keys():
            heapq.heappush(amazonResults, (-1*self.amazonDistance(self.matrix[key], self.matrix[seedItem]), key))

        result  = [heapq.heappop(amazonResults) for x in xrange(numRecommendations)]

        #remove seedItem if it is in the results and replace with the next recommendation
        for x in result:
            if x[1] == seedItem:
                result.remove(x)
                result.append(heapq.heappop(amazonResults))
                break

        #return the specified number of results requested
        return result
        
    def amazonDistance(self, resource1CourseSet, resource2CourseSet):
        #find the number of common courses
        return float(len(resource1CourseSet.intersection(resource2CourseSet)))*100/(len(resource1CourseSet)*len(resource2CourseSet))

    def metrics(self):
        print "Starting metrics\n"
        pl.hist([len(x) for x in self.matrix.values() if len(x) < 101], 100)
        pl.axis([0, 100, 0, 40000])
        pl.title("Problem Frequency in Courses vs Number of Problems")
        pl.xlabel("Number of Courses a Problem Appears In")
        pl.ylabel("Number of Courses")

    def matrixLoad(self):
        print "Matrix Load: %.2f%%" % (float(sum([len(x) for x in self.matrix.values()]))*100/(self.numCourses*len(self.matrix.keys())))
        
if __name__ == "__main__":
    print "Loading File {0}...\n".format(sys.argv[1])
    r = Recommender(sys.argv[1])
    #r.matrixLoad()
    #r.metrics()
    seedItem = raw_input('\nEnter seed item number (or enter to exit): ')
    while seedItem is not '':
        start = time.clock()
        result = r.recommend(seedItem, 15)
        if result is not None:
            print "\nRecommended Problems for seed item {0} using {1}:".format(seedItem, sys.argv[1])
            for x in result:
                print "Name:{0:7} AmazonDistance:{1:.3f}".format(x[1], -x[0])
            print "\nTime computing recommendations: {:.3f} seconds\n".format(time.clock() - start)
        else:
            print '\n{0} is not a valid problem number\n'.format(seedItem)
        seedItem = raw_input('Enter new seed item number (or press enter to exit): ')

        
            
        
