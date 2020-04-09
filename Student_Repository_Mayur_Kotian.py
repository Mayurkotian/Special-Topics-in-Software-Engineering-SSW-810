"""This assignment is about creating a repository for each university storing data about 
its students ,instructors ,grades and majors by reading four txt files , computing GPA, adding new columns as required and electives 
and then printing out the pretty table"""

from HW08_Mayur_Kotian import file_reader
from prettytable import PrettyTable
from typing import Dict, DefaultDict, List
from collections import defaultdict
import os

class Major: 
    """Major stores major, required ,and electives courses and computes gpa to print it out using pretty table"""
    Passing_grades:List[str] = ['A','A-','B+','B-','C+','C'] 

    def __init__(self, major:str) -> None:  
        """Initializes Major instances with major ,required and elective lists for each major """
        self._major = major
        self._required:List[str] = list() 
        self._electives:List[str] = list() 
 
    def add_course(self, flag , course) -> None:
        """add courses according to the flag value (R or E) to their respective lists"""
        if flag == 'R':
            self._required.append(course)
        elif flag == 'E':
            self._electives.append(course)
        else:
            print(f"The flag was neither R or E. This {flag} is not valid. ")

    def get_required(self) -> None:
        """returns a new list copy of required list"""
        return list(self._required)

    def get_elective(self) -> None:
        """return a new list copy of elective list"""
        return list(self._electives)

    def info(self) ->  List[str]:
        """ info has data in format of major, sorted list of required courses and sorted list of elective courses for pretty table. """
        return [ self._major, sorted(self._required), sorted(self._electives)]

class Student:
    """Student stores cwid, names, major , completed courses, remaining courses, elective courses and stores course grades. """
    def __init__(self, cwid:str, name:str, major:str, required:List[str], elective:List[str]) -> None: 
        """Initializes Student instance with cwid , name, major, and course dict"""
        self._cwid:str = cwid
        self._name:str = name 
        self._major:str = major
        self._courses: Dict[str,str] = dict()  # _courses[course] = grade
        self._grades: Dict[str,float] = {'A':4.0,'A-':3.75,'B+':3.25,'B':3.0,'B-':2.75,'C+':2.25,'C':2.0} 
        self._remaining_required: List[str] = required 
        self._remaining_electives: List[str] = elective 

    def compute_grades(self) -> None :
        """compute_grades calculates each students GPA and returns it to the pretty table. """
        sumlist:List[float]= list()
        for v in self._courses.values() :
            if v in self._grades:
                sumlist.append(self._grades[v])
            else:
                return 0
        if len(sumlist) == 0:
            gpa:float  = 0
        else:
            gpa:float = sum(sumlist)/ len(sumlist) 
        return(format(gpa,'.2f'))  

    def store_course_grade(self, course:str, grade:str) -> None:
        """store course grade stores grades into courses dictionary with key as course. """
        Passing_grades:List[str] = ['A','A-','B+','B','B-','C+','C'] 
        if grade in Passing_grades:    
            self._courses[course] = grade
            if course in self._remaining_required:
                self._remaining_required.remove(course)
            if course in self._remaining_electives:
                self._remaining_electives.clear()
                
    def info(self):
        """ info has data in format of cwid, name, major, and course and grades for pretty table just in order of pretty table header. """
        return [self._cwid, self._name, self._major, sorted(self._courses.keys()),sorted(self._remaining_required),sorted(self._remaining_electives),self.compute_grades()]

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
        """Initializes student , instructor , major dict to create instance for each student, major and instructor to then print it on pretty table for major, students and instructors."""
    
        self._path:str = path 
        self._students: Dict[str, Student]= dict()              
        self._instructors: Dict[str, Instructor]= dict()   
        self._majors:Dict[str, Major]= dict()

        self._read_majors()
        self._read_students()
        self._read_instructors()
        self._read_grades()

        self.major_pretty_table()
        self.student_pretty_table()
        self.instructor_pretty_table()

    def _read_majors(self) -> None:
        """read_majors read the txt files and using file reader [Major, Flag, Courses]"""
        try:
            for major, flag, course in file_reader(os.path.join(self._path, 'majors.txt'), 3 , sep ='\t', header = True):
                if major not in self._majors:
                    self._majors[major] = Major(major)             
                self._majors[major].add_course(flag,course) 

        except FileNotFoundError:
            raise FileNotFoundError("The stated file for reading majors is not found at the given file address")

        except ValueError:
            print(ValueError) 

    def _read_students(self) -> None:
        """read_students reads the txt files and using file reader, the data is fed into student object for every single student"""
        try:
            for cwid, name, major in file_reader(os.path.join(self._path, 'students.txt'), 3 , sep =';', header = True): 
                required = self._majors[major].get_required()
                elective = self._majors[major].get_elective()
                self._students[cwid] = Student(cwid, name, major, required, elective )

        except FileNotFoundError:
            raise FileNotFoundError("The stated file for reading student is not found at the given file address ")

        except ValueError:
            print(ValueError) 

    def _read_instructors(self) -> None:
        """read_instructor reads the txt files and using file reader, the data is fed into instructor object for every  single instructor """
        try:
            for instructor_cwid, name, dept in file_reader(os.path.join(self._path, 'instructors.txt'), 3 , sep ='|', header = True): 
                self._instructors[instructor_cwid] = Instructor(instructor_cwid, name, dept)
        
        except FileNotFoundError:
            raise FileNotFoundError("The stated file for reading instructor is not found at the given file address ")

        except ValueError:
            print(ValueError) 

    def _read_grades(self) -> None: 
        """read_grades reads the txt files using file reader, and then add grades to student/instructor """
        
        try:
            for student_cwid, course, grade, instructor_cwid in file_reader(os.path.join(self._path, 'grades.txt'), 4 , sep ='|', header = True):
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
            raise FileNotFoundError("The stated file for reading grade is not found at the given file address ")

        except ValueError:
            print(ValueError) 

    
    def student_pretty_table(self) -> None:
        """student_pretty_table prints a pretty table for students """
        pt = PrettyTable(field_names = ['CWID', 'Name', 'Major', 'Complete Courses','Remaining Required','Remaining Elective','GPA']) 
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

    def major_pretty_table(self) -> None:  
        """Major_pretty_table prints a pretty table for user to read information about majors and required courses. """
        pt = PrettyTable(field_names = ['Major', 'Required Courses', 'Electives']) 
        for majorval in self._majors.values():
            pt.add_row(majorval.info())

        print(pt)

def main():
    """Defined all sorts of possible repositories to check the exceptions"""
    stevens: Repository = Repository(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_10\Stevens")

if __name__ == '__main__':
    main()