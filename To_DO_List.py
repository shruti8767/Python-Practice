to_do_list=["Clean the room","Do coding","Workout","Pay bill"]

#I want to add more task 
to_do_list.append("Buy groceries")
to_do_list.append("Schedul meeting")

#I completed workout 
to_do_list.remove("Workout")

#Set remainder to Pay bill
if "Pay bill" in to_do_list:
    print("Don't forget to pay bill!")
    
print("##To do remaining List##")
for task in to_do_list:
    print(task)
