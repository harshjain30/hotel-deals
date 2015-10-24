#Deal Format : Hotel Foobar,250,$50 off your stay 3 nights or more,-50,rebate_3plus,2016-03-01,2016-03-31
#Input Format : BestHotelDeal ./deals.csv "Hotel Foobar" 2016-03-05 3

import csv
import sys
import datetime

def findBestDeal(f,a):
	reader = csv.reader(f)
	for row in reader:
	 	#do something
			




if __name__ == '__main__':
	#check all arguments are present
	if len(sys.argv) != 5:
		print("Please provide 4 inputs in the following order: /path/to/deals/file 'Hotel Name' date-of-booking nights")
		exit()
	
	#check hotel name is provided
	if not sys.argv[2]:
		print("Please enter a hotel name")
		exit()
	
	#check date is formatted
	try:
		booking_date = datetime.datetime.strptime(sys.argv[3], "%Y-%m-%d")
	except ValueError:
		print("Please enter a valid date in the format: yyyy-(m)m-(d)d")
		exit()

	#check number of nights is a positive integer
	if not sys.argv[4].isdigit() or not int(sys.argv[4]):
		print("Please ensure that the number of nights you enter is positive and an integer")
	
	#check deals file is accessible and find the best deal(s)
	try:
		with open(sys.argv[1]) as f:
			findBestDeal(f, sys.argv[2], booking_date, int(sys.argv[4]))
	except EnvironmentError as err:
		print("Sorry, there was an error reading the file:", err)