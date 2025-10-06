import pandas as pd

# Part 2: Exchange Rates
# Note: I used pandas to parse the .csv file because I'm pretty familiar with it even though its technically introduced next lecture
# The program collects user inputs (amount as float; from/to as strings)
# This program loads the BankofCanadaExchangeRates.csv, builds a “CAD per 1 unit of currency” map from columns ending in “/CAD” using the last non-NaN value, and performs FX conversions via CAD
# The class `ExchangeRates` stores `df` (DataFrame of the CSV), `date_col` (optional date column name that I didn't really end up using), and `rates_cad_per_currency` (dict of latest rates; includes "CAD": 1.0)
# All methods are public by Python convention except for `__init__` which builds the rates map, `supported_currencies()` returns a sorted list of codes, `convert(..)` converts the currencies via CAD
# Prints supported currencies and the conversion result with amounts rounded to 2 digits for display of the currencies
# This program assumes valid inputs and does not provide much data validation checks

class ExchangeRates:
    def __init__(self, csv_path, date_col=None):
        # Loads the .csv into a dataframe
        self.df = pd.read_csv(csv_path)
        # I coded it this way since the latest exchange rate is always at the bottom, I used the dataframe as is
        self.date_col = date_col
        df = self.df

        # This section builds a dictionary of the latest rates,
        # I'm looking to detect rate columns by names that end with "/CAD" since the .csv is formatted this way
        # Then for each column, the program will convert the values to numeric, drop the NaNs and take the last (latest) value

        self.rates_cad_per_currency = {}
        for column in df.columns:
            # Only proceed if this column is not the date column and its name ends with "/CAD"
            if column != self.date_col and str(column).upper().endswith("/CAD"):
                # Stores the currency code before the slash in variable named key
                key = str(column).split("/")[0].upper()
                # Stores the last numeric entry that is not null in that column in a variable called value
                value = float(pd.to_numeric(df[column], errors="coerce").dropna().iloc[-1])
                # This line adds the key value pair to the dictionary
                self.rates_cad_per_currency[key] = value

        # Add CAD as a base currency as it will be easier to compute other equations later
        self.rates_cad_per_currency["CAD"] = 1.0

    def supported_currencies(self):
        # Function that returns a sorted list of all currencies we have rates for
        return sorted(self.rates_cad_per_currency)

    def convert(self, amount, convert_from_currency, convert_to_currency):
        # This normalizes the input currency codes.
        from_currency = str(convert_from_currency).upper()
        to_currency = str(convert_to_currency).upper()

        # This looks up "CAD per 1 from" and "CAD per 1 to".
        convert_from_currency = self.rates_cad_per_currency[from_currency]
        convert_to_currency = self.rates_cad_per_currency[to_currency]

        # Universal conversion equation:
        return float(amount) * convert_from_currency / convert_to_currency

Exchange_rates = ExchangeRates("BankOfCanadaExchangeRates.csv")

# Show which currencies the user can do conversions with
print("\nAvailable currencies to convert:", ", ".join(Exchange_rates.supported_currencies()))

# Input from the user for the amount (float) and currencies they would like to convert from and to (str)
amount = float(input("Please enter the amount you would like to convert: "))
from_currency = str(input("Please enter the currency you are converting from: "))
to_currency = str(input("Please enter the currency you are converting to: "))

 # Compute and display the result using the latest rates map.
result = Exchange_rates.convert(amount, from_currency, to_currency)
print(f"Result: {round(amount,2)} {from_currency} -> {round(result,2)} {to_currency}")

