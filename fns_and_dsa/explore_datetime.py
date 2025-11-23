from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date in a variable
    current_date = datetime.now()
    
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_datetime}")
    return current_date


def calculate_future_date(days_to_add):
    # Get today's date
    current_date = datetime.now()
    
    # Save the future date in a variable
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {formatted_future_date}")
    return future_date


# ---- Main Program ----
if __name__ == "__main__":
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Ask the user for number of days to add
    try:
        user_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(user_input)
    except ValueError:
        print("Invalid input! Please enter an integer.")
