#
# Property of Ratnodeep Bandyopadhyay
# All rights reserved. Nov 2020.
#

from enum import Enum
import pdb

class Quarters(Enum):
    FALL   = 'FALL'
    WINTER = 'WINTER'
    SPRING = 'SPRING'
    SUMMER = 'SUMMER'




class Course:
    def __init__(self, name, cid, avail, pre, load):
        self._name  = name  # string
        self._id    = cid   # string
        self._avail = avail # list
        self._pre   = pre   # list
        self._load  = load  # number


    def __str__(self):
        return self._id

    def __repr__(self):
        return 'Name: {0}\nID: {1}\nAvail: {2}\nPreq: {3}\nLoad: {4}'.format(self._name, self._id, self._avail, self._pre, self._load)

    def amIPre(self, crsObj):
        return ( self._id in crsObj._pre )

    def wasThatPre(self, crsObj):
        return ( crsObj._id in self._pre )

    def isOffered(self, quarter):
        return (quarter in self._avail)





class QuarterList:
    def __init__(self, quarter):
        self._quarter = quarter
        self._quarterlist = []


    def roomExists(self, courses, checkCourse, maxload):
        return ((maxload - checkCourse._load) >= 0)


    def preNotInQuarter(self, checkCourse, coursesInQuarter):
        #pdb.set_trace()
        for course in coursesInQuarter:
            if course._id in checkCourse._pre:
                return False
        return True


    # in order for a course to be added:
        # the course must be offered
        # the course must have all preqs sorted
        # there must be room
    def addCourses( self, courselistObj, maxload ):
        newQuarterCourses = []
        duplicateCourselist = list(courselistObj._courselist)
        for course in duplicateCourselist:
            #print(course, ' ', self._quarter) #dbg
            #pdb.set_trace() #dbg
            if( course.isOffered(self._quarter) and courselistObj.checkPreqsSorted(course) and self.roomExists(newQuarterCourses, course, maxload) and self.preNotInQuarter(course, newQuarterCourses) ):
                newQuarterCourses.append(course)
                maxload = maxload - course._load
                courselistObj._courselist.remove(course)

        self._quarterlist.append(newQuarterCourses)

        return

