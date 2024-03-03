list_1 = [1, 5, 3]
list_2 = [4, 2, 6]

zip_list = zip(list_1, list_2)
print(list(zip_list)[0])

'''
Imagine that you have two lists, the first one contains the students' names, and the second one contains their grade.

Now, we want to link each student with his grade in a dictionary called names_grades .

To do so, loop over the two lists at the SAME time and assign each student to his/her grade.

You should use : for loops, dictionaries, and zip
'''
students_names = ["Micheal Ford", "John Buch", "Isra Raul", "Messi Ronaldo"]
students_grades = [80, 53, 90, 100]

names_grades = {}

for a, b in zip(students_names, students_grades):
    names_grades[a] = b

print(names_grades)