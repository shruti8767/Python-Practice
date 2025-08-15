# Create a Calculator using elif statement

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operation=(input("Which operation you want to perform, please type (+,-,*,/,%,**):"))

if operation == '+':
    result=num1+num2
elif operation == '-':
    result=num1-num2
elif operation == '*':
    result=num1*num2
elif operation == '/':
    if num2!=0:
        result=num1/num2
    else:
        result="Error! Division by zero."
elif operation == '%':
    result=num1%num2
elif operation == '**':
    result=num1**num2
else:
    result="Invalid input"
print("Result:",result)
