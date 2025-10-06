# Part 1: Mortgage Payments
# This  script calculates mortgage payments for multiple schedules (monthly, semi-monthly, bi-weekly, weekly, plus accelerated versions)
# Given a principal (float), a quoted annual rate entered as a percent (float), and an amortization period in years (int). It converts the nominal semi-annual rate to an effective annual
# rate (EAR), derives the corresponding per-period rates, and uses the present value of an annuity (PVA) to compute payments, rounding money values to two decimals.
# Class & attributes: `MortgagePayment` has public attributes `quoted_rate` (stored as a decimal after converting the user’s percent input) and `amortization_period`
# Public Methods: effective_annual_rate(), periodic_rate(), payments(); Private Methodds: __pva__(), __round2__() used internally by payments().
# This program assumes valid inputs and does not provide data validation checks

# Ask the user for inputs and casts them as numbers, float for the quoted_rate and int for the amortization_period
quoted_rate = float(input("Please input your quoted rate as a percentage: "))
amortization_period = int(input("Please input your amortization period in years: "))
principal = float(input("Please input your principal amount: "))

class MortgagePayment:
    # initializer with the quoted_rate and amortization_period
    def __init__(self, quoted_rate, amortization_period):
        self.quoted_rate = quoted_rate / 100.0  # interpret input as percent
        self.amortization_period = amortization_period

    # This function converts the quoted nominal mortgage rate (compounded semi-annually) to the effective annual rate (EAR):
    def effective_annual_rate(self):
        quoted_rate = self.quoted_rate
        return ((1 + quoted_rate / 2) ** 2) - 1
    
    # Function that converts APR to EAR for a given frequency
    def periodic_rate(self, periods_per_year):
        EAR = self.effective_annual_rate()
        return (1 + EAR) ** (1 / float(periods_per_year)) - 1
    
    # Present Value of Annuity forumla: (1 - (1+r)^(-n)) / r   with r=0 returning n
    def __pva__(self, r, n):    
        if r == 0.0:
            return float(n)
        return (1 - (1.0 + r) ** (-float(n))) / r
    
    # Since we're working with money values, I thought it would be good to round 2 decimal places
    def __round2__(self, x):
        return round(x, 2)

    def payments(self, principal):

        # Values that reflect how many payment periods in a year
        MONTHLY = 12
        SEMI_MONTHLY = 24
        BI_WEEKLY = 26
        WEEKLY = 52

        # This function computs one schedule’s payment using the PVA formula
        def payment_for(frequency):
            r = self.periodic_rate(frequency)
            n = self.amortization_period * frequency
            return principal / self.__pva__(r, n)

        # These are for the regular schedules
        monthly_raw = payment_for(MONTHLY)
        semi_monthly_raw = payment_for(SEMI_MONTHLY)
        bi_weekly_raw = payment_for(BI_WEEKLY)
        weekly_raw = payment_for(WEEKLY)

        monthly = self.__round2__(monthly_raw)
        semi_monthly = self.__round2__(semi_monthly_raw)
        bi_weekly = self.__round2__(bi_weekly_raw)
        weekly = self.__round2__(weekly_raw)

        # These are for the accelerated schedules
        accel_bi_weekly = self.__round2__(monthly_raw / 2)
        accel_weekly = self.__round2__(monthly_raw / 4)

        #The tuple is returned as requested :3
        return (monthly, semi_monthly, bi_weekly, weekly, accel_bi_weekly, accel_weekly)

mortgage_calculation = MortgagePayment(quoted_rate, amortization_period)

monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly = mortgage_calculation.payments(principal)

# Printing it this way cause it was the requested format
print(f"Monthly Payment: ${monthly}")
print(f"Semi-monthly Payment: ${semi_monthly}")
print(f"Bi-weekly Payment: ${bi_weekly}")
print(f"Weekly Payment: ${weekly}")
print(f"Rapid Bi-weekly Payment: ${rapid_bi_weekly}")
print(f"Rapid Weekly Payment: ${rapid_weekly}")