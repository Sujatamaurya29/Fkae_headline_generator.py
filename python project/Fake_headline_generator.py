#import the random module
import random

#create subjects
subjects = [
    "Sujata Maurya",
    "Virat Kohli",
    "Kajal Singh",
    "A Mumbai Cat",
    "A Group of Monkey",
    "Prime Minister Modi",
    "Auto Rahul Driver From Delhi"
]

action =[
    "Launches",
    "Cancles",
    "Dances with",
    "Eats",
    "Declares war on",
    "Orders",
    "Celebrates"
]

places_or_things =[
    "At Red Fort",
    "In Mumbai Local Train",
    "A Plate Of Momos",
    "Inside a Parliament",
    "At Ganga Ghat",
    "During IPL Match",
    "At India Gate"
]

# 3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(action)
    places_or_things = random.choice(places_or_things)
    
    headline =f" BREAKING NEWS: {subject} {action} {places_or_things}"
    print("\n"+ headline)
    
    user_input = input("\n Do you want another headline? (yes/no)").strip().lower
    if user_input =="no":
        break
    
    
print("\n Thanks for using the fake news headline generator.have a fun day")
    