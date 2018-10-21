"""
Each student at a certain school speaks a number of languages. We need to determine which languges are spoken
by all the students, which languages are spoken by at least one student.
Given, the number of students, and then for each student given the number of languages they speak followed
by the name of each language spoken, find and print the number of languages spoken by all the students,
followed by a list the languages by name, then print the number of languages spoken by at least one student,
followed by the list of the languages by name. Print the languages in alphabetical order.
"""


n = int(input())
all = {input() for i in range (int(input()))}
only_schooler = all
for i in range (n-1):
    schooler = {input() for i in range (int(input()))}
    all.update(schooler)
    only_schooler &= schooler
print (len(only_schooler), '\n', *sorted(only_schooler, key = str))
print (len(all), '\n',  *sorted(all, key = str))