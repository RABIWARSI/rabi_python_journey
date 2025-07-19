sub1 = float(input("Enter subject 1 marks: "))
sub2 = float(input("Enter subject 2 marks: "))
sub3 = float(input("Enter subject 3 marks: "))
sub4 = float(input("Enter subject 4 marks: "))
sub5 = float(input("Enter subject 5 marks: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

print("Total marks:", total)
print("Percentage:", percentage)

if percentage >= 80:
    print("Grade: A+")
elif percentage >= 70:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
else:
    print("Fail")
