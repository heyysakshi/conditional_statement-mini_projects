name=input("Enter the Name of Customer : ")
unit=int(input("Enter the Units Consumed : "))
if unit<=100 :
    bill=unit*3
    print("The  Energy Charge : ",bill)
elif unit>=101 and unit<=200 :
    bill=unit*5
    print("The Energy Charge : ",bill)
else:
    bill=unit*7
    print("The Energy Charge : ",bill)
service=150
print("The Service Charge : ",service)
final=service+bill
if final>5000 :
    print("High Usage Bill...")
else :
    print("The Final Bill : ",final)


