def suggest_activity(weather, time_of_day, health_status):
    # Decision tree based on weather, time of day, and health condition
    if weather == "sunny":
        if time_of_day == "morning":
            if health_status == "good":
                activity = "Go for a jog in the park"
            else:
                activity = "Do some light stretching indoors"
        elif time_of_day == "afternoon":
            if health_status == "good":
                activity = "Have a picnic outdoors"
            else:
                activity = "Sit under a tree and relax"
        elif time_of_day == "evening":
            if health_status == "good":
                activity = "Take a walk and enjoy the sunset"
            else:
                activity = "Watch the sunset from indoors"
        else:  # night
            activity = "Stargazing might be nice tonight"
    
    elif weather == "rainy":
        if time_of_day == "morning":
            if health_status == "good":
                activity = "Read a book by the window"
            else:
                activity = "Stay in bed and rest"
        elif time_of_day == "afternoon":
            if health_status == "good":
                activity = "Visit a local museum"
            else:
                activity = "Relax at home with a hot beverage"
        elif time_of_day == "evening":
            if health_status == "good":
                activity = "Watch a movie at home"
            else:
                activity = "Listen to calming music indoors"
        else:  # night
            activity = "Relax with a warm drink and unwind"
    
    elif weather == "snowy":
        if time_of_day == "morning":
            if health_status == "good":
                activity = "Build a snowman outside"
            else:
                activity = "Watch the snow fall from indoors"
        elif time_of_day == "afternoon":
            if health_status == "good":
                activity = "Go skiing or sledding"
            else:
                activity = "Watch a movie with a blanket"
        elif time_of_day == "evening":
            if health_status == "good":
                activity = "Warm up with hot cocoa by the fire"
            else:
                activity = "Stay warm and rest indoors"
        else:  # night
            activity = "Bundle up and watch the snow fall from inside"
    
    else:
        activity = "Invalid weather condition entered."
    
    return activity

# Main program to take user input
def main():
    # Taking user input
    weather = input("Enter the weather condition (sunny, rainy, snowy): ").lower()
    time_of_day = input("Enter the time of day (morning, afternoon, evening, night): ").lower()
    health_status = input("Enter your health status (good, not good): ").lower()
    
    # Get the suggested activity
    activity = suggest_activity(weather, time_of_day, health_status)
    
    # Output the suggested activity
    print("Suggested activity:", activity)

# Run the program
if __name__ == "__main__":
    main()
