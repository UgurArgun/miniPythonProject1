'''
Imagine that we have a dictionary that contains the students' names and grades.

Now, we want to filter out the students who passed - above 50 - and get their first names in a list called passed_students_names

But instead of doing it the long way with too many lines, I want you to challenge yourself and do it in just one line of code.

Hints :

You are going to need the items function in the dictionary.

You are going to need the split function in the string.

You are going to need the string slicing and indexing.

You are going to need the if statement.

You need to do everything in one line, so you need list comprehension.

This exercise is a little bit advanced, so take your time.
'''
students_dict = {
                    "Joel Corry" : 70,
                    "James Bond" : 90,
                    "Fatma Ahmed": 20,
                    "Lily Saqr"  : 94,
                    "Ahmed Yan"  : 40,
                }
passed_students_names = [name.split()[0] for name, x in students_dict.items() if x > 50]

print(passed_students_names)