import dateutil
from dateutil.relativedelta import relativedelta
import datetime
import os
import csv
kings = csv.reader(open("rgnl1.csv", "rt"))
year = int(input('Enter a year     '))
month = int(input('Enter a month     '))
day = int(input('Enter a day    '))
thedate = datetime.datetime(year, month, day)



def regn(date):
    return  datetime.datetime.strptime(date,"%d/%m/%Y")

if thedate <= regn('13/10/1066'):
	print(f'Too early!')

else: if thedate <= regn('13/10/2072'):
	print(f'Too far in the future!')

	
else:

	for row in kings:
		if regn(row[1]) <= thedate <= regn(row[2]) :
			some_date = regn(row[1])
			rdelta = relativedelta(thedate,some_date)
			print(rdelta.years+1, row[0])


