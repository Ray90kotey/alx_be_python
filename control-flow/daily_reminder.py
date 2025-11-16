# daily_reminder.py
# A program that gives a personalized daily reminder for one task.

print("---- Personal Daily Reminder ----")

# Prompt for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop requirement (purpose: allow processing inside loop)
for _ in range(1):

    # Match Case for priority levels
    match priority:
        case "high":
            base_message = f"'{task}' is a HIGH priority task"
        case "medium":
            base_message = f"'{task}' is a MEDIUM priority task"
        case "low":
            base_message = f"'{task}' is a LOW priority task"
        case _:
            base_message = f"The priority level for '{task}' is UNKNOWN"

    # Time sensitivity check
    if time_bound == "yes":
        final_message = base_message + " that requires immediate attention today!"
    else:
        final_message = base_message + ". Complete it when you have free time."

# Final customized reminder
print("\nCustomized Reminder:")
print(final_message)
