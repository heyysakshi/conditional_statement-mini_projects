name = input("Enter Customer Name: ")
age = int(input("Enter Age: "))
show_type = input("Enter Show Type (Morning/Evening): ")
day_type = input("Enter Day Type (Weekday/Weekend): ")
base_price = 200
if age < 0:
    print("Invalid Age! Age cannot be negative.")
else:
    discount = 0
    surcharge = 0
    if age < 12:
        discount = base_price * 50 / 100
    elif age >= 60:
        discount = base_price * 30 / 100
    if show_type == "morning":
        discount += 30
    if day_type == "weekend":
        surcharge = 50
    final_price = base_price - discount + surcharge
    print("\n----- Ticket Details -----")
    print("Customer Name      :", name)
    print("Original Ticket Price : ", base_price)
    print("Discount           : ", discount)
    print("Weekend Surcharge  : ", surcharge)
    print("Final Ticket Price : ", final_price)