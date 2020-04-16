import unittest
from Student_Repository_Mayur_Kotian import Repository, Student, Instructor, Major
from typing import List,Dict
from prettytable import PrettyTable
import sqlite3


class StudentRepositoryTestCase(unittest.TestCase):
    """This class is used to test all the possible test cases on each class and verifies the test values. """
    def test_class_student(self):
        """ test_class_student is to test if the values provided to the pretty table are correct or not"""
        stevens: Repository = Repository(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_11\Stevens")
        list1 = list()
        list2 = [['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [], '3.38'], ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546'], '4.00'], ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546'], '4.00'], ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], [], [], '3.50']]
        for stu in stevens._students.values():
            list1.append(stu.info())

        self.assertEqual(list1, list2)

    def test_class_instructor(self):
        """ test_class_instructor is to test if the values provided to the pretty table are correct or not """
        stevens: Repository = Repository(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_11\Stevens")
        list1 = list()
        list2 = [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1], ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4], ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1], ['98762', 'Hawking, S', 'CS', 'CS 501', 1], ['98762', 'Hawking, S', 'CS', 'CS 546', 1], ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]
        for instval in stevens._instructors.values():
            for row in instval.info():
                list1.append(row)

        self.assertEqual(list1, list2)

    def test_class_major(self):
        """ test_class_major is to test if the values provided to the pretty table are correct or not"""
        stevens: Repository = Repository(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_11\Stevens")
        list1 = list()
        list2 = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']], ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]]
        for stu in stevens._majors.values():
            list1.append(stu.info())
                
        self.assertEqual(list1, list2)

    def test_studentdf(self):
        """ test_studentdf is to test if the values provided to the pretty table are correct or not when retrived from the database. """
        dblink = "C:/Program Files/JetBrains/DataGrip 2020.1/bin/studentdb.db"
        db: sqlite3.Connection = sqlite3.connect(dblink)
        query:str= "select students.Name as Student_Name, students.CWID, grades.Course, grades.Grade, instructors.Name as Instructor_Name from ((students inner join grades on students.CWID = grades.StudentCWID) inner join instructors on grades.InstructorCWID = instructors.CWID) order by Student_Name ASC;"        
        list1 = list()
        list2 = [('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'), ('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'), ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'), ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'), ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'), ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'), ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'), ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'), ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J')]
        for row in db.execute(query):
            list1.append(row)

        self.assertEqual(list1, list2)

    

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
            








