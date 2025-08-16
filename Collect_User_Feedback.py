##Collecting User Feedback
#Use a list to collect and analyze user feedback

feedback=["Great service","very satisfied","Could be better","Excellent exprience"]

#Adding new feedback
feedback.append("Not happy with the service")

#Counting specific feedback
positive_feedback_count=sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())
print("User Feedback:")
for comment in feedback:
    print(f"-{comment}")