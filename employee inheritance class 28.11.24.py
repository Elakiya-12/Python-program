"""class Employee:
    def getEmployeeInfo(self):
        self.id=input('Enter ID')
        self.name=inpur('Enter the name')
        self.salary=int(input('Enter the salary'))
    def displayEmployeeInfo(self):
        print('ID=",self.id,"\nName={self.name}\nSalary={self.salary})
    def getsalary(self):
        return self.salary
    class Perks(Employee):
        def calculateSalary(self):
            self.sal=getSalary()
            self.basic=sal*70/100
            self.hra=sal*15/100
            self.da=sal*14/100
            self.total=self.basic+self.hra+self.da
        def displayPerks(self):
            self.displayEmployeeInfo()
            print("Perks=",self.getSalary()+self.total)
        p=Perks()
        p.calculateSalary()
        p.display"""





# 2
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the name:")
    def displayEmployeeInfo(self):
        print("ID=",selfid,"\nName=",self.name)

class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("Enter the salary:"))
    def displayInfo(self):
        self.displayEmployeeInfo()
        print("Salary=",self.sal)























        
