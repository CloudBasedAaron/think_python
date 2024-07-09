# "Think Python" Exercise 1

def race_stats():
    # Take inputs from user for distance and finishing time
    distance_in_km = int(input("How many kilometers in your race in whole digits:\n"))
    user_time_in_min = int(input("Enter the number of minutes in your time in whole digits:\n"))
    user_time_in_sec = int(input("Now enter the number of seconds in your time in whole digits:\n"))

    # Convert race time to total seconds
    total_time_in_sec = (user_time_in_min * 60) + user_time_in_sec

    # Convert race seconds to hours
    total_time_in_hours = total_time_in_sec / 3600

    # Convert race kilometers to miles
    race_distance_in_miles = round(distance_in_km / 1.61, 2)

    # Calculate average pace
    seconds_per_mile = round(total_time_in_sec / race_distance_in_miles)
    pace_in_minutes, pace_in_seconds = divmod(seconds_per_mile, 60)

    # Calculate race average speed
    speed_in_mph = round(race_distance_in_miles / total_time_in_hours, 2)

    # Outputs:
    print(f"Your race was {race_distance_in_miles} miles long!")
    print(f"You finished the race with an average speed of {speed_in_mph} miles per hour.")
    print(f"Your pace was {pace_in_minutes} minutes and {pace_in_seconds} seconds per mile.")


race_stats()
