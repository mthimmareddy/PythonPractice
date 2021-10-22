

class Checkprime(object):

    def __init__(self,num):
        self.num=num

    def __check(self):
        for x in range(2,self.num):
            if self.num %x!=0:
                return True
            else:
                return False
    def displaycheck(self):
        return self.__check()



class Employee(object):
    empId=0
    def __init__(self, name):
        self.name = name
        Employee.empId += 1
        self.EmpId=Employee.empId
        #Employee.empId+=1

    def get_empdetails(self):
        return self.name,self.EmpId
    def get_CountEmp(self):
        return Employee.empId


if __name__=="__main__":
    a=Checkprime(19)
    b=Employee("manju")
    c = Employee("sanju")
    print(b.get_CountEmp())
    print(b.get_empdetails())
    print(a.displaycheck())