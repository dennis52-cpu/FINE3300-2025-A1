# FINE 3300 - Assignment 1 (Mortgage & Exchange Rates)
Author: Dennis Han (219615848)

This repository contains all deliverables for FINE 3300 - Assignment #1.
The first part includes a Python implementation of a Mortgage Payment calculator using semi-annual compounding → EAR → periodic rates → present value of annuity (PVA).

The second part involves implementation of an Exchange Rates utility that loads Bank of Canada rates from a .csv file and converts amounts via CAD (supports USD↔CAD and other currencies present in the file).

### Requested output (Part 1, MortgagePayments)

PS C:\Users\Dennis\OneDrive\Desktop\Python FINE 3300> & C:\Users\Dennis\AppData\Local\Programs\Python\Python312\python.exe "c:/Users/Dennis/OneDrive/Desktop/Python FINE 3300/FINE 3300 Assignment #1.py"       
Please input your quoted rate as a percentage: 5.5
Please input your amortization period in years: 25
Please input your principal amount: 100000
Monthly Payment: $610.39
Semi-monthly Payment: $304.85
Bi-weekly Payment: $281.38
Weekly Payment: $140.61
Rapid Bi-weekly Payment: $305.2
Rapid Weekly Payment: $152.6

### First Requested Output  (Part 2, ExchangeRates)

PS C:\Users\Dennis\OneDrive\Desktop\Python FINE 3300> & C:\Users\Dennis\AppData\Local\Programs\Python\Python312\python.exe "c:/Users/Dennis/OneDrive/Desktop/Python FINE 3300/FINE 3300 Assignment #2.py"

Available currencies to convert: AUD, BRL, CAD, CHF, CNY, EUR, GBP, HKD, IDR, INR, JPY, KRW, MXN, MYR, NOK, NZD, PEN, RUB, SAR, SEK, SGD, THB, TRY, TWD, USD, VND, ZAR
Please enter the amount you would like to convert: 100000
Please enter the currency you are converting from: CAD
Please enter the currency you are converting to: USD
Result: 100000.0 CAD -> 73003.36 USD

### Second Requested Output (Part 2, ExchangeRates)

PS C:\Users\Dennis\OneDrive\Desktop\Python FINE 3300> & C:\Users\Dennis\AppData\Local\Programs\Python\Python312\python.exe "c:/Users/Dennis/OneDrive/Desktop/Python FINE 3300/FINE 3300 Assignment #2.py"

Available currencies to convert: AUD, BRL, CAD, CHF, CNY, EUR, GBP, HKD, IDR, INR, JPY, KRW, MXN, MYR, NOK, NZD, PEN, RUB, SAR, SEK, SGD, THB, TRY, TWD, USD, VND, ZAR
Please enter the amount you would like to convert: 100000
Please enter the currency you are converting from: USD
Please enter the currency you are converting to: CAD
Result: 100000.0 USD -> 136980.0 CAD

### Assumptions / Notes
- Input quoted rate is provided as percent (e.g. 5.5 for 5.5%). The program converts to decimal internally.
- Monetary results are rounded to two decimals for display.
- The CSV is assumed to be ordered by date (top=oldest, bottom=latest); if not, the program still selects the last non-NaN per column as latest.
- The assignment requires USD↔CAD. I made it so the general converter also supports other currencies available in the CSV.


