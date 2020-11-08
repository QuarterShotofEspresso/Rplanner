from course import *
import json
from prettytable import PrettyTable

generateMessage = """
 Enter course offerings as F/W/s/S corressponding to Fall/Winter/Spring/Summer
 Enter prereqs by course ID and seperate by ONE SPACE, NOT COMMAS.
 Empty entries restart course's entry.
 Type 'quit' on course name to stop writing new courses.
"""






class GenerateCourseList:
    def __init__(self, filepath):
        self._courselist = []
        self._filepath = filepath

    def makeCourse(self):
        while(True):
            name  = input('Course Name:    ').upper()
            if( name == 'QUIT' ):
                return {}
            elif( len(name) == 0 ):
                print('Entry is empty. Restarting THIS course entry')
                continue

            cid   = input('Course id:      ').upper()
            if( len(cid) == 0 ):
                print('Entry is empty. Restarting THIS course entry')
                continue

            avail = input('Offered: [FWsS] ')
            availarr = []
            if('F' in avail):
                availarr.append('FALL')
            if('W' in avail):
                availarr.append('WINTER')
            if('s' in avail):
                availarr.append('SPRING')
            if('S' in avail):
                availarr.append('SUMMER')
            if( len(availarr) == 0 ):
                print('Entry is empty. Restarting THIS course entry')
                continue
            
            
            pre   = input('Prereqs:        ').upper().split(' ')
            if len(pre) == 0:
                print('Entry is empty. Restarting THIS course entry')
                continue
            

            cl    = int(input('Course Load:    '))

            courseDescription = {'name': name, 'id': cid, 'avail': availarr, 'pre': pre, 'load': cl}


            print('Course Description:\n{0}'.format(courseDescription))
            if( input('CourseValid? [Y/n]').lower() == 'n' ):
                print('Restarting THIS course entry')
                continue
            
            return courseDescription




    def generate(self, editMode):

        print(generateMessage)

        newcourse = self.makeCourse()

        while( bool(newcourse) ):
            self._courselist.append(newcourse)
            newcourse = self.makeCourse()

        print('Collected data. Writing to file: {0}'.format(self._filepath))
        with open(self._filepath, editMode) as fp:
            json.dump(self._courselist, fp)
        
        
        return


    def list(self):
        with open(self._filepath, 'r') as fp:
            json.load(self._courselist, fp)

        for key, value in self._courselist.items():
            print(key, value)

        return







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

        #if False:
        #    # dbg------------------------------------
        #    print('Updated Course List:')
        #    for course in self._courselist:
        #        print(repr(course))
        #        print('\n')

        #pdb.set_trace()





    def checkPreqsSorted(self, checkCourse): #?
        for course in self._courselist:
            if(checkCourse._id != course._id and course._id in checkCourse._pre):
                return False
        return True




    def fileIntoQuarters(self, maxload):
        # declare quarters
        self.Fall   = QuarterList(Quarters.FALL.name, maxload)
        self.Winter = QuarterList(Quarters.WINTER.name, maxload)
        self.Spring = QuarterList(Quarters.SPRING.name, maxload)
        self.Summer = QuarterList(Quarters.SUMMER.name, maxload)

        # fill each quarter block
        while( len(self._courselist) != 0 ):
            #pdb.set_trace() #dbg
            self.Fall.addCourses(self)
            self.Winter.addCourses(self)
            self.Spring.addCourses(self)
            if(self.excludeSummer):
                self.Summer.addCourses(self)

        return


    def levelPlan(self, *courselists):
        #pdb.set_trace()
        most_courses = len(max(courselists, key=lambda p: len(p)))
        for courselist in courselists:
            while( len(courselist) != most_courses ):
                courselist.append('')


    def generateRPlanner(self):
        rplanPT = PrettyTable()
        i = 0

        for i in range(len(self.Fall._quarterlist)):
            self.levelPlan(self.Fall._quarterlist[i],
                           self.Winter._quarterlist[i],
                           self.Spring._quarterlist[i],
                           self.Summer._quarterlist[i])
            rplanPT.add_column(self.Fall._quarter, self.Fall._quarterlist[i])
            rplanPT.add_column(self.Winter._quarter, self.Winter._quarterlist[i])
            rplanPT.add_column(self.Spring._quarter, self.Spring._quarterlist[i])
            rplanPT.add_column(self.Summer._quarter, self.Summer._quarterlist[i])
            self._rplan += '\n' + rplanPT.get_string(title='Year {0}'.format(i))
            rplanPT.clear()
        
        return 




    def printRPlanner(self):
        print(self._rplan)
        return


    def saveRPlanner(self):
        with open(self._savefile, 'w+') as fp:
            fp.write(self._rplan)

        return




