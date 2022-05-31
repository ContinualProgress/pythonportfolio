#!/usr/bin/python3

# Given the file "student_subject_scores_v1.txt", programatically find the following:
# 1. Number of students
# 2. Third lowest scorer in Geography
# 3. Student(s) absent in any of the subject exam
# 4. Student with highest average score across all subjects
# 5. Save the scores for each student in new individual files

import operator
from pprint import pprint

numStudents = set()
grades = {}
averageScore = {}

dataFile = "testfile.txt"

#Populate grades dictionary
with open(dataFile) as f:
    #Discard the first line
    f.readline()
    for line in f:
        subject, student, score = line.split()
        #If the subject is not part of the grades dictionary, add it.
        if subject not in grades:
            grades[subject] = {}
        grades[subject][student] = score

#Create a structure of unique students.
for item in grades.keys():
    numStudents.update(grades[item].keys() )


#Calculate third lowest grade in geography.
thirdLowestInGeography = sorted(grades["Geography"].items(), key=operator.itemgetter(1) )[2]

#Calculate students missing from each subject.
for item in grades.keys():
    classSet = set(grades[item].keys() )
    if len(numStudents.difference(classSet) ) == 0:
      print("The missing students from {0}: {1}".format(item, "None"))
    else:
      print("The missing students from {0}: {1}".format(item, numStudents.difference(classSet)))

#Calculate student with highest average score across all subjects
for student in numStudents:
    score = 0
    for subject in grades.keys():
        if student in grades[subject].keys():
            #print("Student: {}, Subject: {}, Score: {}".format(student, subject, grades[subject][student]) )
            score += int(grades[subject][student] )
    averageScore[student] = score/len(grades.keys() )
    highestAverage = sorted(averageScore.items(), key=operator.itemgetter(1))[-1]


#Place grades for a particular student in a file.
for student in numStudents:
    studentFile = "{}.csv".format(student)
    with open(studentFile, "w") as studentLog:
        for subject in grades.keys():
            if student in grades[subject].keys():
                studentLog.write("{}: {}\n".format(subject, grades[subject][student]) )

#pprint(grades)
#pprint(numStudents)

print("Number of students: {}".format(len(numStudents) ) )
print("Third lowest Grade in Geography: {}".format(thirdLowestInGeography) )
print("Highest average across all courses: {}".format(highestAverage) )
