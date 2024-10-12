'''
TPRG 2131 Fall 2024 Assignment 1, Test file template.
Oct, 2024
Hemil Prajapati (100942152).
This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving.
credit to the original author(s).

Use this template as the start

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''

import math # Importing the math module for mathematical functions

# Function to get a positive value
def get_positive_value(message):
    while True: # Loop to keep asking for input until a valid value is entered
        try:
            value = float(input(message))
            while value <= 0.0:
                value = float(input("The value must be greater than zero\n"
                            + message))
            return value
        except ValueError: # If input is not a number, prompt the user to enter a valid number
            print("Oops!  That was no valid number.  Try again...")

# Function to calculate the area of a square
def area_square (length):
    area_sq1 = length ** 2 
    area_sq = round(area_sq1, 1) # Round the result to 1 decimal place
    return area_sq

# Function to calculate the volume of a rectangle
def volume_rectangle (length, height, width):
    vol_rec1 = length * height * width
    vol_rec = round(vol_rec1, 1) # Round the result to 1 decimal place
    return vol_rec

# Function to calculate the area of a circle
def area_circle (radius):
    area_cir1 = math.pi * radius ** 2
    area_cir = round(area_cir1, 1) # Round the result to 1 decimal place
    return area_cir

# Function to calculate the volume of a cone
def volume_cone (height, radius):
    vol_cone1 = 0.33 * math.pi * height * radius **2
    vol_cone = round(vol_cone1, 1) # Round the result to 1 decimal place
    return vol_cone
  
# Function to calculate the area of a triangle  
def area_triangle (base, height):
    area_tri1 = 0.5 * base * height
    area_tri = round(area_tri1, 1) # Round the result to 1 decimal place
    return area_tri

# Function to get a decision input from the user (Quit, View, or Default view)
def get_decision(message):
    decision = str(input(message))
    while decision != 'Q' and decision != 'q' and decision != 'V' and decision != 'v' and decision != 'D' and decision != 'd':
        decision = str(input("\nInvalid choice. Please choose Valid letter"))
    return decision

# Function to get the user's choice of calculation
def get_choice(message):
    choice = str(input(message))
    while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6':
        choice = str(input("\nInvalid choice. Please choose between 1 and 6."))
    return choice

# Main function to control the flow of the program
def main():
    while True:
        # Get the decision from the user (Quit, View formula, or Default view)
        decision = get_decision ("Enter (Q/q) to Quit, (V/v) to change the calculated view or (D/d) for default view:-")
        if decision == "Q" or decision == "q": # If the user chooses to quit, exit the program
            print ("You choose to quit...")
            break
        
         # loop to display the choices for area/volume calculations    
        while True:
            choice = get_choice("\n1:- Area of Square \n2:- Volume of Rectangle \n3:- Area of Circle \n4:- Volume of Cone \n5:- Area of Triangle \n6:- Main Menu")
            
            if choice == "1": # Area of Square
                length = get_positive_value("What is the value of length in meter?  ")
                result = area_square (length) # Calculate area
                formula = f"({length} ** 2)"
                if decision == "V" or decision == "v": # Show result with formula
                    print("\nThe Area of Square is:", result , "\u33A1 ", "\nThe formula is:" , formula )
                elif decision == "D" or decision == "d": # Show only result in default view
                    print("\nThe Area of Square is:", result , "\u33A1 ")
                
            elif choice == "2": # Volume of Rectangle
                length = get_positive_value("What is the value of length in meter?  ")
                height = get_positive_value("What is the value of height in meter?  ")
                width = get_positive_value("What is the value of width in meter?  ")
                result = volume_rectangle (length, height, width) # Calculate volume
                formula = f"({length} * {height} * {width})"
                if decision == "V" or decision == "v": # Show result with formula
                    print("\nThe Volume of Rectangle is:", result , "\u33A5 ", "\nThe formula is:" , formula)
                elif decision == "D" or decision == "d": # Show only result in default view
                    print("\nThe Volume of Rectangle is:", result)
            
            elif choice == "3": # Area of Circle
                radius = get_positive_value("What is the value of radius in meter?  ")
                result = area_circle (radius) # Calculate area
                formula = f"({math.pi} * {radius} ** 2)"
                if decision == "V" or decision == "v": # Show result with formula
                    print("\nThe Area of Circle is:", result, "\u33A1 ", "\nThe formula is:" , formula)
                elif decision == "D" or decision == "d": # Show only result in default view
                    print("\nThe Area of Circle is:", result, "\u33A1 ")
                
            elif choice == "4": # Volume of Cone
                height = get_positive_value("What is the value of height in meter?  ")
                radius = get_positive_value("What is the value of radius in meter?  ")
                result = volume_cone (height, radius) # Calculate volume
                formula = f"(0.33 * {math.pi} * {height} * {radius} **2)"
                if decision == "V" or decision == "v": # Show result with formula
                    print("\nThe Volume of Cone is:", result , "\u33A5 ", "\nThe formula is:" , formula)
                elif decision == "D" or decision == "d": # Show only result in default view
                    print("\nThe Volume of Cone is:", result , "\u33A5 ")
                
            elif choice == "5": # Area of Triangle
                base = get_positive_value("What is the value of base in meter?  ")
                height = get_positive_value("What is the value of height in meter?  ")
                result = area_triangle (base, height) # Calculate area
                formula = f"(0.5 * {base} * {height})"
                if decision == "V" or decision == "v": # Show result with formula
                    print("\nThe Area of Triangle is:", result, "\u33A1 ", "\nThe formula is:" , formula)
                elif decision == "D" or decision == "d": # Show only result in default view
                    print("\nThe Area of Triangle is:", result, "\u33A1 ")
                    
            elif choice == "6": # Return to the main menu
                print("Return to the Main Menu")
                break

# Entry point of the program
if __name__ == "__main__":
    main()
