def calculator(n1,oper,n2):
    if oper == '+':
        result = n1+n2
    elif oper=='-':
        result = n1-n2
    elif oper == '*':
        result = n1*n2
    elif oper=='/':
        if n2!=0:
            result = n1/n2
        else:
            return "Error: Division by zero is not allowed."
    elif oper=='%':
        result = n1%n2
    else:
        return "Error: Invalid operator. Please use +, -, *, /, or %."
    return( result)
f="y"
while(f=="y"):
    n1 = float(input("Enter the first number: "))
    oper = input("Enter an operator (+, -, *, /, %): ")
    n2 = float(input("Enter the second number: "))
    print(calculator(n1,oper,n2))
    print("do you want to perform any other operations y/n")
    f=str(input("enter your choice :"))



"""
Output:-

PS D:\cognifyz\L1> Python L1T4.py
Enter the first number: 5
Enter an operator (+, -, *, /, %): +
Enter the second number: 3
8.0
do you want to perform any other operations y/n
enter your choice :y 
Enter the first number: 3
Enter an operator (+, -, *, /, %): *
Enter the second number: 2
6.0
do you want to perform any other operations y/n
enter your choice :y
Enter the first number: 3
Enter an operator (+, -, *, /, %): -
Enter the second number: 5
-2.0
do you want to perform any other operations y/n
enter your choice :y
Enter the first number: 5
Enter an operator (+, -, *, /, %): /
Enter the second number: 2
2.5
do you want to perform any other operations y/n
enter your choice :


"""