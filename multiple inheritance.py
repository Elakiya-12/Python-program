class Employee:
    def __init__(self,name,Id,position):
        self.name=name
        self.Id=Id
        self.position=position
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nId:{self.Id}\nPosition:{self.position}")
class Address:
    def __init__(self,street,state,country):#during object creation we are passing the value
        self.street=street
        self.state=state
        self.country=country
    def displayAddressInfo(self):
        print(f"Street Name: {self.street}\nState Name:{self.state}\nCountry name: {self.country}")

class EmployeeDetails(Employee,Address):
    def __init__(self,name,Id,position,street,state,country):
        super().__init__(name,Id,position)#access the variables for the immediate parent or initialize the variable
        Address.__init__(self,street,state,country)
    def displayEmp(self):#calling two methods employee and address
        self.displayEmployeeInfo()
        self.displayAddressInfo()

ed=EmployeeDetails("Jiya",100,"Manager","Shenoy Nagar","Tamilnadu","India")
ed.displayEmp()
        
