# Program to calculate Total, Percentage and Grade

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
total = sub1 + sub2 + sub3 + sub4
percentage = total / 4

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\n----- Result -----")
print("Mark of sub1:",sub1)
print("Mark of sub2:",sub2)
print("Mark of sub3:",sub3)
print("Mark of sub4:",sub4)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
