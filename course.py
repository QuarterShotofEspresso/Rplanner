from enum import Enum

class Quarters(Enum):
    FALL   = 'FALL'
    WINTER = 'WINTER'
    SPRING = 'SPRING'
    SUMMER = 'SUMMER'




class Course:
    def __init__(self, name, cid, avail, pre, load):
        _name  = name  # string
        _id    = cid   # string
        _avail = avail # list
        _pre   = pre   # list
        _load  = load  # number

    def amIPre(crsObj):
        return ( self._id in crsObj._pre )

    def wasHePre(crsObj):
        return ( crsObj._id in self._pre )

    # debugging methods
    def printCourse(self):
        print('Name: {0}\tID: {1}\tAvail: {2}\tPreq: {3}'.format())
        return

    def isOffered(self, quarter):
        return (quarter in self._avail)





class QuarterList:
    def __init__(self, quarter, courseload):
        _quarter = quarter
        _quarterList = []
        _courseload = courseload


    def roomExists(self, courses, checkCourse):
        currentload = self._courseload
        for course in courses: currentload = currentload - course._load
        return ((currentload - checkCourse._load) >= 0)


    # in order for a course to be added:
        # the course must be offered
        # the course must have all preqs sorted
        # there must be room
    def addCourses( coursesToAdd, courselist ):
        newQuarterCourses = []
        for i,course in enumerate(courselist):
            if( course.isOffered(self._quarter) and courselist.checkPreqsSorted(course) and self.roomExists(newQuarterCourses, course) ):
                newQuarterCourses.append(course)
                coursesToAdd = coursesToAdd - course._courseload
                courselist.pop(i)

        self._quarterlist.append(newQuarterCourses)

        return

