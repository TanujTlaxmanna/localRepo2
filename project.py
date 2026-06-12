def addition():
    a = int(input("Enter Your first Number : "))
    b = int(input("Enter Your Second Number : "))
    return a + b

def subtraction():
    a = int(input("Enter Your first Number : "))
    b = int(input("Enter Your Second Number : "))
    return a - b

def multiplication():
    a = int(input("Enter Your first Number : "))
    b = int(input("Enter Your Second Number : "))
    return a * b

def division():
    a = int(input("Enter Your first Number : "))
    b = int(input("Enter Your Second Number : "))
    if b == 0:
        return "Error! Division by zero."
    return a / b

def square():
    a = int(input("Enter your Digit : "))
    return a*a 

def squareRoot():
    a = int(input("Enter your Digit : "))
    return a**(1/2)

def exponential():
    a = int(input("Enter your Digit : "))
    b = int(input("Enter your exponential Power :"))
    return a ** b

def exponentialRoot():
    a = int(input("Enter your Digit : "))
    b = int(input("Enter your exponential Root :"))
    return a ** (1/b)


    

print("\n\t\t\t\t\tWelcome To My calculator!!! \n");

while True:
    
    print("\t\tPlease Type The Respective Number To Enter any the following Operations\n\n")
    a = int(input("1. Addition \t\t\t\t\t\t\t2. Subtraction \n3. Multiplication \t\t\t\t\t\t4. Division \n5. Square Of your Number \t\t\t\t\t6. Square Root of your Number \n7. Exponential Power of your Number \t\t\t\t8. Exponential Root of your Number \n\n9. To finish Simulation \n"))
    
    
    if a == 1:
        x = addition()
        print("-------------------\n|Solution :", x, "    | \n-------------------")
    elif a == 2:
        x = subtraction()
        print("-------------------\n|Solution :", x, "    | \n-------------------")
    elif a == 3:
        x = multiplication()
        print("-------------------\n|Solution :", x, "    | \n-------------------")
    elif a == 4:
        x = division()
        print("-------------------\n|Solution :", x, "    | \n-------------------")
    elif a == 5:
        x = square()
        print("-------------------\n|Solution :", x, "    | \n-------------------")
    elif a == 6:
        x = squareRoot()
        print(f"---------------------\n|Solution : {x:.2f}    | \n---------------------")
    elif a == 7:
        x = exponential()
        print(f"---------------------\n|Solution : {x:.2f}    | \n---------------------")
    elif a == 8:
        x = exponentialRoot()
        print(f"---------------------\n|Solution : {x:.2f}    | \n---------------------")
    elif a == 9:
        break
    else:
        print("Invalid Input", "\n")