monthly_investment = int(input("Enter amount you will invest monthly : "))
years = int(input("How many years do you want to stay invested in : "))
interest = float(input("Average interest rate : "))
amount = 12*monthly_investment
total_invested = monthly_investment*years*12
total_amount = 0
for _ in range(years):
    total_amount = total_amount+amount
    total_amount = total_amount+(total_amount*(interest/100))
print(f'Total amount you would have invested for {years} years would be {total_invested} rupees')
print(f'Your investment of {monthly_investment} rupees every month for {years} years'
      f' at an interest rate of {interest}% will grow up to be {total_amount:1.2f} rupees')
print(f'Your returns would be {total_amount/total_invested:1.2f}x times your invested amount')