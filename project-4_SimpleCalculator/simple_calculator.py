def addition(first_number,second_number):
    return first_number+second_number

def subtraction(first_number,second_number):
    return first_number-second_number
   
def multiplication(first_number,second_number):
    return first_number*second_number
  
def division(first_number,second_number):
    return first_number/second_number
   
def modulus(first_number,second_number):
    return first_number%second_number
   

print("===== SIMPLE CALCULATOR =====")

print("1. Addition.")
print("2. Subtraction.")
print("3. Multiplication.")
print("4. Division.")
print("5. Modulus.")
print("6. Exit.")

while True:
    choice=int(input("Enter your choice: "))

    if(choice==6):
        break
    elif(choice<=0 or choice>=7):
        print("Invalid choice. Select again.")
        continue
    else:
        first_number=float(input("Enter first number: "))
        second_number=float(input("Enter second number: "))

        match choice:
            case 1:
                result=addition(first_number,second_number)
                print("Result: ",result)
            case 2:
                result=subtraction(first_number,second_number)
                print("Result: ",result)
            case 3:
                result=multiplication(first_number,second_number)
                print("Result: ",result)
            case 4:
                if second_number==0:
                    while(second_number==0):
                        print("Division by Zero is Invalid.")
                        second_number=float(input("Enter second number: "))
                result=division(first_number,second_number)
                print("Result: ",result)
            case 5:
                if second_number==0:
                   while(second_number==0):
                        print("Modulus by Zero is Invalid.")
                        second_number=float(input("Enter second number: "))
                result=modulus(first_number,second_number)
                print("Result: ",result)