# Lazy RPlanner
> Author: Ratnodeep Bandyopadhyay ([@QuarterShotofEspresso](https://github.com/QuarterShotofEspresso))

 Lazy Rplanner is course planning utility. This is targeted for my school
 (UCR) but this could likely be used for other schools, it depends 
 on course description and hierarchy. Read below for more information.
 It's 'lazy' because Rplanner will produce a course plan that will likely 
 use a low number of years, but it's unlikely to produce a plan 
 with the least number of years possible. Still, courses can
 be supplied out of order (with restrictions on seed courses) and 
 produce an effective and adaptable course plan.
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


## Use Cases:  
```
    ./main.py <file> [-ns] [-s <file>] [-l <load>]  
    ./main.py -h  
    ./main.py -g <file>
```


## Flags:  
```
    -g  <file>  Launch course list generator and load conents of existing course list.  
    -gO <file>  Launch course list generator and overwrite existing course list.
    -h          Prints this message. Every other flag is ignored.  
    -ns         No summer courses. (Default keeps summer courses)  
    -s  <file>  Print path to file. (Default prints to console)  
    -l  <load>  Maximum course load per quarter. (Defaults to 4)
```

## Example  
```
    ./main.py courses.json -ns -l 3 -s myschedule
    ./main.py courses.json -ns

```


## Notes
 Seed Courses:  Seed courses are courses that will be sorted into quarters
                first. This means these courses should have NO prerequisites.
                These courses are the first ones to complete in the upcoming
                quarters. Rplanner uses seed courses to list those 
                courses dependent on these later down in the course plan. To 
                signify a course is a seed course press ENTER or RETURN on 
                the prerequisite detils when generating the course list.


 Course load:   Course load is a versatile feature of rplanner.
                It enables the description of abstract details
                such as the perceived difficulty of a course and 
                concrete details like co-requisites all in one go.
                Remember that course load is NOT the units per class.  
  
                If there is a difficult course, for example: CS111,
                whose difficulty could demand the time and effort of two
                courses, then the course load for CS111 would be 2.
                Similarly, the course load of a body-count class, like
                ENGR101, could be worth a quarter of the time and effort 
                of a regular class. Therefore, the course load for
                ENGR101 is 0.25. A co-requisite like CS161 & CS161L
                could be logged as one course: CS161&L with a course
                load of 2.
                **Remember: Course load is subjective.
                            These are just examples.


