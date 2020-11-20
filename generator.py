import json
import re

helpmessage_gen = """

 Enter course offerings as F/W/S/s corressponding to Fall/Winter/Spring/Summer
 Enter prereqs by course ID and seperate by ONE SPACE, NOT COMMAS.
 Empty entries restart course's entry.
 Type 'quit' on gen> to stop writing new courses.

 Commands:
     rm <CID>           to remove course by ID
     help               to print this message
     quit               to quit courselist generator
     list               list all courses by ID and index
     listsdet           list all courses by all detail and index
     move <SIND> <EIND> move course from <S[tart]IND[ex]> to <E[nd]IND[ex]>
     <*>                anything else is interpreted as a course name

 Example:
     rm CS111           will search for an existing CID by \'CS111\' and remove it
     CS010              starts the creation of a new course entry with CID: \'CS010\'
     ramitbabe          starts the creation of a new course entry with CID: \'ramitbabe\'
     move 12 9          moves the course at index 12 to index 9

"""


class GenerateCourseList:
    def __init__(self, filepath):
        self._courselist = []
        self._filepath = filepath


    def removeCourseDescription(self, rmtoken):
        for course in self._courselist:
            if( course['id'] == rmtoken ):
                self._courselist.remove(course)
                print('Sucessfully removed {0}'.format(course))
                return
        print('CID not found {0}'.format(rmtoken))
        return



    def makeCourse(self):
        
        rmPat   = re.compile(r'^RM (.+)')
        helpPat = re.compile(r'^HELP')
        quitPat = re.compile(r'^QUIT')
        lsPat   = re.compile(r'^LIST')
        lsdPat  = re.compile(r'^LISTDET')
        movePat = re.compile(r'^MOVE (.+?) (.+)')
        seedcourse = False

        while(True):

            # Course ID
            cid    = input('gen>                ').upper()
            if( quitPat.match(cid) ):
                return {}, False
            elif( rmPat.match(cid) ): # remove cid
                rmtoken = rmPat.search(cid)
                self.removeCourseDescription(rmtoken.group(1))
                continue
            elif( helpPat.match(cid) ):
                print(helpmessage_gen)
                continue
            elif( lsPat.match(cid) ):
                for i in range(len(self._courselist)):
                    if(self._courselist[i]['pre'] == 'SEED'):
                        formattedOut = '[{0}:] {1}\tSEED'.format(i, self._courselist[i]['id']))
                    else:
                        formattedOut = '[{0}:] {1}'.format(i, self._courselist[i]['id']))
                continue
            elif( lsdPat.match(cid) ):
                for i in range(len(self._courselist)):
                    print('[{0}:] {1}'.format(i, self._courselist[i]))
                continue
            elif( movePat.match(cid) ):
                indextoken = movePat.search(cid)
                sind = int(indextoken.group(1))
                eind = int(indextoken.group(2))
                # locate course in current location
                self._courselist.insert(eind, self._courselist.pop(sind))
                continue
            elif( len(cid) == 0 ):
                continue

    
            # Course name
            name   = input('Course Name [none]: ').upper()
            #if( len(name) == 0 ):
            #    print('Entry is empty. Restarting THIS course entry')
            #    continue
            #elif( nonePat.match(name) ):
            #    name = ''


            # Availability
            avail  = input('Offered [FWSs]:     ')
            availarr = []
            allQuarters = False
            if( len(avail) == 0 ):
                allQuarters = True
            if('F' in avail or allQuarters):
                availarr.append('FALL')
            if('W' in avail or allQuarters):
                availarr.append('WINTER')
            if('S' in avail or allQuarters):
                availarr.append('SPRING')
            if('s' in avail or allQuarters):
                availarr.append('SUMMER')
            if( len(availarr) == 0 ):
                print('Symbol(s) not understood. Restarting THIS course entry')
                continue


            # Prereqs
            prestr = input('Prereqs [seed]:     ')
            pre    = prestr.upper().split(' ')
            if( len(prestr) == 0 ):
                pre = 'SEED'
                seedcourse = True
                print('Logged as seed course.')


            # Course Load
            clstr  = input('Course Load [1]:    ')
            if( len(clstr) == 0 ):
                cl = 1
            else:
                cl = int(clstr)

            courseDescription = {'name': name, 'id': cid, 'avail': availarr, 'pre': pre, 'load': cl}

            print('Course Description:\n{0}'.format(courseDescription))
            if( input('Course description valid? [n] ').lower() == 'n' ):
                print('Restarting THIS course entry.')
                continue
            
            return courseDescription, seedcourse




    def generate(self, keepExisting=True):

        print(helpmessage_gen)

        #keep the existing courses in the provided json
        if( keepExisting ):
            with open(self._filepath, 'r') as fp:
                self._courselist = json.load(fp)

        newcourse = self.makeCourse()

        while( bool(newcourse[0]) ):
            if( newcourse[1] ): #if course is seed course
                self._courselist.insert(0, newcourse[0])
            else:
                self._courselist.append(newcourse[0])
            newcourse = self.makeCourse()

        print('Collected data. Writing to file: {0}'.format(self._filepath))
        with open(self._filepath, 'w+') as fp:
            json.dump(self._courselist, fp)
        
        
        return


