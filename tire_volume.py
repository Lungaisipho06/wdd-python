# tire_volume.py
# Enhancement: The program asks the user if they want to buy tires.
# If the answer is 'yes', it prompts for and stores their phone number
# in the volumes.txt file along with the tire data.

import math
from datetime import datetime

def main():
    # --- 1. Get Input from User and Convert to Numbers ---

    print("Welcome to the Tire Volume Calculator!")
    
    # Get the width of the tire in millimeters (w)
    w_str = input("Enter the width of the tire in mm (ex 205): ")
    w = float(w_str)

    # Get the aspect ratio of the tire (a)
    a_str = input("Enter the aspect ratio of the tire (ex 60): ")
    a = float(a_str)

    # Get the diameter of the wheel in inches (d)
    d_str = input("Enter the diameter of the wheel in inches (ex 15): ")
    d = float(d_str)

    # --- 2. Calculate the Tire Volume ---
    
    # Formula: V = [π * w^2 * a * (w * a + 2,540 * d)] / 10,000,000,000
    
    # Calculate the volume
    v = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000

    # Round the volume to two decimal places
    v_rounded = round(v, 2)

    # --- 3. Display Results ---
    
    print(f"The approximate volume is {v_rounded} liters")

    # --- 4. Get Current Date and Enhancement Feature ---
    
    # Get the current date (without time)
    current_date_and_time = datetime.now()
    current_date = f"{current_date_and_time:%Y-%m-%d}"

    # Enhancement: Ask about purchase and get phone number
    phone_number = ""
    buy_tires = input("Would you like to buy tires with these dimensions? (yes/no): ").lower()
    
    if buy_tires == "yes":
        phone_number = input("Please enter your phone number so we can contact you: ")
    
    # --- 5. Append Data to volumes.txt ---
    
    # Open the file in append mode ("at")
    with open("volumes.txt", "at") as volumes_file:
        # Prepare the core data string (date, w, a, d, v)
        output_line = f"{current_date}, {w}, {a}, {d}, {v_rounded}"
        
        # Add the phone number if it was entered
        if phone_number:
            output_line += f", {phone_number}"
        
        # Write the line to the file
        print(output_line, file=volumes_file)

# Execute the main function
if __name__ == "__main__":
    main()
    

