##Example : Calculate the sum of first N natural numbers using a while and for loop

#While Loop

n=10
sum=0
count=1
while count<=n:
    sum=sum+count
    count=count+1

print("Sum of first 10 natural numbers:",sum)

#For Loop

sum=0

for i in range(11):
    sum=sum+i
print("Sum:", sum)