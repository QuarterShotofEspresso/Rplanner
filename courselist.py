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
        # for each course in the scrambled set
        for course in self._courselistScrambled:
            newIndex = len(self._courselist)
            # skim through each course backwards in the sorted set
            for i in range(len(self._courselist), 0, -1):
                # if the selected course is a preq, insert immediately
                if( course.amIPre(self._courselistScrambled.at(i)) ):
                    newIndex = i - 1
                # else if the selected course has a preq, parse through each till the end
                elif( course.wasHePre( self.courselistScrambled.at(i) ) ):
                    newIndex = i
                    break
            self._courselist.insert(newIndex, course)


    def allPreSorted(self, index): #?
        if len(self._courselist) == 0:
            raise Exception('Courselist out of range')

        i = 0
        while( self.courselist = 0




    def fileIntoQuarters(self):
        # parse through courselist
        for course in self._courselist:

            # for each course, check that the course is valid
            # 
            





class QuarterList:
    def __init__(self, quarter):
        _quarter = quarter
        _quarterList = []

