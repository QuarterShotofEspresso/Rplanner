from course import *
import json


class CourseList:
    def __init__(self, ns):
        _courselistScrambled = []
        _courselist  = []    
        _quarterlist = {Quarters.FALL: [], Quarters.WINTER: [], Quarters.SPRING: [], Quarters.SUMMER: []}
        _rplan = ''
        self.Fall = 0
        self.Winter = 0
        self.Spring = 0
        self.Summer = 0
        excludeSummer = ns




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





    def checkPreqsSorted(self, checkCourse): #?
        for course in self.courselist:
            if(course._id in checkCourse._pre):
                return False
        return True




    def fileIntoQuarters(self, maxload):
        # declare quarters
        self.Fall   = QuarterList(Quarters.FALL)
        self.Winter = QuarterList(Quarters.WINTER)
        self.Spring = QuarterList(Quarters.SPRING)
        self.Summer = QuarterList(Quarters.SUMMER)

        # fill each quarter block
        while( len(self._courselist) != 0 ):
            Fall.addCourses(maxload, self._courselist)
            Winter.addCourses(maxload, self._courselist)
            Spring.addCourses(maxload, self._courselist)
            if(excludeSummer):
                Summer.addCourses(maxload, self._courselist)

        return



    def generateRPlanner(self):
        rplanPT = PrettyTable()
        i = 0

        for i range(len(self.Fall._quarterlist)):
            rplanPT.add_column(Fall._quarter, Fall._quarterList[i])
            rplanPT.add_column(Winter._quarter, Winter._quarterList[i])
            rplanPT.add_column(Spring._quarter, Spring._quarterList[i])
            rplanPT.add_column(Summer._quarter, Summer._quarterList[i])
            self._rplan += '\n' + rplanPT.get_string(title='Year {0}'.format(i))
            rplanPT.clear()

        return 




    def printRPlanner(self):
        print(self._rplan)
        return


    def saveRPlanner(self):
        with fp as open(self._savefile, 'w+'):
            fp.write(self._rplan)

        return




