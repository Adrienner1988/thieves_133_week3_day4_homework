#Using VS Code, Jupytor Notebook, and Object Oriented Programming, create a program that will calculate the Return on Investment(ROI) for a rental property.
#1. Income
#   Duplex
#       Rental Income = $2K
#       Laundry Income = 0
#       Storage = 0
#       Misc = 0
#   TOTAL MONTHLY INCOME = $2K
#2. Expenses
#       Tax = $150
#       Insurance = $100
#       Utilities = 0
#           Electric =
#           Water =
#           Sewer =
#           Gas =
#       HOA = 0
#       Lawn/Snow = 0
#       Vacancy = $100
#       Repairs = $100
#       Captial Expdenditures (CapEx) = $100
#       Property Management = $200
#       Mortgage: = $860
#   TOTAL MONTHLY EXPENSES = $1,610
#3. Cash Flow
#       Income - Expenses
#       2000    -   1610
#           $390
#   TOTAL MONTHLY CASH FLOW = $390
#4. Cash on Cash ROI
#       Down Payment = $40K
#       Closing Costs = $3K
#       Rehab Budget = $7K
#       Misc Other = 0
#   TOTAL INVESTMENT = $50K
#       Total Montly Cash Flow * 12
#               390     *   12
#       Annual Cash flow = $4,680
#       Annual Cash flow / Total Investment
#           4680 / 50000
#               .0963 = 9.36%
#   CASH ON CASH ROI = 9.36%


#  THE MATH
#   roi = (acf/ti) * 100
#   acf = tmcf * 12
#   ti = dp + cc + rb + mo
#   tmcf = inc - exp
#   inc = ri + li + si + mi
#   exp = tax + ins+ utl + hoa + ls + vac + rep + capex + pm + mort
#   utl = ele + h2o + sew + gas

class ROICalc():
    def __init__(self):
        self.calcIncome
        self.calcExpenses
        self.calcCashFlow
        self.calcROI 


#     def runner(self):
#         print('Welcome to the Bigger Pockets ROI (Return on Investment) Calculator! \nThis calculator will calculate your OVERALL ROI on your investments, or you can calculate each section separately.')
        
#         while True:
#              choice = input("\nWhat would you like to do? \nCalculate ROI on property 'ROI', calculate income 'income', calculate expenses 'expenses', calculate cash flow? 'flow', or 'quit' " ).lower()
#              print('\nPlease enter ALL values without extra characters such as $ or , .  ')

#              if choice == 'quit':
#                   print('\nThanks for visiting our ROI Calculator! If you change your mind, we would love you help you calculate the ROI on your investments in the future.')
#                   break
#              elif choice == 'income':
#                   self.calcIncome()
#              elif choice == 'expenses':
#                   self.calcExpenses()
#              elif choice == 'flow':
#                   self.calcCashFlow()
#              elif choice == 'roi':
#                   self.calcROI()
#              else:
#                   print('Invalid entry, please make another choice.')
                  

    def calcIncome(self):
        print('Welcome to the Bigger Pockets ROI (Return on Investment) Calculator!')
        print('\nPlease enter ALL values without extra characters such as $ or , .  ')
        rental = int(input('\nWhat is your monthly rental income? '))
        laundry = int(input('\nWhat is your monthly laundry income? '))
        storage = int(input('\nWhat is your monthly storage income? '))
        misc = int(input('\nWhat is your monthly miscellaneous income? '))
        inc_sum = int(rental) + int(laundry) + int(storage) + int(misc)
        print(f'\nYour total monthly income is ${inc_sum}.')   


    def calcExpenses(self):
        tax = int(input('\nWhat are your tax expenses? '))
        insurance = int(input('\nWhat are your insurance expenses? '))
        electric = int(input('\nWhat are your electric expenses? '))
        water = int(input('\nWhat are your water expenses? '))
        sewer = int(input('\nWhat are your sewer expenses? '))
        gas = int(input('\nWhat are your gas expenses? '))
        hoa = int(input('\nWhat are your HOA expenses? '))
        l_s = int(input('\nWhat are your lawn/snow expenses? '))
        vacancy = int(input('\nWhat are your vacancy expenses? '))
        repair = int(input('\nWhat are your repair expenses? '))
        capEx = int(input('\nWhat are your capital expenditures expenses? '))
        management = int(input('\nWhat are your property management expenses? '))
        mortgage = int(input('\nWhat is your mortgage? '))
        expe_sum = int(tax) + int(insurance) + int(electric) + int(water) + int(sewer) + int(gas) + int(hoa) + int(l_s) + int(vacancy) + int(repair) + int(capEx) + int(management) + int(mortgage)
        print(f'\nYour total monthly income is ${expe_sum}.')
        

    def calcCashFlow(self):
            print('\nYour total monthly cash flow is calculated by taking your income and subtracting your expenses.')
            total_inc = int(input('What is your income? '))
            total_expe = int(input('What is your expense? '))
            cash_flow = int(total_inc) - int(total_expe)
            print(f'\nYour total monthly income is ${cash_flow}.')
    

    def calcROI(self):
         print('\nNow a few more numbers and we will have your investment ROI.')
         down_pay = int(input('\nWhat is your down payment? '))
         closing_cost = int(input('\nWhat are your closing cost? '))
         rehab_budget = int(input('\nWhat is your rehab budget? '))
         misc_other = int(input('\nAre there any other miscellaneous expenses? '))
         total_investment = int(down_pay) + int(closing_cost) + int(rehab_budget) + int(misc_other)
         print(f'\nYour total investment is {total_investment}.')
         print('\nAlmost done! Now lets get your ROI.')
         total_cashflow = int(input('\nWhat is your total cash flow? '))
         annual_cash_flow = int(total_cashflow) * 12
         print(f'\nYour annual cash flow is {annual_cash_flow}.')
         roi = int(annual_cash_flow) / int(total_investment) * 100
         print(f'\nYour cash on can ROI is {roi}%.')

ROI = ROICalc()
# ROI.runner()
ROI.calcIncome()
ROI.calcExpenses()
ROI.calcCashFlow()
ROI.calcROI()


