#award.py
#Pseudocode: 
#Assign variables to each race. 
#Ask for an input for each race time.
#Check whether input is sensible (i.e no negative numbers, not 0)
#Add up the times and assign that to another variable.
#Compare the total time taken to the set conditions given, which then decide the output message (which award they got)



print("Today we shall find out if you got an award for your trialthon.")

swimming_time = int(input("Please enter how long it took you to complete the swimming race (in minutes):"))

while (swimming_time <= 0) == True :                        #I wanted to add in a control structure here to prevent invalid times from being put in.
    print("Please enter a valid time.")                     #If I wanted an infinite loop, I have to use while

    swimming_time = int(input("Please enter how long it took you to complete the swimming race (in minutes):"))


cycling_time = int(input("Please enter how long it took you to complete the cycling race (in minutes):"))

while (cycling_time <= 0) == True :                             
    print("Please enter a valid time.")

    cycling_time = int(input("Please enter how long it took you to complete the cycling race (in minutes):"))
       

running_time = int(input("Please enter how long it took you to complete the running race (in minutes):"))

while (running_time <= 0) == True :
       print("Please enter a valid time.")

       running_time = int(input("Please enter how long it took you to complete the running race (in minutes):"))
       


total_time_taken = swimming_time + cycling_time + running_time

print(f"You completed the race in {total_time_taken} minutes.")

if 0 < total_time_taken <= 100:
       print(f"Congratulations! You completed the race within the qualifying time.\n You are awarded Provincal Colours! ")
elif 100 < total_time_taken<= 105:
       print(f"Congratulations! You completed the race within 5 minutes of the qualifying time.\n You are awarded Provincal Half Colours!")
elif 105 < total_time_taken <= 110:
       print(f"Congratulations! You completed the race within 10 minutes of the qualifying time.\nYou are awarded Provincal Scroll!")
else:
       print(f"You completed the race more than 10 minutes off of the qualifying time.\n Thank you for participating! Better luck next time!")
