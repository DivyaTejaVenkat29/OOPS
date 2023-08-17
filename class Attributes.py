class Student:
    # class variable
    school_name='ABC School'

    #Constructor
    def __init__(self,name,age):
        #instance variable
        self.name=name
        self.age=age

s1=Student('rajevu', 23)
# access the instance variables
print('Student:',s1.name,s1.age)

#access the class variable
print('School name:',Student.school_name)

#modify the instance variables
s1.name='araya'
s1.age=21
print('Student:',s1.name,s1.age)

#modify the class variables
Student.school_name='XYZ School'
print('School Name:',Student.school_name) 
