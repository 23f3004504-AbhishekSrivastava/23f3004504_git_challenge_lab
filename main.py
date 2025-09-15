import pandas as pd

def add(a,b):
    return a+b
def pro(a,b):
    return a*b
def sub(a,b):
    return a-b
def div(a,b):
    if b==0:
        return print("Exception devide by 0")
    else:
        return a/b

a=int(input("Enter the number >>  "))
op=input("Enter the operator  +, -, /, *  >> ")
b =int(input("Enter the 2nd number  >>  "))

if op == "+":
    print("The sum of given numbers is ", add(a,b))
elif op == "-":
    print("The difference of given numbers is ", sub(a,b))
elif op == "*":
    print("The product of given numbers is ", pro(a,b))
elif op == "/":
    print("The division of given numbers is ", div(a,b))
else:
    print("Invalid Operator")
