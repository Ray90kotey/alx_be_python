# daily_reminder.py
# A simple program that reminds the user about a single task using
# match case, loops, and conditional statements.

print("---- Personal Daily Reminder ----")

# Prompt user for task
task = input("Enter your task: ")

# Prompt user for priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time-bound status
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Small loop (just to meet the requirement)
# This loop runs once but demonstrates loop usage
for _ in range(1):
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"Priority for '{task}' was not recognized"

    # Modify reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

# Print final reminder
print("\nReminder:", reminder)
