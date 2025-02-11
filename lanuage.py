def user_choice(choice, num1, num2):    
    if choice == 1 : 
	    print(f"Your Choice is Addition = {num1+num2} = ")
    elif choice == 2: 
	    print(f"Your Choice is subtrction = {num1-num2}")	

    elif choice == 3: # type: ignore
	    print(f"Your Choice is multiplication = {num1*num2}")	

    elif choice == 4: # type: ignore
	    print(f"Your Choice is division = {num1/num2}")	
    else:
        print("Wrong Choice")
	
num1= int(input("enter the first number = "))
num2= int(input("Enter the Second Number= "))
num3= (num1,num2)
print(num3)
choice= int(input("Enter the choice of the user = "))
user_choice(choice, num1, num2)