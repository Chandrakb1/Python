
#Validate the given number is fibonacci sequence

fibNumber = int(input("Enter the number: "))

a = 1
b = 1
count = 0

if(fibNumber == 0 or fibNumber == 1):
    print("The given number is fibonacci number")

else:
        while count < fibNumber:
            count = a+b
            a = b
            b = count            

if count == fibNumber:
    print("The given number is fibonacci")
else:
    print("The given number is not a fibonacci")


                
            

        
            

