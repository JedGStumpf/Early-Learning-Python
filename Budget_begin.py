"""
Found this old gem.  1st "program" I wrote after a coulple entry level Python couses.
I might think about refactoring, restructuring into classes, possibly adding a UI...  to be continued?
Docstring added 3/17/2021  ///   Last saved prior 9/23/2019
"""


expense_list = []
bill_list = []
household = []
fun = []
income_list = []
paychecks = []
other_income = []
income_total = 0.0
expense_total = 0.0
available = 0.0


def done_or_not():
    done = input(
        "If you are surely done with this segment press 'Y' '\n' Otherwise press any key to continue: ")
    if done.upper().startswith('Y'):
        return False
    elif done == "" or done == " ":
        pass
    else:
        pass


def budget(*stumpf):

    def monthly(*other_income):
        while True:
            new_month = input(
                "Press 'Enter' if this is for the current Month\nPress 'N', to clear previous entries and carry on to a new Month: ")
            if new_month.upper().startswith("N"):
                available = 0.0
                cash_in = input("Enter your previous balance: ")
                if cash_in == float:
                    available += float(cash_in)
                    print(
                        "incorrect entry, please enter your previous months balance in numbers: ")
                    cash_in = input("Enter your previous balance: ")
                else:
                    if done_or_not() == False:
                        return False
            else:
                return False

    monthly()

    def funds(*income):
        # count = 0
        while True:
            cash_in = input(
                "Enter 'P' for Paycheck, 'O' for Other, or Enter to finish adding income: ")
            if cash_in.upper().startswith("P"):
                cash_add = input("Enter the amount of 'paycheck' income: ")
                if cash_add == int or float:
                    income_list.append(float(cash_add))
                    paychecks.append(float(cash_add))
                else:
                    print(
                        "incorrect entry, please enter your paycheck total in numbers: ")
                    cash_add = input("Enter the amount of 'paycheck' income: ")
            elif cash_in.upper().startswith("O"):
                cash_add = input("Enter the amount of 'other' income: ")
                if cash_add == int or float:
                    income_list.append(float(cash_add))
                    other_income.append(float(cash_add))
                else:
                    print(
                        "incorrect entry, please enter your other income total in numbers: ")
                    cash_add = input("Enter the amount of 'other' income: ")
            else:
                if done_or_not() == False:
                    list_income = income_list
                    list_paychecks = paychecks
                    list_other_income = other_income
                    print('\n\nIncome list:', list_income, '\nPaychecks:',
                          list_paychecks, '\nOther Income:', list_other_income)
                    return False
                else:
                    pass
    funds()

    def bills(*expenses):
        # count = 0
        while True:
            paid_out = input(
                "Enter 'B' for Bills, 'H' for Household, 'F' for Fun, or Enter to finish adding Expenses: ")
            if paid_out.upper().startswith("B"):
                bills_add = input("Enter the amount of the 'Bill': ")
                if bills_add == int or float:
                    expense_list.append(float(bills_add))
                    bill_list.append(float(bills_add))
                else:
                    print("incorrect entry, please enter your bill total in numbers: ")
                    bills_add = input("Enter the amount of the 'Bill': ")
            elif paid_out.upper().startswith("H"):
                household_add = input(
                    "Enter the amount of the 'Household' purchase: ")
                if household_add == int or float:
                    expense_list.append(float(household_add))
                    household.append(float(household_add))
                else:
                    print(
                        "incorrect entry, please enter your household bill total in numbers: ")
                    household_add = input(
                        "Enter the amount of the 'Household' purchase: ")
            elif paid_out.upper().startswith("F"):
                fun_add = input("Enter the amount of the 'Fun' purchase: ")
                if fun_add == int or float:
                    expense_list.append(float(fun_add))
                    fun.append(float(fun_add))
                else:
                    print(
                        "incorrect entry, please enter your fun bill total in numbers: ")
                    fun_add = input("Enter the amount of the 'Fun' purchase: ")
            else:
                if done_or_not() == False:
                    list_expense = expense_list
                    list_bills = bill_list
                    list_household = household
                    list_fun = fun
                    print('\n\nAll Expenses:', list_expense, '\nBills:', list_bills,
                          '\nHouse Expenses:', list_household, '\nFun Expenses:', list_fun)
                    return False
                else:
                    pass
    bills()

    def mula(income_total, expense_total, available):
        for money in income_list:
            income_total += money
        for payment in expense_list:
            expense_total += payment
        total_income = income_total
        total_expense = expense_total
        available += income_total - expense_total
        print('\n\n\n', 'Monthly Total Income:', total_income, '\nMonthly Total Expenses:',
              total_expense, '\nBalance after all income and expenses:', available)
    mula(income_total, expense_total, available)


budget()
