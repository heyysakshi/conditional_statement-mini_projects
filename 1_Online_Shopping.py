name = input("Enter the Name of Customer : ")
amount = int(input("Enter the Purchase Amount : "))
c_type = input("Enter the Customer Type (Regular or Premium) : ")
if amount >= 5000:
    print("Congratulations!!! You got 20% Discount...")
    d_amount = amount * 20 / 100
elif amount >= 3000 and amount<=5000:
    print("Congratulations!!! You got 10% Discount...")
    d_amount = amount * 10 / 100
elif amount >= 1000:
    print("Congratulations!!! You got 5% Discount...")
    d_amount = amount * 5 / 100
else:
    print("No Discount...")
    d_amount = 0
final = amount - d_amount
print("Discount Amount :", d_amount)
if final >= 2000:
    print("Delivery is Free...")
    total = final
else:
    print("Delivery Charge = 100")
    total = final + 100
if c_type == "premium":
    premium_discount = total * 5 / 100
    total = total - premium_discount
    print("Premium Discount :", premium_discount)
print("Final Payable Amount :", total)