#finance_calculators.py
#Pseudocode:
#Display what investment and bond means to the user.
#Ask the user for an input of investment or bond.
#Depending on their answer, create a control structure that will calculate
#their finances.
#If investment is chosen, ask user for details like deposit, interest rate and years investment.
#Assign all user-inputs to certain variables.
#Create control structure to ask for simple or compound interest.
#If simple, use arithmetic operators to calculate and then display their amount of money.
#If compound, use arithmetic operators to calculate and then display their amount of money.

#If bond is chosen, ask user for details like house value, interest rate and months to repay the bond.
#Assign all user-inputs to certain variables.
#Calculate monthly interest rate and assign to a variable.
#Use arithmetic operators to calculate how much the user needs to repay for the bond each month.
#Display the amount to the user.

import math
print()
print("investment - to calculate the amount of interest you'll earn on your investment")
print()
print("bond - to calculate the amount you'll have to pay on a home loan")
print()
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
print()

user_input = user_input.lower()   #using .lower() prevents code breakage issues from capital letters

while user_input != "investment" and user_input != "bond":    # while loop used to avoid code breakage

    print("Your entry is invalid.")

    user_input = input("Please enter either 'investment' or 'bond':")

else:
    if user_input == "investment":

        user_deposit = float(input("How much would you like to deposit in your account? "))           #used float() for user input for a more accurate calculation
        print()

        interest_rate = float(input("What is your interest rate as a percentage? (do not input '%')")) #figured that interest isn't usually an integer, so made it a float
        print()

        years_investment = int(input("How many years do you plan to invest for?"))                     #int() or float() can work here. But most people would just input an integer
        print()

        interest = input("Do you want simple or compound interest? \nPlease enter 'simple' or 'compound':")

        interest = interest.lower()                                                                    #using .lower() prevents code breakage issues from capital letters
        print()

        while interest != "simple" and interest != "compound":                                         # while loop used to avoid code breakage
            
            print("Your entry is invalid.")

            interest = input("Please enter either 'simple' or 'compound':")
        
        else:

            if interest == 'compound':
                
                total_amount_compound = user_deposit * math. pow((1+interest_rate), years_investment)
            
                print("The amount of money you have with compound interest is: £ {}".format(round(total_amount_compound,2)))   

                #used the round() function as floats produce very long numbers, but we are dealing with money which should only have 2 decimal places.

            if interest == 'simple':
                
                total_amount_simple = user_deposit * ( 1 + (interest_rate / 100) * years_investment)
                
                print("The amount of money you have with simple interest is: £{}".format(round(total_amount_simple,2)))


    elif user_input == "bond":
        
        value_house = float(input("What is the present value of your house?"))
        print()
        interest_rate = float(input("What is your interest rate as a percentage? (do not input '%')"))
        print()
        months_repay_bond = int(input("How many months will it take for you to repay the bond? "))
        print()

        monthly_interest_rate = (interest_rate / 100) / 12

        repayment_bond = (monthly_interest_rate * value_house) / (1 - (1+monthly_interest_rate) ** (- months_repay_bond))

        print("The amount of money you have to repay each month is: £{}".format(round(repayment_bond,2)))
    





