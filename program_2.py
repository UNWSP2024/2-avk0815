
def average_age():
    # Get User Input
    age1 = float(input("Enter the age of person 1: "))
    age2 = float(input("Enter the age of person 2: "))
    age3 = float(input("Enter the age of person 3: "))
    age4 = float(input("Enter the age of person 4: "))
    age5 = float(input("Enter the age of person 5: "))

    # Sum ages
    total_age = age1 + age2 + age3 + age4 + age5

# Average the ages
    average = total_age / 5

    # Print the results
    print(f"The average age is: {average}")
# Line which calls the above function.
average_age()