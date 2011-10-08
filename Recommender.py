from Data import RecommenderResult
import heapq, sys

class Recommender:
    def __init__(self, courseList):
        self.courseList = courseList
        #matrix keys will be resource numbers, matrix values are lists of course names that a particular resource appeared in
        self.matrix = {}
        
    def recommend(self, seedItem, numRecommendations):
        #courseList is the name of the data file
        courseList = open(self.courseList)
        
        #process the file line by line
        for line in courseList:
            line = line.strip().split("\t")
            resourceNumber = line[0]
            courseName = line[1]

            #add the courseName to the dictionary entry for the resourceNumber
            try:
                self.matrix[resourceNumber].append(courseName)
            except KeyError:
                self.matrix[resourceNumber] = [courseName]

        #make an empty heap
        amazonResults = []
        
        #calculate the amazonDistance for every item in the matrix (except the recommender seed)
        for key in [x for x in self.matrix.keys() if not x == seedItem]:
            heapq.heappush(amazonResults,  RecommenderResult(key, self.amazonDistance(self.matrix[key], self.matrix[seedItem])))
            
        #return the specified number of results requested
        return heapq.nlargest(numRecommendations, amazonResults)
        
    def amazonDistance(self, resource1CourseList, resource2CourseList):
        #sort the resource courses by name
        resource1CourseList.sort()
        resource2CourseList.sort()
        i = j = amazonDistance = 0

        #while we're in range keep comparing
        while ( i < len(resource1CourseList) and j < len(resource2CourseList) ):
            #get course names to compare
            course1 = resource1CourseList[i]
            course2 = resource2CourseList[j]
            #if equal, then resource1 and resource2 appeared in a course together, add 1 to the amazon distance
            if course1 == course2:
                amazonDistance += 1
                i += 1
                j += 1
            # course1 comes before course2, no match, advance in course1 list
            elif course1 < course2:
                i += 1
            #course2 comes before course1, no match, advance in course2 list
            else:
                j += 1
        
        return amazonDistance

if __name__ == "__main__":
    r = Recommender("testdata.dat")
    print "Recommended Problems for %s" % sys.argv[1]
    for x in r.recommend(sys.argv[1], 10):
        print x

    
        
            
        
