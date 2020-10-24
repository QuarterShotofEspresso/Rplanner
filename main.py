#!/usr/bin/python3
from courselist import *

# use case:
"""

main.py <course_list_json> [-ns] [-s <save_file_path>] [-p]
    create plan

main.py -h
    Prints this message

"""

def main():

    # enter the input file
    filepath = input('Path to course details: '))
    # read prerequisits and populate into a course list
    # first course must be a seed course: a course with no course-pres
    mycl = CourseList()
    mycl.populateCourseList(filepath)

    mycl.sortByPre()
    
    # sort all courses into respective quarters
    # make sure each class is not going to lose prereq sort
        # flag: -m <max_classes_per_quarter>
        # flag: -ns ### no summer classes (don't include -ns for summer classes)
    mycl.sortIntoQuarters(classesPerQuarter)
    # generate table using pretty table module
    mycl.generateRplanner()
`   # print/save the file
    mycl.printRplanner()
        # use flag -s <file_path>
    mycl.saveRplanner(saveFilepath)

