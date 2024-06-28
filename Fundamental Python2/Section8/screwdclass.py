class Screwdrive:
    def __init__(self,color,len,type,doseRotate,doesTest):
        self.color= color
        self.len= len
        self.type= type
        self.doseRotate= doseRotate
        self.doesTest= doesTest
    def Rotates(self):
        result= f"I am a {self.len} cm {self.color} {self.type} Screwdrive"
        if(self.doseRotate):
            print(result +"and I rotate")
        else:
              print(result +"and I don't rotate")
    def testelectrisety(self):
        result= f"I am a {self.len} cm {self.color} {self.type} Screwdrive"
        if(self.doesTest):
            print(result +"and I test")
        else:
              print(result +"and I don't test")
                
           