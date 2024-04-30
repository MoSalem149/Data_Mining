# Assignment (2):

# BMI (Body Mass Index) is a measurement of body fat based on height and weight that applies to both men and women between the ages of 18 and 65 years. 
# BMI can be used to  indicate if you are overweight, obese, underweight or normal.
# You should receive the following fields : Name , Weight (KG),  Height (CM).
# Use the following formula to calculate BMI :
# BMI = (Weight in Kilograms / (Height in Meters x Height in  Meters))
# Notes :
# bmi <= 18.5 then UNDERWEIGHT
# bmi > 18.5 AND bmi<=24.9 then NORMAL WEIGHT
# bmi > 24.9 AND num<=29.9 then OVERWEIGHT
# bmi > 30.0 then OBESE
# Demo for the final result: "Your BMI value is <<BMI_VALUE>> and you are : <<STATUS>>.

def calculate_bmi(weight, height):
    height_meters = height / 100
    bmi = weight / (height_meters * height_meters)
    return bmi

def determine_status(bmi):
    if bmi <= 18.5:
        return "UNDERWEIGHT"
    elif bmi > 18.5 and bmi <= 24.9:
        return "NORMAL WEIGHT"
    elif bmi > 24.9 and bmi <= 29.9:
        return "OVERWEIGHT"
    else:
        return "OBESE"
    
def main():
    name = input("Enter your name: ")
    weight = float(input("Enter your weight in KG: "))
    height = float(input("Enter your height in CM: "))

    bmi = calculate_bmi(weight, height)
    status = determine_status(bmi)

    print(f"Hello {name}, your BMI value is {bmi:.2f} and you are: {status}.")

if __name__ == "__main__":
    main()