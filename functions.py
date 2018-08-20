#program to check whether on is overweight

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
