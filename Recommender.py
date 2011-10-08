from Data import RecommenderResult
import heapq, sys
import time

class Recommender:
    def __init__(self, courseList):
        courseList = open(courseList)
        #matrix keys will be resource numbers, matrix values are sets of course names that a particular resource appeared in
        self.matrix = {}
        
        #process the file line by line
        for line in courseList:
            resourceNumber, courseName = line.strip().split("\t")

            #add the courseName to the dictionary entry for the resourceNumber
            if not resourceNumber in self.matrix:
                self.matrix[resourceNumber] = set([courseName])
            else:
                self.matrix[resourceNumber].add(courseName)

        courseList.close()
        
    def recommend(self, seedItem, numRecommendations):
        #check that the seedItem is a valid problem
        if not seedItem in self.matrix:
            print "%s is not a valid problem" % seedItem
            return []
        
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
        return len(resource1CourseSet.intersection(resource2CourseSet))

if __name__ == "__main__":
    print "Loading File..."
    time.clock()
    r = Recommender(sys.argv[1])
    mid = time.clock()
    print "Time to load the file: %f seconds\n" % mid
    print "Recommended Problems for seed item %s using %s" % (sys.argv[2], sys.argv[1])
    for x in r.recommend(sys.argv[2], 10):
        print "Name:%s AmazonDistance:%i" % (x[1], -x[0])
    print "\nTime computing recommendations: %f seconds" % (time.clock() - mid)

    
        
            
        
