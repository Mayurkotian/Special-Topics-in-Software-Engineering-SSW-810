"""This assignment is about creating a repository for each university storing data about 
its students , instructors by reading three txt files and printing out the pretty table"""

from HW08_Mayur_Kotian import file_reader
from prettytable import PrettyTable
from typing import Dict, DefaultDict, List
from collections import defaultdict
import os

class Student:
    """Student stores cwid, names, major and stores course grades. """
    def __init__(self, cwid:str, name:str, major:str) -> None:
        """Initializes Student instance with cwid , name, major, and course dict"""
        self._cwid:str = cwid
        self._name:str = name 
        self._major:str = major
        self._courses: Dict[str,str] = dict()           

    def store_course_grade(self, course:str, grade:str) -> None:
        """store course grade stores grades into courses dictionary with key as course. """
        self._courses[course] = grade

    def info(self):
        """ info has data in format of cwid, name, major, and course and grades for pretty table just in order of pretty table header. """
        return [self._cwid, self._name, self._major, sorted(self._courses.keys())]

class Instructor:
    """Instructors stores instructor cwid , names , dept and also stores courses with number of students for that professor."""
    def __init__(self, instructor_cwid:str, name:str, dept:str) -> None:
        self._instructor_cwid:str = instructor_cwid
        self._name:str = name 
        self._dept:str = dept
        self._courses: DefaultDict[str,int] = defaultdict(int) 
        
    def store_course_student(self,course:str):
        """This counts number of students in each class for that professor's courses. """
        self._courses[course] += 1
        
    def info(self):
        """ info has data in format of cwid, name, dept, and course and number of students for pretty table just in order of pretty table header. """
        for key, value in self._courses.items():
            yield [self._instructor_cwid, self._name, self._dept, key, value]

class Repository:
    """This repository takes in the path of the file and stores all data from the txt files and prints the pretty table. """
    def __init__(self, path:str) -> None:
        """Initializes student , instructor dict to create instance for each student and instructor to then print it on pretty table for students and instructors."""
    
        self._path:str = path 
        self._students: Dict[str, Student]= dict()             
        self._instructors: Dict[str, Instructor]= dict()       
        self._read_students()
        self._read_instructors()
        self._read_grades()
        self.student_pretty_table()
        self.instructor_pretty_table()

#################### READ DATA FROM TXT FILES  ##############################

    def _read_students(self) -> None:
        """read_students reads the txt files and using file reader, the data is fed into student object for every single student"""
        try:
            for cwid, name, major in file_reader(os.path.join(self._path, 'students.txt'), 3 , sep ='\t', header = False):
                self._students[cwid] = Student(cwid, name, major)
        
        except FileNotFoundError:
            raise FileNotFoundError("The stated file for reading student is not found ")

        except ValueError:
            raise ValueError

    def _read_instructors(self) -> None:
        """read_instructor reads the txt files and using file reader, the data is fed into instructor object for every  single instructor """
        try:
            for instructor_cwid, name, dept in file_reader(os.path.join(self._path, 'instructors.txt'), 3 , sep ='\t', header = False):
                self._instructors[instructor_cwid] = Instructor(instructor_cwid, name, dept)
        
        except FileNotFoundError:
            raise FileNotFoundError("The stated file for reading instructor is not found ")

        except ValueError:
            raise ValueError

    def _read_grades(self) -> None: 
        """read_grades reads the txt files using file reader, and then add grades to student/instructor """
        
        try:
            for student_cwid, course, grade, instructor_cwid in file_reader(os.path.join(self._path, 'grades.txt'), 4 , sep ='\t', header = False):
                if student_cwid in self._students:
                    s: Student = self._students[student_cwid]
                    s.store_course_grade(course, grade)
                else:
                    print(f"No such student with cwid {student_cwid} has  grade {grade}. ")
                        
                if instructor_cwid in self._instructors:
                    inst: Instructor = self._instructors[instructor_cwid]
                    inst.store_course_student(course)
                else:
                    print(f"No such instructor with cwid {instructor_cwid} has grade {grade}. ")
            
        except FileNotFoundError:
            raise FileNotFoundError("The stated file for reading grade is not found")

        except ValueError:
            raise ValueError

####################  PRETTY TABLE ##############################
    def student_pretty_table(self) -> None:
        """student_pretty_table prints a pretty table for students """
        pt = PrettyTable(field_names = ['CWID', 'Name', 'Major', 'Courses']) 
        for stu in self._students.values():
            pt.add_row(stu.info())

        print(pt)

    def instructor_pretty_table(self) -> None:
        """instructor_pretty_table prints a pretty table for instructors """
        pt = PrettyTable(field_names =  ['Cwid', 'Name', 'Dept', 'Course', 'Students'])
        for instval in self._instructors.values():
            for row in instval.info():
                pt.add_row(row)
        
        print(pt)

#################################################################
def main():
    """Defined all sorts of possible repositories to check the exceptions"""
    # stevens: Repository = Repository(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_9\Stevenswronggrade")
    # stevens:Repository = Repository(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_9\Stevensfields")
    # stevens: Repository = Repository(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_9\StevenValueerror")
    # stevens: Repository = Repository(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_9\Stevens")

if __name__ == '__main__':
    main()