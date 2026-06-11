def addition():
    a = int(input("Select Your first Number : "))
    b = int(input("Select Your Second Number : "))
    return a + b

def subtraction():
    a = int(input("Select Your first Number : "))
    b = int(input("Select Your Second Number : "))
    return a - b

def multiplication():
    a = int(input("Select Your first Number : "))
    b = int(input("Select Your Second Number : "))
    return a * b

def division():
    a = int(input("Select Your first Number : "))
    b = int(input("Select Your Second Number : "))
    if b == 0:
        return "Error! Division by zero."
    return a / b


    

print("Welcome To My calculator!!! \n");

while True:
    
    print("Please Type The Respective Number To Select any the following Operations")
    a = int(input("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. To finish Simulation \n"))
    
    
    if a == 1:
        x = addition()
        print("Solution :", x, "\n")
    elif a == 2:
        x = subtraction()
        print("Solution :", x, "\n")
    elif a == 3:
        x = multiplication()
        print("Solution :", x, "\n")
    elif a == 4:
        x = division()
        print("Solution :", x, "\n")
    elif a == 5:
        break
    else:
        print("Invalid Input", "\n")