#!/usr/bin/env python3

#WHICH OLYMPIC SPORT IS BEST FIT FOR YOUR BODY TYPE?

import time

#create a dictionary with key:value pairs

question1 = {
        "Question": "How tall are you?",
        "A. Very, and don't ask me how the weather is up there.": "[basketball, high jumping, boxing, hurdling, rowing, swimming, tennis, throwing, volleyball]",
        "B. Average. I can buy clothes off the rack.": "[cycling, soccer, wrestling]",
        "C. Short. I'm barely allowed on roller coasters.": "[gymnastics, diving, marathon, sprinting, weightlifting]"
}

question2 = {
        "Question": "For your height, do you have long legs with a short torso?",
        "A. Yes. I seem to be mostly legs.": "[basketball, volleyball, cycling, high jumping, hurdling, running, rowing]",
        "B. No. My torso is long and my shirts never stay tucked in.": "[boxing, wrestling, throwing, gymnastics, diving, sprinting, swimming, water polo,throwing]"
}

question3 = {
        "Question": "Do you have long arms for your height?",
        "A. Yes, all my sleeves are too short.": "[basketball, boxing, rowing, swimming, throwing, water polo, volleyball]",
        "B. No, I'm a little bit like a T Rex": "[gymnastics, weightlifting]"
}

question4 = {
        "Question":"Do you have big feet or big hands?", 
        "A. Big feet. Boats, really.": "[swimming, sprinting]",
        "B. Big hands": "[basketball, volleyball, swimming, water polo, weightlifting]",
        "C. Both": "[swimming, sprinting, basketball, volleyball, swimming, water polo, weightlifting]",
        "D. Neither": "none"
}

question5 = {
        "Question": "Are your shoulder broad or narrow?", 
        "A. Broad. I can carry the world on them": "[boxing, rowing, swimming, water polo, throwing]",
        "B. Narrow. I'm more of a lightweight.": "[cycling, gymnastics, marathon]",
        "C. Neither": "none"
}

question6 = {
        "Question": "Where are your beefiest muscles?",
        "A. Upper body. Wanna see my guns?": "[archery, boxing, gymnastics, tennis]",
        "B. Lower body. My legs kick butt.": "[cycling, sprinting, hurdling, soccer]",
        "C. Everywhere. My muscles have muscles.": "[rowing, swimming, water polo, throwing, weightlifting, wrestling]",
        "D. My muscles aren't beefy. I'm kind of scrawny.": "[high jumping, marathon, volleyball]",
       
}

#Turn dictionaries into list
question1_list = list(question1.keys())
question2_list = list(question2.keys())
question3_list = list(question3.keys())
question4_list = list(question4.keys())
question5_list = list(question5.keys())
question6_list = list(question6.keys())

print("What Olympic Sport Is Best Fit For Your Body Type?")

time.sleep(3)

def main():
        basketball = 0
        boxing = 0
        cycling = 0 
        high_jumping = 0
        hurdling = 0
        rowing = 0
        running = 0
        shooting = 0
        swimming = 0
        tennis = 0
        throwing = 0
        volleyball = 0
        water_polo = 0
        
        print("Question 1...")
        time.sleep(3)
        print(question1["Question"])
        time.sleep(3)
        print(question1_list[1])
        time.sleep(2)
        print(question1_list[2])
        time.sleep(2)
        
        while True:
                try:
                        q1answer = input("Please choose letter A, B or C \n")
                        q1answer = q1answer.upper()
                        if q1answer not in ["A", "B", "C"]:
                                print("Please make a valid choice between A, B or C")
                                continue
                        elif q1answer == "A":
                               basketball += 1
                               high_jumping +=1
                               boxing += 1 
                               hurdling += 1 
                               rowing += 1 
                               swimming += 1 
                               tennis += 1 
                               throwing += 1 
                               volleyball += 1
                        elif q1answer == "B":
                                cycling +=1
                                soccer += 1
                                wrestling += 1
                        elif q1answer == "C":
                                gymnastics += 1
                                diving += 1
                                marathon += 1
                                sprinting += 1
                                weightlifting += 1

                        break
                except:
                        print("Try again!")


main()
