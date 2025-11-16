# daily_reminder.py
# A program that gives a personalized daily reminder for one task.

print("---- Personal Daily Reminder ----")

# Prompt for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop requirement
for _ in range(1):

    # Match Case for priority levels
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            base_message = f"The priority level for '{task}' is unknown"

    # Time sensitivity check
    if time_bound == "yes":
        final_message = base_message + " that requires immediate attention today!"
    else:
        final_message = base_message + ". Consider completing it when you have free time."

# ✔ REQUIRED FORMAT: Must begin with "Reminder:"
print(f"Reminder: {final_message}")
