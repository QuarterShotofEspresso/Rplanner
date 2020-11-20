#!/usr/bin/python3
#
# Property of Ratnodeep Bandyopadhyay
# All rights reserved. Nov 2020.
#

from courselist import *
from generator import *
import sys


helpmessage = ''
with open('README.md', 'r') as fp:
    helpmessage = fp.read()


def main():

    if (len(sys.argv) < 2):
        print('Incorrect usage. Type \'./<exec> -h\' for help.')
        return

    if ('-h' in sys.argv):
        print(helpmessage)
        return

    if ('-gO' in sys.argv):
        genfilepath = sys.argv[sys.argv.index('-gO') + 1]
        coursegen = GenerateCourseList(genfilepath)
        coursegen.generate(False)
        return

    elif ('-g' in sys.argv):
        genfilepath = sys.argv[sys.argv.index('-g') + 1]
        coursegen = GenerateCourseList(genfilepath)
        coursegen.generate()
        return
    
    # look for -dc flag to avoid clumping related courses
    clumpRelated = (not '-dc' in sys.argv)
    #print(clumpRelated)

    # enter the input file
    coursefilepath = sys.argv[1]
    # read prerequisits and populate into a course list
    # first course must be a seed course: a course with no course-pres
    mycl = CourseList(('-ns' in sys.argv))
    mycl.populateCourseList(coursefilepath)


    # NOTE: Do I even need this method?
    # Think about the algo a little more.
    # This method may be redundant
    #pdb.set_trace() #dbg
    mycl.sortByPre(clumpRelated)
    
    # sort all courses into respective quarters
    # make sure each class is not going to lose prereq sort
        # flag: -l <max_classes_per_quarter>
        # flag: -ns ### no summer classes (don't include -ns for summer classes)
    maxload = 4
    if( '-l' in sys.argv ):
        maxload = sys.argv[sys.argv.index('-l') + 1]

    #pdb.set_trace() #dbg

    mycl.fileIntoQuarters(maxload)
    # generate table using pretty table module
    mycl.generateRPlanner()

    if( '-s' in sys.argv ):
        saveFilepath = sys.argv[sys.argv.index('-s') + 1]
        # use flag -s <file_path>
        mycl.saveRPlanner(saveFilepath)
    else:
        # print plan
        print(mycl)



main()


