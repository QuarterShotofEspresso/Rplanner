#
# Property of Ratnodeep Bandyopadhyay
# All rights reserved. Nov 2020.
#

from course import *
import json
from prettytable import PrettyTable


class CourseList:
    def __init__(self, ns):
        self._courselistScrambled = []
        self._courselist  = []    
        self._rplan = ''
        self.Fall = 0
        self.Winter = 0
        self.Spring = 0
        self.Summer = 0
        self.excludeSummer = ns



    def __str__(self):
        return self._rplan


    def populateCourseList(self, filepath):
        # open filepath
        with open(filepath, 'r') as fp:
            rawdata = json.load(fp)


        if( len(rawdata) == 0 ):
            raise Exception('File contained no data')


        #iterate through each element and parse them as Course objects
        for element in rawdata:
            self._courselistScrambled.append(
                Course( element['name'],
                        element['id'],
                        element['avail'],
                        element['pre'],
                        element['load']
                        )
                )
       
        return




    def sortByPre(self):
        self._courselist.append(self._courselistScrambled.pop(0))
        # for each course in the scrambled set
        for course in self._courselistScrambled:
            #pdb.set_trace() #dbg
            newIndex = len(self._courselist)
            # skim through each course backwards in the sorted set
            for i in range(len(self._courselist) - 1, -1, -1):
                # if the selected course is a preq, insert immediately
                if( course.amIPre(self._courselist[i]) ):
                    newIndex = i
                # else if the selected course has a preq, parse through each till the end
                elif( course.wasThatPre( self._courselist[i] ) ):
                    newIndex = i + 1
                    break
            self._courselist.insert(newIndex, course)




    def checkPreqsSorted(self, checkCourse): #?
        for course in self._courselist:
            if((checkCourse._id != course._id) and (course._id in checkCourse._pre)):
                return False
        return True




    def fileIntoQuarters(self, maxload):
        # declare quarters
        self.Fall   = QuarterList(Quarters.FALL.name)
        self.Winter = QuarterList(Quarters.WINTER.name)
        self.Spring = QuarterList(Quarters.SPRING.name)
        self.Summer = QuarterList(Quarters.SUMMER.name)

        # fill each quarter block
        while( len(self._courselist) != 0 ):
            #pdb.set_trace() #dbg
            self.Fall.addCourses(self, maxload)
            self.Winter.addCourses(self, maxload)
            self.Spring.addCourses(self, maxload)
            if(not self.excludeSummer):
                self.Summer.addCourses(self, maxload)

        return


    def levelQuarters(self, *courselists):
        maxLength = len(max(courselists, key=lambda p: len(p)))
        for courselist in courselists:
            while( len(courselist) < maxLength ):
                courselist.append([])


    def levelCourses(self, *courselists):
        #pdb.set_trace()
        most_courses = len(max(courselists, key=lambda p: len(p)))
        for courselist in courselists:
            while( len(courselist) < most_courses ):
                courselist.append('')


    def generateRPlanner(self):
        rplanPT = PrettyTable()
        i = 0

        self.levelQuarters( self.Fall._quarterlist,
                            self.Winter._quarterlist,
                            self.Spring._quarterlist,
                            self.Summer._quarterlist
                          )

        for i in range(len(self.Fall._quarterlist)):
            self.levelCourses(  self.Fall._quarterlist[i],
                                self.Winter._quarterlist[i],
                                self.Spring._quarterlist[i],
                                self.Summer._quarterlist[i]
                             )
            rplanPT.add_column(self.Fall._quarter, self.Fall._quarterlist[i])
            rplanPT.add_column(self.Winter._quarter, self.Winter._quarterlist[i])
            rplanPT.add_column(self.Spring._quarter, self.Spring._quarterlist[i])
            rplanPT.add_column(self.Summer._quarter, self.Summer._quarterlist[i])
            self._rplan += '\n' + rplanPT.get_string(title='Year {0}'.format(i))
            rplanPT.clear()
        
        return 


    def saveRPlanner(self, savefile):
        with open(savefile, 'w+') as fp:
            fp.write(self._rplan)

        return




