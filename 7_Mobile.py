name = input("Enter the Customer Name : ")
plan = input("Enter Plan Type (Basic/Standard/Premium) : ").lower()
data = int(input("Enter the Extra data used in GB : "))
print("Name of Customer :", name)
print("Plan Type :", plan)
print("Unit of data used :", data)
if data < 0:
    print("Invalid data usage")
else:
    if plan == "basic":
        base_charge = 299
    elif plan == "standard":
        base_charge = 499
    elif plan == "premium":
        base_charge = 799
    else:
        print("Invalid Plan Type")
    extra_charge = data * 20
    if data > 10:
        surcharge = 100
    else:
        surcharge = 0
    final_bill = base_charge + extra_charge + surcharge
    print("Base Plan Charge :", base_charge)
    print("Extra Data Charge :", extra_charge)
    print("Surcharge :", surcharge)
    print("Final Bill :", final_bill)