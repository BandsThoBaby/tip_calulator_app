#If the bill was $150.00, split between 5 people, with 12% tip. 

print("Welcome to the tip calculator.")
bill_total = input("What was the total bill? $ ")
tip_percentage = input("What percentage tip would you like to give? ")
people_total = input("How many people to split the bill? ")

#turn the strings into integers
bill_total_int = int(bill_total)
tip_percentage_int = int(tip_percentage)
people_total_int = int(people_total)

#work out how much in $ the tip is
tip_total_int = bill_total_int * (tip_percentage_int / 100)

#work out the tip + bill final total
total_amount_int = bill_total_int + tip_total_int

#workout the amount owed per person
amount_pp_int = total_amount_int / people_total_int

#change the amount owed per person to 2 Decimal places
two_dp_amount_pp_int = format(amount_pp_int, ".2f")

#print the total owed per person
print("Each person should pay: $", two_dp_amount_pp_int)

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇