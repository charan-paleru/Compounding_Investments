monthly_income = int(input("Enter monthly income that you earn : "))
print('Note:'
      'About 10% to 15% is the average preferred percentage of your monthly income that can be put for investments')
percent_of_income = float(input("Enter the percentage of your income you would like to invest monthly : "))
monthly_investment = monthly_income * percent_of_income / 100
print(f'about {percent_of_income:1.1f}% of your monthly income is {monthly_investment:1.2f} rupees')
years = int(input('Enter the number of years you would like to stay in investing : '))
answer = input(f"Would you be continuously investing every month for {years} years (Y/N) : ")
while answer != 'Y' and answer != 'N':
    print('Enter in the form (Y/N) properly : ')
    answer = input(f"Would you be continuously investing every month for {years} years (Y/N) : ")
if answer == 'Y':
    print(f'So you choose to invest continuously for {years} years every month')
    interest = int(input('Enter expected annual interest growth rate : '))
    total_invested = monthly_investment * years * 12
    amount = monthly_investment * 12
    total_amount = 0
    for _ in range(years):
        total_amount = total_amount + amount
        total_amount = total_amount + (total_amount * (interest / 100))
    print(f'Total amount you would have invested for {years} years would be {total_invested} rupees')
    print(f'Your investment of {monthly_investment} rupees every month for {years} years'
          f' at an interest rate of {interest}% will grow up to be {total_amount:1.2f} rupees')
    print(f'Your returns would be {total_amount / total_invested:1.2f}x times your invested amount')
elif answer == 'N':
    investment_years = int(input('If you would not be continuously investing enter for how many years you would be '
                                 'investing monthly : '))
    if investment_years > years:
        while investment_years > years:
            print(f'Enter value less than {years}')
            investment_years = int(input('Enter for how many years you would be investing monthly : '))
    interest = int(input('Enter expected annual interest growth rate : '))
    total_investment = monthly_investment * 12 * investment_years
    yearly_amount = monthly_investment * 12
    total_amount = 0
    for i in range(years):
        if i < investment_years:
            total_amount = total_amount + yearly_amount
        total_amount = total_amount + (total_amount * (interest / 100))
    print(f'Total amount you would have invested for {investment_years} years would be {total_investment} rupees')
    print(f'Your investment of {monthly_investment} rupees every month for {investment_years} years '
          f'and remaining with the investment for a total of {years} years would grow up to be {total_amount:1.2f} '
          f'rupees')
    print(f'Your returns would be {total_amount / total_investment:1.2f}x times your invested amount')
