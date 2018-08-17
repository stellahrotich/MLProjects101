#program to give grades when a student enters  mark scored

marks = float(input("Please enter your marks I give you your grade:"))
if marks < 0 or marks > 100:
    print ("Out of Range")
else:
    if marks >= 70:
        print ("A")
    elif marks >= 60:
        print ("B")
    elif marks >= 50:
        print ("C")
    elif marks >= 40:
        print ("D")
    else:
        print ("FAIL")
