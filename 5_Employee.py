name=input("Enter the Name of employee : ")
salary=int(input("Enterv the Salary Of Employee : "))
yoe=int(input("Enter the Year of Experience : "))
rating=int(input("Enter the Performance rating from 1 to 5 : "))
if rating >5 :
    print("Regect : Invalid Rating")
else :
    print("The Name of Employee : ",name)
    if yoe >= 10 and rating>=4 :
        print("Congratulations!!!You got 20 % Bonus")
        B_amt=salary*20/100
        G_salary=salary+B_amt
        print("Bonus Amount : ",B_amt)
        print("Final Salary : ",G_salary)
    elif yoe>=5  and rating>=4 :
        print("Congratulations!!!You got 15 % Bonus")
        B_amt=salary*15/100
        G_salary=salary+B_amt
        print("Bonus Amount : ",B_amt)    
        print("Final Salary : ",G_salary)
    elif  yoe>=2  and rating>=3 :
        print("Congratulations!!!You got 10 % Bonus")
        B_amt=salary*10/100
        G_salary=salary+B_amt
        print("Bonus Amount : ",B_amt)    
        print("Final Salary : ",G_salary)
    else :
         print("No Bonus!!")
if rating==5 :
    print("Excellent Performer")




























