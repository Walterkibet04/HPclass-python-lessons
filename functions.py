def students(fullname,age,gender,course,institution):
    print(f"{fullname} is {age} pursuing {course}")

students("walter kibet", 25, "male","Information technology","UOE")

fruits = ["apples","mangoes","banana","oranges"]
try:
    for i in range(5):
        print(f"the index and element from the list is {i, fruits[1]}")
except:
    print("out of range")


