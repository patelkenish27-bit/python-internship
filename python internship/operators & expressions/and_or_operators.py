percentage=float(input("enter the student percentage :"))
if percentage>0 or percentage<100:
   
    if percentage>=80 and percentage<100:
        print("distinction")
    elif percentage>=70 and percentage<80:
        print("first class")
    elif percentage>=60 and percentage<70:
        print("second class")
    elif percentage>=35 and percentage<60:
        print("pass")
    else:
        print("fail")
else:
    print("invalid percentage")