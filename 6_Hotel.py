name = input("Enter the Name of Guest : ")
room = input("Enter Room Type (Standard/Deluxe/Suite) : ").lower()
night = int(input("Enter the Number of Nights Stays : "))
print("\nGuest Details")
print("Name of Guest :", name)
print("Room Type :", room)
print("Number of Nights :", night)
if night > 0:
    if room == "standard":
        rate = 2000
    elif room == "deluxe":
        rate = 3500
    elif room == "suite":
        rate = 6000
    else:
        print("Error: Invalid Room Type!")
        rate = 0
    if rate > 0:
        room_charge = rate * night
        if night >= 10:
            discount = room_charge * 20 / 100
            print("Congratulations!! You got 20% discount...")
        elif night >= 5:
            discount = room_charge * 10 / 100
            print("Congratulations!! You got 10% discount...")
        else:
            discount = 0
            print("No discount available.")
        final_amount = room_charge - discount
        print("\nBooking Summary")
        print("Room Charge :", room_charge)
        print("Discount :", discount)
        print("Final Booking Amount :", final_amount)
else:
    print("Error: Number of nights must be greater than 0.")
