class employee:
    def __init__(self,name,age,gender,salary) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary 

    def Totalsalary(self,target): 
        Totalsalary= self.salary + target
        print("Totalsalary=",Totalsalary)

    def printall(self):
          print("name=",self.name)
          print("age=",self.age)
          print("gender=",self.gender)
          print("salary=",self.salary)

         
em1 = employee("yousef",25,"email",2500)
em1.printall()
em1.Totalsalary(1000)


em2 = employee("ahmed",30,"email",3500)
em2.printall()
em2.Totalsalary(2000)