# Create a Calculator using elif statement

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operation=(input("Which operation you want to perform, please type (+,-,*,/,%,**):"))

if operation == '+':
    result=num1+num2
    print(result)
elif operation == '-':
    result=num1-num2
    print(result)
elif operation == '*':
    result=num1*num2
    print(result)
elif operation == '/':
    result=num1/num2
    print(result)
elif operation == '%':
    result=num1%num2
    print(result)
elif operation == '**':
    result=num1**num2
    print(result)
else:
    print("Invalid input.")