#!/usr/bin/python3
from courselist import *
import sys


# use case:
helpmessage = """

 Rplanner is a course planning utility catered for Rside students.
 This could likely be used for other schools, it depends on course structure and
 hierarchy.
 Provide a json file containing details of each course.
 This json file can be created using the -g flag. See below.
 Each course requires:
    - name (Ex: Biomedical Ethics, Discrete Structures, Linear Algebra I)
    - id (Ex: PHIL009, cs111, or Math131)
    - availability (Fall, Winter, Spring, or Summer)
    - prerequisites (Provide by id)
    - course load (This is the perceived difficulty. See below for more info)
 With these inputs, Rplanner will generate a course plan using the least number
 of years possible.
 The number of years cannot be assigned and is dependent on the courses input.


 Use Cases:
    ./main.py <file> [-ns] [-s <file>] [-l <load>]
    ./main.py -h
    ./main.py -g <file>


 Flags:
    -g <file>   Launch course list generator.
    -h          Prints this message. Every other flag is ignored.
    -ns         No summer courses. (Default keeps summer courses)
    -s <file>   Print path to file. (Default prints to console)
    -l <load>   Maximum course load per quarter. (Defaults to 4)

 Example:
    ./main.py courses.json -ns -l 3 -s myschedule
    ./main.py courses.json -ns


 Course load:   Course load is the perceived difficulty of a class.
                Course load is NOT the units per class.
                If there is a difficult course, for example: CS111,
                whose difficulty could demand the time and effort of two
                courses, then the course load for CS111 would be 2.
                Similarly, the course load of a body-count class, like
                ENGR101, could be worth a quarter of the time and effort 
                of a regular class. Therefore, the course load for
                ENGR101 is 0.25.
                **Remember: Course load is entirely subjective.
                            This is just an example.



"""

def main():


    if (len(sys.argv) < 2):
        print('Incorrect useage. Type \'./<exec> -h\' for help.')
        return

    if ('-h' in sys.argv):
        print(helpmessage)
        return

    if ('-gO' in sys.argv):
        genfilepath = sys.argv[sys.argv.index('-gO') + 1]
        coursegen = GenerateCourseList(genfilepath)
        coursegen.generate('w+')
        return
    elif ('-gA' in sys.argv):
        genfilepath = sys.argv[sys.argv.index('-gA') + 1]
        coursegen = GenerateCourseList(genfilepath)
        coursegen.generate('a+')
        return
    elif ('-gL' in sys.argv):
        genfilepath = sys.argv[sys.argv.index('-gL') + 1]
        coursegen = GenerateCourseList(genfilepath)
        coursegen.list()
        return
        


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
    mycl.sortByPre()
    
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
        # print/save the file
        print(mycl)



main()


