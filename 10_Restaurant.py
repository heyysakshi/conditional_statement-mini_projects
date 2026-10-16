name=input("Enter customer name: ")
bill=float(input("Enter food bill amount: "))
member=input("Membership (Yes/No): ")
if bill<1000:
    discount=0
elif bill<=2999:
    discount=bill*0.05
elif bill<=4999:
    discount=bill*0.10
else:
    discount=bill*0.15
if member=="Yes":
    discount=discount+(bill*0.05)
amount=bill-discount
service=amount*0.05
final=amount+service
print("Customer Name:",name)
print("Original Bill:",bill)
print("Discount:",discount)
print("Service Charge:",service)
print("Final Payable Amount:",final)
if final>=5000:
    print("Thank you for being a valued customer")
else:
    print("Thank you")