#!/usr/bin/python3
from courselist import *
import sys

# use case:
helpmessage = """

 Rplanner is a simple python script that designs a course plan for Rside students.
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
 With this inputs, Rplanner will generate an n-year course plan.
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

    if ('-h' in sys.argv):
        print(helpmessage)
        return

    if ('-g' in sys.argv):
        generateCoursePlan()
        return


    # enter the input file
    if( '-s' in sys.argv ):
        filepath = sys.argv[sys.argv.find('-s') + 1]
    # read prerequisits and populate into a course list
    # first course must be a seed course: a course with no course-pres
    mycl = CourseList()
    mycl.populateCourseList(filepath)

    mycl.sortByPre()
    
    # sort all courses into respective quarters
    # make sure each class is not going to lose prereq sort
        # flag: -m <max_classes_per_quarter>
        # flag: -ns ### no summer classes (don't include -ns for summer classes)
    maxload = 4
    if( maxload
    mycl.sortIntoQuarters(classesPerQuarter)
    # generate table using pretty table module
    mycl.generateRplanner()
    # print/save the file
    mycl.printRplanner()
        # use flag -s <file_path>
    mycl.saveRplanner(saveFilepath)



main()

