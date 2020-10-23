#!/usr/bin/python3
from courselist import *

def main():

    # enter the input file
    filepath = input('Path to course details: '))
    # read prerequisits and populate into a course list
    mycl = CourseList()
    mycl.populateCourseList(filepath)

    mycl.sortByPre()
    
    # sort all courses into respective quarters
    # make sure each class is not going to lose prereq sort
    mycl.sortIntoQuarters()

