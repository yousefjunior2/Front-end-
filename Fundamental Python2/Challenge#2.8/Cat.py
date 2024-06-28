class Cat:
    def __init__(self,Name,Type,color,age,doesWalk,doesRun) :
        self.Name = Name
        self.Type = Type
        self.color = color
        self.age = age
        self.doesWalk = doesWalk
        self.doesRun = doesRun
    def Walking(self):
        result= f"My Name {self.Name} ,I am {  self.age } month old, type is {self.Type},my color is {self.color}"   
        print(result + " and I am walk",self.doesWalk )
      
    def Running(self):
        result= f"My Name {self.Name} ,I am {  self.age } month old, type is {self.Type},my color is {self.color}"   
        print(result + " and I am Run", self.doesRun)
        