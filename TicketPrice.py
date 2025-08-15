###Determine the ticket price based on age and whether the person is a student.
#Ticket pricing based on age and student status

#Take user input
age=int(input("Enter your age:"))
status=input("You are a student(True/False): ")

if age<5:
    price="Free"
elif age<12:
    price="$10"
elif age<17:
    if status == True:
        price="$12"
    else:
        price="$15"
elif age<=64:
    if status == True:
        price="$18"
    else:
        price="$25"
else:
    price="$20"
print("Price for you :",price)