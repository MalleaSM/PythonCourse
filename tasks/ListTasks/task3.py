"""
Loan payment calculator
"""

# Get the details of the loan from the user: How much money do you owe, in dollars?​
money_owed = input('How much money do you owe, in dollars?\n')
# Convert input to float​
money_owed = float(money_owed)

# Get the annual percentage rate: what us the annual percentage rate?​
apr = input('what us the annual percentage rate?\n')
apr = float(apr)
# Get the monthly payment: what will your monthly payment be, in dollars?​
payment = input('what will your monthly payment be, in dollars?\n')
payment = float(payment)
# Get  months to calculate results: how many months do you want to see the results for?​
months = input('how many months do you want to see the results for?\n​')
months = int(months)
# Repeat the calculation for all the months the user  wants to see results for​

# Divide annual percentage rate by 100 to make it a percent, then divide by 12 to get the monthly insterest rate
#   monthly_rate = apr/100/12
# add in  interest
#   interest_paid = money_owed * monthly_rate
#   money_owed = money_owed + interest_paid
# Make payment
#   money_owed = money_owed - payment
# Print the results 
#   print("Paid", payment, "of which", interest_paid, "was interest")
#   print("Now, I owe", money_owed)
month_count=1
while  month_count < months:
    monthly_rate = float(apr)/100/12
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    money_owed = money_owed - payment
    money_owed = round(money_owed, 2)
    if(money_owed < 0):
        print("the last payment is", money_owed)
        print("You pay off the loan in", month_count, "months")
        break
    else:
        print("Paid", payment, "of which", interest_paid, "was interest")
        print("Now, I owe", money_owed)

    month_count = month_count+1

# add control to check if money_owed - payment < 0 then print messages and break repetition
#   print("the last payment is", money_owed)
#   print("You pay off the loan in", month_count, "months")

# round the dollar amount to two decimals   
