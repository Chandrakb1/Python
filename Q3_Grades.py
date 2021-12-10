# Get the marks scored by a student in these subjects
totalMarks = 300
maxMarks =100

English=int(input("Enter marks in the English subject: "))
Maths=int(input("Enter marks in the Maths subject: "))
Science=int(input("Enter marks in the Science subject: "))

avg=(English+Maths+Science)*maxMarks//totalMarks
print(avg)

if(avg>=90):
    print("Grade: A")
elif (avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=35 and avg<80):
    print("Grade: Average")
else:
    print("Grade: Fail")
     


