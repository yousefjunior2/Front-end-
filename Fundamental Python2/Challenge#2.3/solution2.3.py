from yousef import joo
import math
import random2


num1=int(input("please,Insert firstNumber"))
num2=int( input("please,Insert secondNumber"))
operation=input("please, insert your the operation")

# result=0
if operation == "+":
     result=   joo.Sum(num1,num2)
elif operation=="-":
    result=   joo.Subtract(num1,num2)
elif operation=="/":
     result=   joo.Division(num1,num2)
elif operation == "*":
     result=   joo.Multiply(num1,num2)
elif operation == "pow":
     result=  math.pow(num1,num2)
elif operation == "sqrt":
     result=   math.sqrt(num1,num2)
elif operation == "random":
     result= random2.randint(num1,num2) 
print("answer:",result)       
print("thanks for using our software") 


