import dateutil
from dateutil.relativedelta import relativedelta
import datetime
import os
import csv
from csv import reader
import re
kings = csv.reader(open("rgnl1.csv", "rt"))
john = csv.reader(open("john.csv", "rt"))
year = input('Enter a regnal or calendar year  (remember to use Roman numerals to number monarchs)    ')
alphyear =  "".join([ch for ch in year if ch.isalpha() or ch.isspace()])
salphyear = str(alphyear)
ylow = salphyear.lower()
yslow = str(ylow)
ryear = int(re.search("\d+", year)[0])

if any(c.isalpha() for c in year):
	if 'joh' in yslow :
		with open('john.csv', newline='') as csvfile:
			temp_reader = csv.reader(csvfile, delimiter=',')
			data = list(temp_reader)
			row_val,colval1,colval2 = ryear,1,2
		try:
	   		 print(data[row_val][colval1],' to ',data[row_val][colval2])
		except IndexError:
	    		print('No data found')
	elif year == '49 henry VI' or year =='49 henry vi' or year == '49 Henry VI' or year == '49 Hen VI' or year == '49 hen vi' or year == 'readeption' or year == 'Readeption':
		print('9 October 1470 to 14 April 1471')
	elif 'car iii' in yslow or 'charles iii' in yslow or 'char iii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 44,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear)  - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear)  - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'eliz ii' in yslow or 'elizabeth ii' in yslow:
				with open('rgnl1.csv', newline='') as csvfile:
					temp_reader = csv.reader(csvfile, delimiter=',')
					data = list(temp_reader)
				row_val,colval1,colval2 = 43,1,2
				accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
				startyear = ryear - 1
				endyear = ryear
				startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
				enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
				try:
					print(startdate,' to ',enddate)
				except:
					print('No data found')
	elif 'geo vi' in yslow or 'george vi' in yslow:
		with open('rgnl1.csv', newline='') as csvfile:
			temp_reader = csv.reader(csvfile, delimiter=',')
			data = list(temp_reader)
		row_val,colval1,colval2 = 42,1,2
		accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
		startyear = ryear - 1
		endyear = ryear
		startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
		enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
		try:
			print(startdate,' to ',enddate)
		except:
			print('No data found')
	elif 'edw viii' in yslow or 'edward viii' in yslow:
		with open('rgnl1.csv', newline='') as csvfile:
			temp_reader = csv.reader(csvfile, delimiter=',')
			data = list(temp_reader)
		row_val,colval1,colval2 = 41,1,2
		accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
		startyear = ryear - 1
		endyear = ryear
		startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
		enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
		try:
			print(startdate,' to ',enddate)
		except:
			print('No data found')

	elif 'george v' in yslow or 'elizabeth ii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 40,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'edw vii' in yslow or 'edward vii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 39,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'vic' in yslow or 'victoria' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 38,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'will iv' in yslow or 'william iv' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 37,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'geo iv' in yslow or 'george iv' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 36,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'geo iii' in yslow or 'george iii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 35,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'geo ii' in yslow or 'george ii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 34,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'geo i' in yslow or 'george i' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 33,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'geo i' in yslow or 'george i' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 33,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'ann' in yslow or 'anne' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 32,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'will iii' in yslow or 'william iii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 31,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'will and mar' in yslow or 'will & mar' in yslow or 'william and mary' in yslow or 'william & mary' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 30,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'jac ii' in yslow or 'jam ii' in yslow or 'james ii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 28,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'car ii' in yslow or 'char ii' in yslow or 'charles ii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 27,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'car i' in yslow or 'char i' in yslow or 'charles i' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 25,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'jac i' in yslow or 'jam i' in yslow or 'james i' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 24,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'eliz i' in yslow  or 'elizabeth i' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 23,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'ph & m' in yslow  or 'ph and  m' in yslow or 'philip and  mary' in yslow or 'philip &  mary' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 22,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'mar' in yslow  or 'mary' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 21,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'edw vi' in yslow  or 'edward vi' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 20,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'edw vi' in yslow  or 'edward vi' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 20,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'hen viii' in yslow  or 'henry viii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 19,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'hen vii' in yslow  or 'henry vii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 18,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'ric iii' in yslow  or 'richard iii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 17,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'ric iii' in yslow  or 'richard iii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 17,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')		
	elif 'edw v' in yslow  or 'edward v' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 16,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')		
	elif 'edw iv' in yslow  or 'edward iv' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 15,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')		
	elif 'hen vi' in yslow  or 'henry vi' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 14,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')		
	elif 'hen v' in yslow  or 'henry v' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 13,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')		
	elif 'hen iv' in yslow  or 'henry iv' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 12,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')		
	elif 'hen iv' in yslow  or 'henry iv' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 11,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')		
	elif 'ric ii' in yslow  or 'richard ii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 10,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')	
	elif 'edw iii' in yslow  or 'edward iii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 9,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')	
	elif 'edw ii' in yslow  or 'edward ii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 8,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')	
	elif 'edw i' in yslow  or 'edward i' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 7,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')	
	elif 'hen iii' in yslow  or 'henry iii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 6,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				ric('No data found')	
	elif 'ric i' in yslow  or 'richard i' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 5,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')	
	elif 'hen ii' in yslow  or 'henry ii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 4,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')
	elif 'steph' in yslow  or 'stephen' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 3,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')	
	elif 'hen i' in yslow  or 'henry i' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 2,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')	
	elif 'will ii' in yslow  or 'william ii' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 1,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')	
	elif 'will i' in yslow  or 'william i' in yslow:
			with open('rgnl1.csv', newline='') as csvfile:
				temp_reader = csv.reader(csvfile, delimiter=',')
				data = list(temp_reader)
			row_val,colval1,colval2 = 0,1,2
			accyear = datetime.datetime.strptime(data[row_val][colval1], '%d/%m/%Y').date()
			startyear = ryear - 1
			endyear = ryear
			startdate = accyear + relativedelta(years=startyear) - relativedelta(days=1)
			enddate = accyear + relativedelta(years=endyear) - relativedelta(days=1)
			try:
				print(startdate,' to ',enddate)
			except:
				print('No data found')	
	else:
		print('No data found')
else: 
	month = int(input('Enter a month     '))
	day = int(input('Enter a day    '))
	numyear = int(year)
	nummonth = int(month)
	numday = int(day)
	thedate = datetime.datetime(numyear, nummonth, numday)
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
	elif regn('3/10/1470') <= thedate <= regn('21/5/1471'):
		print(f'49 Hen VI')
	elif regn('20/10/1216') <= thedate <= regn('12/10/2072'):
		for row in kings:
			if regn(row[1]) <= thedate <= regn(row[2]) :
				some_date = regn(row[1])
				rdelta = relativedelta(thedate,some_date)
				print(rdelta.years+1, row[0])