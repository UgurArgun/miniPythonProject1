names = ["Rachael Green", "Goodfellow Ian", "Tedd Crock", "Mina Joseph"]
salaries = [10260, 41571, 71211, 52141, 35781]
people_salaries = []

for i, j in enumerate(names):
    x = j + " $" + str(salaries[i])
    people_salaries.append(x)

print(people_salaries)