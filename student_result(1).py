Name = input("Enter your name:")
Roll_no = int(input("Enter your Roll_no:"))

English =int(input("Enter your English marks:"))
Physics = int(input("Enter your Physics marks:"))
Maths = int(input("Enter your Maths marks:"))
Chemistry= int(input("Enter your Chemistry marks:"))
Computer =int(input("Enter your Computer marks:"))

Total_marks = English + Physics + Maths + Chemistry + Computer

Percentage = ( Total_marks / 500 ) * 100
print("Total Marks =", Total_marks)
print("Percentage =", Percentage)

if  Percentage >= 80:
    print("Grade = A")
elif Percentage >= 70:
        print("Grade = B")
elif Percentage >= 60:
            print("Grade = C")
elif Percentage >= 50:
                print("Grade = D")
else :
                    print("FAIL")
                    