#program to check whether on is overweight/underweight

weight_kg = float(input("Enter your weight"))
print(weight_kg)
height_m = float(input("Enter your height"))
print(height_m)
bmi= (weight_kg)/(height_m**2)
if bmi < 25:
    print("You are underweight")
else:
    print("you are overweight")
    
#function to check bmi
name = "Phebian"
def bmi(weight_kg,height_m):
    bmi = weight_kg/(height_m**2)
    if bmi > 25:
        return name + " " + "You are overweight"
    else:
        return  name + " " +"You are underweight"

        result = bmi(98.8,1.85)
        print(result)
        
#function to guess a random number between 1 and 10 ,3 times atmost

#Guess a random number assignment
import random
numberofguesses = 0
x = random.randint(1, 10)
if numberofguesses <= 3:
    guess = int(raw_input("Enter an integer from 1 to 10: "))
    while x != "guess":
        print
        if guess < x:
            print "guess is small"
            guess = int(raw_input("Enter an integer from 1 to 10: "))
        elif guess > x:
            print "guess is large"
            guess = int(raw_input("Enter an integer from 1 to 10: "))
        else:
            print "you guessed it!"
else:    
    print("You have blocked your game")
