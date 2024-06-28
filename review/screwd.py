class screwdriver:
    def __init__(self,color,len,type,doesRotate,doesTest):
        self.color = color
        self.len = len
        self.type = type
        self.doesRotate = doesRotate
        self.doesTest = doesTest
    def rotate(self,):
        result = f"My length is {self.len} cm the color is {self.color} type is {self.type} screwdrive"    
        if (self.doesRotate):
            print(result + "and I rotat")
        else:
            print(result + "and I does not rotat")
    def test(self,):
        result = f"My length is {self.len} cm the color is {self.color} type is {self.type} screwdrive"    
        if (self.doesTest):
            print(result + "and I Test")
        else:
            print(result + "and I does not Test")
