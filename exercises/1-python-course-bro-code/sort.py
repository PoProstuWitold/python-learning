# sort() method   = used with lists
# sort() function = used with iterables

# list of tuples
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

grade = lambda grades:grades[1]
age = lambda ages:ages[2]
# students.sort(key=age)                                       # sorts current list
sorted_students_by_grade = sorted(students,key=grade) # sorts and creates a new list
sorted_students_by_age = sorted(students,key=age) # sorts and creates a new list

print("Sorted by grade")
for i in sorted_students_by_grade:
    print(i)
    
print("Sorted by age")
for i in sorted_students_by_age:
    print(i)