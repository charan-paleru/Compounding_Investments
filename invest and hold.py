monthly_investment = int(input('Enter amount you want to invest monthly : '))
investing_years = int(input('Enter how many years you would keep investing : '))
total_years = int(input('Enter how many years you would like to stay with the investment : '))
interest = float(input('Enter the expected expected annual interest rate : '))
total_investment = monthly_investment*12*investing_years
yearly_amount = monthly_investment*12
total_amount = 0
for i in range(total_years):
    if i < investing_years:
        total_amount = total_amount + yearly_amount
    total_amount = total_amount+(total_amount*(interest/100))
print(f'Total amount you would have invested for {investing_years} years would be {total_investment} rupees')
print(f'Your investment of {monthly_investment} rupees every month for {investing_years} years '
      f'and remaining with the investment for a total of {total_years} years would grow up to be {total_amount:1.2f} rupees')
print(f'Your returns would be {total_amount/total_investment:1.2f}x times your invested amount')
