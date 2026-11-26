
percentage = float(input("Enter the student percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid Percentage")

elif percentage >= 0 and percentage <= 100:

    if percentage >= 80:
        print("Distinction")
    elif percentage >= 70:
        print("First Class")
    elif percentage >= 60:
        print("Second Class")
    elif percentage >= 35:
        print("Pass")
    else:
        print("Fail")
