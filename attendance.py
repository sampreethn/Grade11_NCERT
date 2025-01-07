num_students=int(input("Enter the number of students :: "))
students = []
for i in range(num_students):
    print("Enter the name of the student ",i+1," : ")
    name=input()
    students.append(name)
students=tuple(students)
find_name=input("Enter a name to find : ")
def search_name():
    item=find_name
    if item in students:
        print("\nName found\n")
        
#     elif item!=find_name:
    else:
        print("\nName not found\n")
    return
search_name()


    