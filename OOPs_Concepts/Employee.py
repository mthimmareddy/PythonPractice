
class Employee(object):
    #class variable
    counter=0
    name=None
    age=None
    dept=None
    def __init__(self,name=None,age=None,dept=None):
        Employee.counter+=1
        self.empId=Employee.counter
        self.name=name

        self.age=age
        self.dept=dept

    def setinfo(self,phone=1234):
        self.phone=phone

    def getvalues(self):
       return (self.empId,self.name,self.age,self.dept,self.phone)

    def set(self):
        pass

    @classmethod
    def getempcount(cls):
        return cls.counter

class Sales(Employee):
    def __init__(self,name,age,dept):
        super().__init__()
        self.name=name
        self.age=age
        self.dept=dept

    def salesoper(self):
        print("in sales")

if __name__=="__main__":
    a=Employee("manju","31","IT")
    a.counter=12
    print(a.counter)
    print(Employee.counter)
    a.setinfo(phone=2435678989)
    b=Employee("radha","33","sales")
    b.setinfo()
    print(a.getvalues())
    print(b.getvalues())
    #a.setinfo(phone=2435678989)
    print(Employee.getempcount())
    #c=Sales("raju",45,"it")
    #print(c.getvalues())
    #print(c.salesoper())