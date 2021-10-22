import random

#print(random(12,34))

class Employee(object):
    empId=99
    count=0
    def __init__(self,name):
        #print(random(1,10))
        Employee.empId=Employee.empId+1
        self.name=name
        Employee.count=Employee.count+1

        #print(Employee.count)
    def getprint(self):
        return (Employee.empId,self.name)

    @classmethod
    def emp_count(cls):
        return Employee.count
    

if __name__=="__main__":
    A=Employee("manjula")
    B=Employee("Tushar")
    print(A.getprint())
    print(B.getprint())
    print(Employee.emp_count())


