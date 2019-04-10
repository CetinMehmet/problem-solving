  """
  Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
  Your task is to help Dr. Wesley calculate the average marks of the students.
  1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet. 
  2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)
"""

from collections import namedtuple

(n, categories) = (int(input()), input().split())
Grade = namedtuple('Grade', categories)

marks = []
for _ in range(n):
  marks.append(Grade._make(input().split()).MARKS)

print(sum(map(int,marks))/n)
