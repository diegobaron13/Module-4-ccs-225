# 10/20/2026
#Samat Toktonazaron
#Abdyrakhman Raiapov
#Ainazik Abdunabieva
#Diego Baron


name = input("Enter your name: ")
print(f"Hello, {name}!, welcome to the trucking program.")

userChoice = input("Choose an option (0-6): ")

if userChoice == "1":
    print("You chose " + userChoice + ": Your load is on time and will be delivered tomorrow.")
elif userChoice == "2":
    print("You chose " + userChoice + ": The nearest truck stop is 12 miles ahead.")
elif userChoice == "3":
    print("You chose " + userChoice + ": Your driving hours have been logged.")
elif userChoice == "4":
    print("You chose " + userChoice + ": Roadside help is on the way.")
elif userChoice == "5":
    print("You chose " + userChoice + ": Clear skies on your route today.")
elif userChoice == "6":
    print("You chose " + userChoice + ": Connecting you to the dispatcher...")
elif userChoice == "0":
    print("You chose " + userChoice + ": Goodbye, drive safe!")
else:
    print("'" + userChoice + "' is not a valid option. Please try again.")