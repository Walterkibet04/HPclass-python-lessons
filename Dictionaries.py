student = {
    "name": "walter",
    "course": "fullstack web development",
    "Gender": "male"
}
print(student)
print(student["name"])
print(len(student))
print(type(student))

# output
# {'name': 'walter', 'course': 'fullstack web development', 'Gender': 'male'}
# walter
# 3 
# <class 'dict'>

#Get a list of the keys

get = student.keys()
print(get) 

#output
#dict_keys(['name', 'course', 'Gender'])

#loop dictionaries
for x in student:
    print(x)

#output
# name
# course
# Gender


#Print all values in the dictionary, one by one
for x in student:
  print(student[x])

#output
# walter
# fullstack web development
# male