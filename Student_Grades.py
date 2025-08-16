#Organizing student grades
#create a list to store and calculate average grades for student

grades=[89,67,99,75,86,79,71,95]

grades.append(93)

average_grade=sum(grades)/len(grades)
print(f"Average of student grades:{average_grade:2f}")

high_grade=max(grades)
low_grade=min(grades)
print("Highest grade:",high_grade)
print("Lowest garde:",low_grade)