name = input("Enter Customer Name: ")
age = int(input("Enter Age: "))
occupation = input("Enter Occupation Risk (Low/Medium/High): ")
smoker = input("Are you a Smoker? (Yes/No): ")
base_premium = 10000
if age < 18:
    print("Not Eligible for Insurance")
else:
    additional_charges = 0
    if age > 50:
        additional_charges += 5000
    if occupation == "high":
        additional_charges += 7000
    elif occupation == "medium":
        additional_charges += 3000
    if smoker == "yes":
        additional_charges += 5000
    final_premium = base_premium + additional_charges
    print("\n----- Insurance Details -----")
    print("Customer Name      :", name)
    print("Eligibility        : Eligible")
    print("Base Premium       : ", base_premium)
    print("Additional Charges : ", additional_charges)
    print("Final Premium      : ", final_premium)
    if additional_charges >= 10000:
        print("Risk Message       : High Risk Policy")