firstNumber=int(input("please,Insert firstNumber"))
secondNumber=int(input("please,Insert secondNumber"))
operation=input("please, insert your the operation")

if operation == "+":
    print("result is",firstNumber+secondNumber)
elif operation=="-":
    print("result is",firstNumber-secondNumber)
elif operation=="*":
    print("result is",firstNumber*secondNumber)
else:
     print("we don't support the operations:+ - *")   

print("thanks for using our software") 

