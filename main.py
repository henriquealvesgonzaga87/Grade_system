# 1st step - make the interface
# 2nd step - make the system to add the data
# 3rd step - check if the file exists, if not, create one
# 4th step - read the file and add students
# 5th step - make a costumized interface
from lib.Interface import *
from lib.functions import *

file = 'data.txt'

if not checkfile(file):
    creatfile(file)
while True:
    option = menu(['Show Students', 'Add new student', 'Exit'])
    if option == 1:
        readfile(file)
    elif option == 2:
        name = str(input('Name: ')).strip().title()
        if not name.isalpha():
            name = str(input('Type a valid name: ')).strip().title()
        grades = list()
        for c in range(1, 4):
            n = readfloat(f'{c}º grade: ')
            grades.append(n)
        average = sum(grades) / len(grades)
        situation = ''
        if average >= 60:
            situation = 'Approved'
        elif average >= 40:
            situation = 'Retake Test'
        else:
            situation = 'Repproved'
        students = addstudents(file, name, grades, average, situation)
    elif option == 3:
        header('Exiting! See you soon!')
        break
    else:
        print('Option not valid!')
