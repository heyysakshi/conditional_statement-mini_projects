name=input("Enter the Name of Student : ")
per=float(input("Enter the Percentage of Student : "))
income=int(input("Enter the Annual Family Income : "))
attendance=int(input("Enter the Attendance Percentage : "))
print("the Name of Student : ",name)
if per<=75 :
    print("Not Eligible for Scholorship!!!")
    print("Reason : Percentage Must be at least 75 %")
elif income>400000 :
     print("Not Eligible for Scholorship!!!")
     print("Reason : Annual Family Income Must be at least 4,00,000 or less...")
elif per>=90 and per>=75 and income<=400000 :
     print("Eligibility Status : Eligible for Scholorship ")
     print("Scholorship Category :  Full Scholorship ")
else :
     print("Eligibility Status : Eligible for Scholorship ")
     print("Scholorship Category :  Partial Scholorship...")

