#logic.py

#Need to create smth with a logical error
#how abt... a wishing calculator?
#How wish system works:
#90 wishes = guaranteed 5* character, but 50/50 chance
#4* item or character gained with every 10 wishes
#Increased chance of 5* character around 75th roll >> I ignored this rule for this task :D
#
#
#
#Pseudocode:
#Ask user how many wishes times they have pulled
#If user has pulled 10 times, message says: congrats you have a 4* character
#If user has pulled 90 times, message says: congrats u have a 5* (include 50/50 roll)
#If user has pulled over 1000 times, message says: calm down, your bank account has insufficient funds
#

print(f"{"*" * 10} Welcome to your gacha wishing calculator !{"*" * 10}")

print()


while True:   #use while loop to ensure integer is entered
    try:                                                     
        number_wishes = int(input("How many wishes have you made? "))
        break  # break out of loop if integer has been inputed
    except ValueError:
        print("Invalid input. Please enter a whole number.")


print()


if number_wishes % 10 == 0:
    number_four_stars = int(number_wishes / 10)
    print(f"Congratulations! You have obtained: {number_four_stars} 4* characters!")

elif number_wishes >= 1000:
    print("Calm down, your bank account has insufficient funds for that.")


elif number_wishes == 90:
    import random

    fifty_fifty = ["5* featured character", "5* standard character"]
    probabilities = [0.5, 0.5]
    random_output = random.choices(fifty_fifty, weights=probabilities, k=1)  #weights is basically just the probabilties, k is how many times "5*..."etc is generated
    if random_output == "5* featured character":
        print(f"Congratulations! You have obtained a {random_output}! That is some good luck there ;)")
    else:
         print(f"Congratulations! You have obtained a {random_output}! Here is a Qiqi or a Diluc for you :)")

#this section above is a logical error because of the statement order. input 1000 and the code will only run the first statement (divisible by 10)


#corrected ver. that works
'''
if number_wishes >= 1000:
    print("Calm down, your bank account has insufficient funds for that.")

elif number_wishes == 90:
    import random

    fifty_fifty = ["5* featured character", "5* standard character"]
    probabilities = [0.5, 0.5]
    random_output = random.choices(fifty_fifty, weights=probabilities, k=1)  #weights is basically just the probabilties, k is how many times "5*..."etc is generated
    if random_output == "5* featured character":
        print(f"Congratulations! You have obtained a {random_output}! That is some good luck there ;)")
    else:
         print(f"Congratulations! You have obtained a {random_output}! Here is a Qiqi or a Diluc for you :)")

elif number_wishes % 10 == 0:
    number_four_stars = int(number_wishes / 10)
    print(f"Congratulations! You have obtained: {number_four_stars} 4* characters!")

'''


