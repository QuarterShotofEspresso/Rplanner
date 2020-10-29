from enum import Enum

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


    def __repr__(self):
        return 'Name: {0}\tID: {1}\tAvail: {2}\tPreq: {3}'.format(self._name, self._id, self._avail, self._pre, self._load)

    def amIPre(self, crsObj):
        return ( self._id in crsObj._pre )

    def wasHePre(self, crsObj):
        return ( crsObj._id in self._pre )

    def isOffered(self, quarter):
        return (quarter in self._avail)





class QuarterList:
    def __init__(self, quarter):
        self._quarter = quarter
        self._quarterlist = []


    def roomExists(self, courses, checkCourse):
        currentload = self._courseload
        for course in courses: currentload = currentload - course._load
        return ((currentload - checkCourse._load) >= 0)


    # in order for a course to be added:
        # the course must be offered
        # the course must have all preqs sorted
        # there must be room
    def addCourses( self, courseload, courselist ):
        newQuarterCourses = []
        for i,course in enumerate(courselist):
            if( course.isOffered(self._quarter) and courselist.checkPreqsSorted(course) and self.roomExists(newQuarterCourses, course) ):
                newQuarterCourses.append(course)
                courseload = courseload - course._courseload
                courselist.pop(i)

        self._quarterlist.append(newQuarterCourses)

        return

