def add_time(start, duration, day=None):
    # ----- Parse the start time -----
    # Split into the time part and the period (AM/PM)
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))
    
    # Convert start time to 24-hour format
    if period.upper() == "PM" and start_hour != 12:
        start_hour += 12
    if period.upper() == "AM" and start_hour == 12:
        start_hour = 0

    # Calculate the total minutes for the start time
    start_total_minutes = start_hour * 60 + start_minute

    # ----- Parse the duration -----
    dur_hour, dur_minute = map(int, duration.split(':'))
    duration_total_minutes = dur_hour * 60 + dur_minute

    # ----- Add the duration to the start time -----
    total_minutes = start_total_minutes + duration_total_minutes

    # Determine how many days later it is and get remaining minutes of the final day
    minutes_in_day = 24 * 60
    days_later = total_minutes // minutes_in_day
    remaining_minutes = total_minutes % minutes_in_day

    # ----- Convert the final time back to hours and minutes -----
    new_hour_24 = remaining_minutes // 60
    new_minute = remaining_minutes % 60

    # Determine the new period (AM or PM) and convert back to 12-hour format
    if new_hour_24 >= 12:
        new_period = "PM"
    else:
        new_period = "AM"
    new_hour = new_hour_24 % 12
    if new_hour == 0:
        new_hour = 12

    # Build the new time string
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"

    # ----- Calculate the day of the week, if provided -----
    if day:
        # List of days for reference
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        # Normalize the input day and find its index
        day_index = days_of_week.index(day.capitalize())
        # Compute the new day index by adding the days later (using modulo to wrap around)
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        # Append the new day to the result
        new_time += f", {new_day}"

    # ----- Add information about the number of days later, if any -----
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
