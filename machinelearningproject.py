
#importing data for exploring and manipulating data

import pandas as pd

#important part of the Pandas library is the DataFrame.DataFrame holds data

#Loading and exploring the data we use the commands below

# save filepath to variable for easier access
vat_tax_payers = '/Users/stellahrotich/Desktop/All-VAT Taxpayers as at May 13,2018..xlsx'

# read the data and store data in DataFrame titled vat_data
vat_data = pd.read_csv(vat_tax_payers) 

# print a summary of the data 
vat_tax_payers.describe()
