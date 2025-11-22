# Study Time Tracker
# This program estimates weekly study hours based on daily input.

print("Welcome to my Python program!")

# Ask user for study hours
hours = input("How many hours did you study today? ")

# Convert input and handle errors
try:
    hours = float(hours)  # Convert input to float for calculation
except ValueError:
    print("Please enter a valid number.")
    exit()

# Calculate weekly study hours
weekly_hours = hours * 7

# Display result clearly
print(f"You are on track to study {weekly_hours} hours this week.")
