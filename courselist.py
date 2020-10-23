from course import *
import json


class CourseList:
    def __init__(self):
        _courselistScrambled = []
        _courselist  = []    
        _quarterlist = {Quarters.FALL: [], Quarters.WINTER: [], Quarters.SPRING: [], Quarters.SUMMER: []}


    def populateCourseList(self, filepath):
        # open filepath
        with fp as open(filepath, 'r'):
            rawdata = json.load(fp)


        if( len(rawdata) == 0 ):
            raise Exception('File contained no data')


        #iterate through each element and parse them as Course objects
        for element in rawdata:
            self._courselistScrambled.append(
                Course( element['name'],
                        element['id'],
                        element['avail'],
                        element['pre']
                        )
                )
       
        return




    def sortByPre(self):
        self._courselist.append(self._courselistScrambled.pop(0))
        newIndex = 0
        # for each course in the scrambled set
        for course in self._courselistScrambled:
            # skim through each course in the sorted set
            for i in range(len(self._courselist)):
                # if the selected course is a preq, insert immediately
                if( course.amIPre(self._courselistScrambled.at(i)) ):
                    newIndex = i
                    break
                # else if the selected course has a preq, parse through each till the end
                elif( course.wasHePre( self.courselistScrambled.at(i) ) ):
                    newIndex = i + 1
            self._courselist.insert(newIndex, course)


    def allPreSorted(self): #?



    #def amIPre(self): #?



    #def wasHePre(self): #?



    def fileIntoQuarters(self):






class QuarterList:
    def __init__(self, quarter):
        _quarter = quarter
        _quarterList = []

