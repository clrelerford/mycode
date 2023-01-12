#!/usr/bin/env python3

"""Which Olympic Sport Is Best Fit For Your Body Type? | CRelerford"""

import time

#create a question dictionary
question1 = {
        "Question": "How tall are you?",
        "A. Very, and don't ask me how the weather is up there.": "[basketball, high_jumping, boxing, hurdling, rowing, swimming, tennis, throwing, volleyball]",
        "B. Average. I can buy clothes off the rack.": "[cycling, soccer, wrestling]",
        "C. Short. I'm barely allowed on roller coasters.": "[gymnastics, diving, marathon, sprinting, weightlifting]"
}

question2 = {
        "Question": "For your height, do you have long legs with a short torso?",
        "A. Yes. I seem to be mostly legs.": "[basketball, volleyball, cycling, high_jumping, hurdling, running, rowing]",
        "B. No. My torso is long and my shirts never stay tucked in.": "[boxing, wrestling, throwing, gymnastics, diving, sprinting, swimming, water_polo, throwing]"
}

question3 = {
        "Question": "Do you have long arms for your height?",
        "A. Yes, all my sleeves are too short.": "[basketball, boxing, rowing, swimming, throwing, water_polo, volleyball]",
        "B. No, I'm a little bit like a T Rex": "[gymnastics, weightlifting]"
}

question4 = {
        "Question":"Do you have big feet or big hands?", 
        "A. Big feet. Boats, really.": "[swimming, sprinting]",
        "B. Big hands": "[basketball, volleyball, swimming, water_polo, weightlifting]",
        "C. Both": "[swimming, sprinting, basketball, volleyball, water_polo, weightlifting]",
        "D. Neither": ["none"]
}

question5 = {
        "Question": "Are your shoulder broad or narrow?", 
        "A. Broad. I can carry the world on them": "[boxing, rowing, swimming, water_polo, throwing]",
        "B. Narrow. I'm more of a lightweight.": "[cycling, gymnastics, marathon]",
        "C. Neither": ["none"]
}

question6 = {
        "Question": "Where are your beefiest muscles?",
        "A. Upper body. Wanna see my guns?": "[archery, boxing, gymnastics, tennis]",
        "B. Lower body. My legs kick butt.": "[cycling, sprinting, hurdling, soccer]",
        "C. Everywhere. My muscles have muscles.": "[rowing, swimming, water_polo, throwing, weightlifting, wrestling]",
        "D. My muscles aren't beefy. I'm kind of scrawny.": "[high_jumping, marathon, volleyball]",
       
}

#Turn dictionaries into list
question1_list = list(question1.keys())
question2_list = list(question2.keys())
question3_list = list(question3.keys())
question4_list = list(question4.keys())
question5_list = list(question5.keys())
question6_list = list(question6.keys())

print("What Olympic Sport Is Best Fit For Your Body Type?")

#added time to give user a moment to read title
time.sleep(1)

def main():
        #created a dictionary to store the variables and their counts
        sports = {"archery": 0, "basketball": 0, "boxing": 0, "cycling": 0, 
          "diving": 0, "gymnastics": 0, "high_jumping": 0, "hurdling": 0,
          "marathon": 0, "rowing": 0, "running": 0, "shooting": 0, 
          "soccer": 0, "sprinting": 0, "swimming": 0, "tennis": 0, 
          "throwing": 0, "volleyball": 0, "water_polo": 0, 
          "weightlifting": 0, "wrestling": 0, "none": 0}

        
        print("Get ready!")
        time.sleep(1)
        print("Set!")
        time.sleep(1)
        print("Go!")
        time.sleep(1)

        #First question and selections printed from questions dictionary
        print(question1["Question"])
        print(question1_list[1])
        print(question1_list[2])
        print(question1_list[3])
        
        #begin while loop for answer input
        while True:
                try:
                        q1answer = input("\nPlease choose letter A, B or C \n")
                        q1answer = q1answer.upper()
                        if q1answer not in ["A", "B", "C"]:
                                print("Please make a valid choice between A, B or C")
                                continue
                        elif q1answer == "A":
                               sports["basketball"] += 1
                               sports["high_jumping"] +=1
                               sports["boxing"] += 1 
                               sports["hurdling"] += 1 
                               sports["rowing"] += 1 
                               sports["swimming"] += 1 
                               sports["tennis"] += 1 
                               sports["throwing"] += 1 
                               sports["volleyball"] += 1
                        elif q1answer == "B":
                                sports["cycling"] +=1
                                sports["soccer"] += 1
                                sports["wrestling"] += 1
                        elif q1answer == "C":
                                sports["gymnastics"] += 1
                                sports["diving"] += 1
                                sports["marathon"] += 1
                                sports["sprinting"] += 1
                                sports["weightlifting"] += 1
                        break
                except Exception as x:
                        print("Try again!", x)


        print(question2["Question"])
        print(question2_list[1])
        print(question2_list[2])

        while True:
                try:
                        q2answer = input("\nPlease choose letter A or B \n")
                        q2answer = q2answer.upper()
                        if q2answer not in ["A", "B"]:
                                print("Please make a valid choice between A or B")
                                continue
                        elif q2answer == "A":
                                sports["basketball"] += 1 
                                sports["cycling"] += 1 
                                sports["high_jumping"] += 1
                                sports["hurdling"] += 1
                                sports["rowing"] += 1
                                sports["running"] += 1
                                sports["volleyball"] += 1
                        elif q2answer == "B":
                                sports["boxing"] += 1
                                sports["diving"] += 1
                                sports["gymnastics"] += 1
                                sports["sprinting"] += 1
                                sports["swimming"] += 1
                                sports["throwing"] += 1
                                sports["water_polo"] += 1
                                sports["wrestling"] += 1
                        break
                except:
                        print("Try again!")

        print(question3["Question"])
        print(question3_list[1])
        print(question3_list[2])

        while True:
                try:
                        q3answer = input("\nPlease choose letter A or B \n")
                        q3answer = q3answer.upper()
                        if q3answer not in ["A", "B"]:
                                print("Please make a valid choice between A or B")
                                continue
                        elif q3answer == "A":
                                sports["basketball"] += 1 
                                sports["boxing"] += 1
                                sports["rowing"] += 1
                                sports["swimming"] += 1
                                sports["throwing"] += 1
                                sports["water_polo"] += 1
                                sports["volleyball"] += 1
                        elif q3answer == "B":
                                sports["gymnastics"] += 1
                                sports["weightlifting"] += 1
                        break
                except:
                        print("Try again!")    

        print(question4["Question"])
        print(question4_list[1])
        print(question4_list[2])
        print(question4_list[3])
        print(question4_list[4])
        
        while True:
                try:
                        q4answer = input("\nPlease choose letter A, B, C, or D \n")
                        q4answer = q4answer.upper()
                        if q4answer not in ["A", "B", "C", "D"]:
                                print("Please make a valid choice between A, B, C or D")
                                continue
                        elif q4answer == "A":
                               sports["swimming"] += 1 
                               sports["sprinting"] += 1
                        elif q4answer == "B":
                                sports["basketball"] +=1
                                sports["volleyball"] += 1
                                sports["swimming"] += 1
                                sports["water_polo"] += 1
                                sports["weightlifting"] += 1
                        elif q4answer == "C":
                                sports["swimming"] += 1 
                                sports["sprinting"] += 1
                                sports["basketball"] +=1
                                sports["volleyball"] += 1
                                sports["water_polo"] += 1
                                sports["weightlifting"] += 1
                        elif q4answer == "D":
                                sports["none"] += 1
                        break
                except Exception as x:
                        print("Try again!", x)

        print(question5["Question"])
        print(question5_list[1])
        print(question5_list[2])
        print(question5_list[3])
        
        while True:
                try:
                        q5answer = input("\nPlease choose letter A, B, or C \n")
                        q5answer = q5answer.upper()
                        if q5answer not in ["A", "B", "C"]:
                                print("Please make a valid choice between A, B, or C")
                                continue
                        elif q5answer == "A":
                                sports["boxing"] += 1 
                                sports["rowing"] += 1
                                sports["swimming"] += 1
                                sports["water_polo"] += 1
                                sports["throwing"] += 1
                        elif q5answer == "B":
                                sports["cycling"] +=1
                                sports["gymnastics"] += 1
                                sports["marathon"] += 1
                                sports["weightlifting"] += 1
                        elif q5answer == "C":
                                sports["none"] += 1
                        break
                except Exception as x:
                        print("Try again!", x) 
                    
        print(question6["Question"])
        print(question6_list[1])
        print(question6_list[2])
        print(question6_list[3])
        print(question6_list[4])
        
        while True:
                try:
                        q6answer = input("\nPlease choose letter A, B, C, or D \n")
                        q6answer = q6answer.upper()
                        if q6answer not in ["A", "B", "C", "D"]:
                                print("Please make a valid choice between A, B, C or D")
                                continue
                        elif q6answer == "A":
                               sports["archery"] += 1 
                               sports["boxing"] += 1
                               sports["gymnastics"] += 1
                               sports["tennis"] += 1
                        elif q6answer == "B":
                                sports["cycling"] +=1
                                sports["sprinting"] += 1
                                sports["hurdling"] += 1
                                sports["soccer"] += 1
                        elif q6answer == "C":
                                sports["rowing"] += 1
                                sports["swimming"] += 1
                                sports["water_polo"] += 1
                                sports["weightlifting"] += 1
                                sports["wrestling"] += 1
                        elif q6answer == "D":
                                sports["high_jumping"] += 1
                                sports["marathon"] += 1
                                sports["volleyball"] += 1
                        break
                except Exception as x:
                        print("Try again!", x)


        # find the variable with the highest count
        max_sport = max(sports, key=sports.get)
        print("Your body is best suited for:", max_sport, "\nStart training for the gold!")
        
main()
