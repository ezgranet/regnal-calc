import dateutil
from dateutil.relativedelta import relativedelta
import datetime
import os
import csv
kings = csv.reader(open("rgnl1.csv", "rt"))
john = csv.reader(open("john.csv", "rt"))

year = int(input('Enter a year     '))
month = int(input('Enter a month     '))
day = int(input('Enter a day    '))
thedate = datetime.datetime(year, month, day)
jstartyear = 1199
jstartmonth = 5
jstartday = 27
jstart = datetime.datetime(jstartyear, jstartmonth, jstartday)
jendyear = 1216
jendmonth = 10
jendday = 19
jend = datetime.datetime(1216, 10, 19)


def regn(date):
    return  datetime.datetime.strptime(date, '%d/%m/%Y')
if thedate <= regn('13/10/1066'):
	print(f'Too early!')

elif thedate >= regn('13/10/2072'):
		print(f'Too far in the future!')

elif regn('27/5/1199') <= thedate <= regn('19/10/1216'):
		for row in john:
			if regn(row[1]) <= thedate <= regn(row[2]) :
				thething = row[0]
				print(f'', row[0])
elif regn('3/10/1470') <= thedate <= regn('21 /05/1471'):
	print(f'49 Hen VI')

elif regn('20/10/1216') <= thedate <= regn('12/10/2072'):
	for row in kings:
		if regn(row[1]) <= thedate <= regn(row[2]) :
			some_date = regn(row[1])
			rdelta = relativedelta(thedate,some_date)
			print(rdelta.years+1, row[0])