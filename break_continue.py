
my_list= [1, 3.14, "stop", 5, "stop", 2]
for i in my_list:
    if i == "stop":
        break
    print(i)  # 1
              # 3.14

my_list= [1, 3.14, "stop", 5, "stop", 2]
for i in my_list:
    if i == "stop":
        continue
    print(i) # 1
             # 3.14
             # 5
             # 2

'''
Imagine that we have a list of ages that we scraped from a website.

Now, we want to store only the even ages so we can perform some analysis on them.

You should do that by using for loops, if conditions and continue statement. Don't use else

Store the filtered ages in a list called ages_even

'''

list_ages = [10, 11, 19, 7, 8, 24, 91, 74, 25, 53, 41, 50, 63, 86]
ages_even = []

for i in list_ages:
    if i % 2 == 1:
        continue
    ages_even.append(i)
print(ages_even)