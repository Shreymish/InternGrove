# Input variables
weather = "sunny"  # could also be "rainy" or "snowy"
time_of_day = "morning"  # could be "afternoon", "evening", or "night"

# Basic if-else AI decision tree
if weather == "sunny":
    if time_of_day == "morning":
        activity = "Go for a jog in the park"
    elif time_of_day == "afternoon":
        activity = "Have a picnic outdoors"
    elif time_of_day == "evening":
        activity = "Take a walk and enjoy the sunset"
    else:
        activity = "Stargazing might be nice tonight"
elif weather == "rainy":
    if time_of_day == "morning":
        activity = "Read a book by the window"
    elif time_of_day == "afternoon":
        activity = "Visit a local museum"
    elif time_of_day == "evening":
        activity = "Watch a movie at home"
    else:
        activity = "Listen to calming music indoors"
elif weather == "snowy":
    if time_of_day == "morning":
        activity = "Build a snowman outside"
    elif time_of_day == "afternoon":
        activity = "Go skiing or sledding"
    elif time_of_day == "evening":
        activity = "Warm up with hot cocoa by the fire"
    else:
        activity = "Bundle up and watch the snow fall"
else:
    activity = "Condition not recognized"

print("Suggested activity: {}".format(activity))
