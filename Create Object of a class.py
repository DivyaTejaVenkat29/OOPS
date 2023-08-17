class Person:
    def __init__(self,name,sex,profession):
    # data members (instance variables)
        self.name=name
        self.sex=sex
        self.profession=profession
    # behavior members (instance methods)
    def show(self):
        print('Name:',self.name,'Sex:',self.sex,'Profession:',self.profession)
    
    #behavior members (instance methods)
    def work(self):
        print(self.name,'working as a',self.profession)

#create object of the class
jessa =Person('Jessa','Female','Software Engineeer')

#call methods
jessa.show()
jessa.work()




