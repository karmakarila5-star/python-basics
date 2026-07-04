medical_cause = input("did you have a medical cause ?(y/n):").strip().upper()
if medical_cause == 'Y':
    print("you are allowed")
else:
    atten = int(input("enter the attendance of the student: "))
    if atten >= 75:
        print("allowed")
    else:
        print("not allowed")