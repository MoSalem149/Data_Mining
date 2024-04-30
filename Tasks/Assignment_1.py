#Assignment (1):

# We want to know your grade ( Pass / Good / Very  Good / Excellent ) from your degree.
# So , you  should receive the following values from the user :  Name , Department , Degree .
# Then show the  following (Demo) : Hello Mohammed , “Your  department is IS and your degree is <<GRADE>>! ” .

def calculate_grade(degree):
    if degree >= 85:
        return "Excellent"
    elif degree >= 75:
        return "Very Good"
    elif degree >= 65:
        return "Good"
    else:
        return "Pass"
    
def main():
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    degree = int(input("Enter your degree: "))

    grade = calculate_grade(degree)

    print(f"Hello {name}, your department is {department} and your degree is {grade}!")

if __name__ == "__main__":
    main()