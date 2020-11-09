import json
import re

helpmessage_gen = """
 Enter course offerings as F/W/s/S corressponding to Fall/Winter/Spring/Summer
 Enter prereqs by course ID and seperate by ONE SPACE, NOT COMMAS.
 Empty entries restart course's entry.
 Type 'quit' on gen> to stop writing new courses.

 rm <CID>           to remove course by ID
 seed <CID>         to move a previously entered course to the front
 help               to print this message
 none               to forego a course name as this is optional
 quit               to quit courselist generator
 <*>                anything else is interpreted as a course name
"""


class GenerateCourseList:
    def __init__(self, filepath):
        self._courselist = []
        self._filepath = filepath


    def removeCourseDescription(self):
        for course in self._courselist:
            if( course.id == rmtoken ):
                self._courselist.remove(course)
                print('Sucessfully removed {0}'.format(course))
                return
        print('Course not find {0}'.format(course))
        return



    def makeCourse(self):
        
        rmPat   = re.compile(r'^RM (.+)')
        seedPat = re.compile(r'^SEED (.+)')
        helpPat = re.compile(r'^HELP')
        nonePat = re.compile(r'^NONE')
        quitPat = re.compile(r'^QUIT')
        seedcourse = False

        while(True):

            # Course ID
            cid   = input('gen>            ').upper()
            if( quitPat.match(cid) ):
                return {}, False
            elif( rmPat.match(cid) ): # remove cid
                rmtoken = rmPat.search(cid)
                self.removeCourseDescription(rmtoken)
                continue
            elif( seedPat.match(cid) ):
                seedtoken = seedPat.search(cid)
                #self.seedCourseDescription(seedtoken) #TODO: if issue becomes common
                continue
            elif( helpPat.match(cid) ):
                print(helpmessage_gen)
                continue
            elif( len(cid) == 0 ):
                continue

    
            # Course name
            name  = input('Course ID  :    ').upper()
            if( len(name) == 0 ):
                print('Entry is empty. Restarting THIS course entry')
                continue
            elif( nonePat.match(name) ):
                name = ''


            # Availability
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
            

            # Prereqs
            pre   = input('Prereqs [seed]: ').upper().split(' ')
            if len(pre) == 0:
                seedcourse = True
                print('Logged as seed course.')


            # Course Load
            cl    = input('Course Load:    ')
            if( len(cl) == 0 ):
                print('Entry is empty. Restarting THIS course entry')
            else:
                cl = int(cl)

            courseDescription = {'name': name, 'id': cid, 'avail': availarr, 'pre': pre, 'load': cl}


            print('Course Description:\n{0}'.format(courseDescription))
            if( input('Course description valid? [Y/n]').lower() == 'n' ):
                print('Restarting THIS course entry')
                continue
            
            return courseDescription, seedcourse




    def generate(self, keepExisting=True):

        print(helpmessage_gen)

        if( keepExisting ):
            with open(self._filepath, 'r') as fp:
                json.load(self._courselist, fp)

        newcourse = self.makeCourse()
        print(newcourse)

        while( bool(newcourse[0]) ):
            if( newcourse[1] ): #if course is seed course
                self._courselist.insert(newcourse[0], 0)
            else:
                self._courselist.append(newcourse[0])
            newcourse = self.makeCourse()

        print('Collected data. Writing to file: {0}'.format(self._filepath))
        with open(self._filepath, 'w+') as fp:
            json.dump(self._courselist, fp)
        
        
        return


