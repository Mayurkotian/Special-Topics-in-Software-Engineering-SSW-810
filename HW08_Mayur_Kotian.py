from datetime import datetime, timedelta 
from typing import Tuple,List, Dict, IO, Iterator
from prettytable import PrettyTable
import os
#PART1
#DATE ARITHMETIC

# def date_arithmetic() -> Tuple[datetime, datetime, int]:
#     """ date_arithmetic has date operations using datetime and timedelta 
#         to find number of days between two numbers and to find what date 
#         it would be after x number of days.
#     """
#     dt1:datetime = datetime.strptime("02/27/2020", "%m/%d/%Y")
#     dt2:datetime = datetime.strptime("02/27/2019", "%m/%d/%Y")
#     dd1:datetime = datetime.strptime("02/01/2019", "%m/%d/%Y")
#     dd2:datetime = datetime.strptime("09/30/2019", "%m/%d/%Y")

#     three_days_after_02272020: datetime = dt1 + timedelta(days = 3)
#     three_days_after_02272019: datetime = dt2 + timedelta(days = 3)
#     days_passed_02012019_09302019: int = (dd2-dd1).days 

#     return three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019
    
#PART2 
#FILE READER

def file_reader(path, field, sep = ',', header= False) -> Iterator[Tuple[str]]:
    """file_reader is a functions that reads a file and return words 
       from the file separated using sep value"""
    try:
        fp:IO = open(path,'r')
    except FileNotFoundError:
        raise FileNotFoundError(f" Can't open this {path}. Try again.")
    else:
        count:int = 0
        for row in fp:
            lines:List[str] = row.strip().split(sep)
            count +=1 

            if len(lines) != field:
                fp.close()
                raise ValueError(f"File has {len(lines)} fields on line {count} but expected {field}. ")
            else:
                if header == False:
                    yield tuple(lines)
                elif count == 1 and header == True:
                    continue
                else:
                    yield tuple(lines)
    fp.close() 

#print(list(file_reader(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_8", 3, sep='|')))

# def openfile(path:str) -> None:
#     fp = open(path,'r')
#     with fp:
#         for rows in fp:
#             print(rows)
# openfile(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_8")
# # # #PART3
# # #PRETTY TABLE

# class FileAnalyzer:
#     """FileAnalyzer is a class which has method used to summarize each file
#         and printing them out using prettytable"""
#     def __init__(self, directory) -> None:
#         """Initializing values for class FileAnalyzer"""
#         self.directory:str = directory
#         self.files_summary:Dict[str,Dict[str,int]] = dict()
#         self.analyze_files()
    
#     def analyze_files(self) -> None:
#         """To analyze the file ending with .py file and count the num of 
#             characters , rows , classes and methods to summarize them in 
#             a dictionary"""
#         try:
#             path:str = self.directory
#             files:List[str] = os.listdir(path)
#         except FileNotFoundError: 
#             raise FileNotFoundError("Cant open this file. The path provided is not correct.")
#         else:
#             for n in files:
#                 if n.endswith(".py"):
#                     try: 
#                         fp:IO = open(os.path.join(path, n),'r')
#                     except FileNotFoundError:
#                         raise FileNotFoundError(f"Error: Can't Open this file: {n}")
#                     else:
#                         char:int = 0
#                         line:int = 0 
#                         classes:int = 0
#                         method:int = 0

#                         for rows in fp:
#                             lines:List[str] = rows.strip().split('\n')
#                             line +=1 
#                             for words in lines:
#                                 char += len(words) 
#                                 if words.startswith('def'):
#                                     method +=1
#                                 elif words.startswith('class'):
#                                     classes +=1 
#                                 else:
#                                     continue 
#                     fp.close()            
#                     self.files_summary[n] = {"class": classes, "function": method, "line": line, "char": char}

#     def pretty_print(self) -> None:
#         """ To print of the summarized data into a table format with structure using 
#             prettytable """
#         table:object = PrettyTable()
#         table.field_names = ["File Name", "Classes", "Functions", "Lines", "Characters"]
#         for i, j in self.files_summary.items():
#             table.add_row([i, j["class"], j["function"], j["line"], j["char"]])
#         return table
                    

