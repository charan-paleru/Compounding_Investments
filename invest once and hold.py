initial_investment = int(input('Enter how much you want to invest : '))
years = int(input('Enter how many years you want to stay invested for : '))
interest_rate = float(input('Enter the expected annual interest rate : '))
investment=initial_investment
for _ in range(years):
    investment = investment+(investment*interest_rate)/100
print(f'Amount you had invested initially is {initial_investment} rupees')
print(f'If you would have stood invested with the initial amount of {initial_investment} rupees '
      f'for up to {years} years then your total returns would be {investment:1.2f} rupees')
print(f'You would have gained {investment/initial_investment:1.2f}x times your initial investment')