age = int(input("Enter your age "))
 
if age >= 0 and age >= 18:
    print("N/A")
if age >=16:
    print("You are 16 and over")
    if age <= 18:
        print("You are 18 and over")
else:
    print("Invalid age was entered.")