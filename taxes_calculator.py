
"""Tax rate	Single filers	Married filing jointly or qualifying widow(er)	Married filing separately	Head of household
10%	Up to $9,275	Up to $18,550	Up to $9,275	Up to $13,250
15%	$9,276 - $37,650	$18,551 - $75,300	$9,276 - $37,650	$13,251 - $50,400
25%	$37,651 - $91,150	$75,301 - $151,900	$37,651 - $75,950	$50,401 - $130,150
28%	$91,151 - $190,150	$151,901 - $231,450	$75,951 - $115,725	$130,151 - $210,800
33%	$190,151 - $413,350	$231,451 - $413,350	$115,726 - $206,675	$210,801 - $413,350
35%	$413,351 - $415,050	$413,351 - $466,950	$206,676 - $233,475	$413,351 - $441,000
39.6%	$415,051 or more	$466,951 or more	$233,476 or more	$441,001 or more"""

def get_tax_table():
    """this returns a tax table organized by filing status, and income percentage for each filing status"""
    status = ['income percentage', 'single filing range', 'married filing jointly or widow income range', 'married filing seperately income range',
             'head of household income range']
    income_percentage = [10,15,25,28,33,35,39.6]
    single_filing_income_range = [9275, 37650,91150,190150,413050,415050,415051]
    married_filing_jointly_or_widow_income_range = [18550,75300,151900,231450,413350,466950,466951]
    married_filing_seperately_income_range = [9275,37650,75950,115725,206675,233475,233476]
    head_of_household_income_range = [13250,50400,130150,210800,413350,441000,441001]
    groups = [status, income_percentage, single_filing_income_range,married_filing_jointly_or_widow_income_range,married_filing_seperately_income_range,head_of_household_income_range]
    return groups#,income_percentage,income_percentage,single_filing_income_range,married_filing_jointly_or_widow_income_range,married_filing_seperately_income_range,head_of_household_income_range

tax_table = get_tax_table()  # tax table is now referring to the function above
tax_table[4-2]
#status_index = tax_table[0].index('single')
#status_index

def is_valid(filing_status, income):
    """determines if filer has a valid filing status"""
    valid = ['single', 'married filing seperately', 'married filing jointly', 'widow', 'head of household']
    if isinstance(filing_status, basestring) and isinstance(income,int):     #determines if type of input is valid
        if filing_status in valid and income > 0:
            return True
        else:
            return False
            print "invalid input. Filing status must be 'single', 'married filing seperately', 'married filing jointly', 'widow', or 'head of household'"
            print "income must be greater than or equal to zero"

def tax():
    """uses the tax table to calculate taxes based on the filing status and income"""
    tax_table = get_tax_table()
    rates = tax_table[1]
    print 'enter filing status'  #included in function?
    filing_status = raw_input()   # to get input as a string
    print 'enter your income'
    income = input()
    valid = False
    valid = is_valid(filing_status, income)
    if valid == True:
        if filing_status == 'single':
            taxes = tax_table[3]
            i = 0
            tax = 0
            while taxes[i] < income:
                tax =  tax + rates[i] * (taxes[i+1] - taxes[i])
                i = i + 1
                tax = tax + rates[i-1] * (income - taxes[i])
        elif filing_status == 'married filing seperately':
            taxes = tax_table[4]
            i = 0
            tax = 0
            while taxes[i] < income:
                tax =  tax + rates[i] * (taxes[i+1] - taxes[i])
                i = i + 1
                tax = tax + rates[i-1] * (income - taxes[i])
        elif filing_status == 'married filing jointly':
            taxes = tax_table[5]
            i = 0
            tax = 0
            while taxes[i] < income:
                tax =  tax + rates[i] * (taxes[i+1] - taxes[i])
                i = i + 1
                tax = tax + rates[i-1] * (income - taxes[i])
    return int(tax)

"""This tells the percentage of income that goes to taxes"""
def percentage_of_tax(tax,income):
  return float(tax)/(income)*100       # the calculation for percentage of tax
"""this is the main function and tells the dollar amount and percentage of tax"""
def main(filing_status,income):
  if income < 0:
    print "invalid income"
    quit()
  if not is_valid(filing_status,income):
    print "invalid filing status"
    quit()
  this_tax = tax(filing_status,income)
  print "Tax: $" + str(this_tax)
  print "Tax as % of income:" + str(percentage_of_tax(this_tax, income))+ "%"
