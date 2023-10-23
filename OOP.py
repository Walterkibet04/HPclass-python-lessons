class Cars:
    def __init__(self,type,model,color):
        self.type = type
        self.model = model
        self.color = color
    
    def display(self):
        print(f"i love {self.model} bla bla {self.type} bla bla {self.color}")

myObj = Cars("range rover","vogue","black")
myObj.display()
myObj2 = Cars("probox","toyota","gray")
myObj2.display()


class Students: 
    def __init__(self, name, course,gender):
        self.name = name 
        self.course = course
        self.gender = gender

    def Display(self):
        print("name: %s \ncourse: %s\n gender: %s" %(self.name, self.course,self.gender))

myObj = Students("Walter", "information tech", "male")

myObj.Display()

#inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("walter", "kibet")
x.printname()
