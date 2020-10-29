from course import *
import json


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
            
            return {'name': name, 'id': cid, 'avail': availarr, 'pre': pre, 'load': cl}


    @classmethod
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


    @classmethod
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
        #self._quarterlist = {Quarters.FALL: [], Quarters.WINTER: [], Quarters.SPRING: [], Quarters.SUMMER: []}
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
            newIndex = len(self._courselist) - 1
            # skim through each course backwards in the sorted set
            for i in range(len(self._courselist) - 1, 0, -1):
                # if the selected course is a preq, insert immediately
                if( course.amIPre(self._courselistScrambled[i]) ):
                    newIndex = i - 1
                # else if the selected course has a preq, parse through each till the end
                elif( course.wasHePre( self._courselistScrambled[i] ) ):
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
            self.Fall.addCourses(maxload, self._courselist)
            self.Winter.addCourses(maxload, self._courselist)
            self.Spring.addCourses(maxload, self._courselist)
            if(self.excludeSummer):
                self.Summer.addCourses(maxload, self._courselist)

        return



    def generateRPlanner(self):
        rplanPT = PrettyTable()
        i = 0

        for i in range(len(self.Fall._quarterlist)):
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
        with open(self._savefile, 'w+') as fp:
            fp.write(self._rplan)

        return




