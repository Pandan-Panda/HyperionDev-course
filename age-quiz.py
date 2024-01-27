#age-quiz.py

#both of the ways below work, the second method made more sense to me as there 
#were more categories from 40-100, but I had to mess around with indentation which
#was mildly annoying.
#I also put two methods b/c the first doesn't use an else statement
age = int(input("How old are you?"))


	
#if age <=13:                                           
	#print("You qualify for the kiddie discount.")
#elif age >= 100 :                       
	#print("Sorry, you're dead.")
#elif age >= 65:
	#print("Enjoy your retirement!")
#elif age >= 40 :
	#print("You're over the hill.")
#elif age == 21:
    #print("Congrats on your 21st!")
#elif 13 <= age <= 39:
	#print("Age is but a number")

if 39 < age <= 100:      #need to use 39 < because 40<= will not work
     if 39 < age <= 64:
        print("You're over the hill.")
     else:                                  #this else needs precise indentation so that it doesn't end/mess up the code
         print("Enjoy your retirement!")
elif age >= 100 :                       
	print("Sorry, you're dead.")
elif age == 21:
    print("Congrats on your 21st!")
elif age <= 13:
     print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")           #now that all previous criteria have been covered, this now 
                                            #leaves 14-39 years of age for the last else condition


