import csv
import sys
import datetime

def calcDealValue(nightly_rate, deal_value, deal_type, eligible_nights):
	if deal_type == "pct":
		return float(deal_value)/100*float(nightly_rate)*eligible_nights
	if deal_type == "rebate":
		return float(deal_value)
	if deal_type == "rebate_3plus" and eligible_nights >= 3:
		return float(deal_value)
	return 0


def printBestDeal(f, hotel_name, checkin_date, nights):
	reader = csv.reader(f)
	
	#initialize best deal
	best_deal = (0, "")
	
	for row in reader:
		eligible = False
		if row[0] == hotel_name:
	 		start_date = datetime.datetime.strptime(row[5], "%Y-%m-%d")
	 		end_date = datetime.datetime.strptime(row[6], "%Y-%m-%d")
	 		checkout_date = checkin_date + datetime.timedelta(days=nights)
	 		
	 		#case 1: checkin date within deal period
	 		if checkin_date >= start_date and checkin_date <= end_date:
	 			eligible_nights = min((end_date-checkin_date).days+1, nights)
	 			eligible = True

	 		#case 2: checkout date within deal period
	 		elif checkout_date >= start_date and checkout_date <= end_date:
 				eligible_nights = min((checkout_date-start_date).days+1, nights)
 				eligible = True

 			#case 3: entire deal period within duration of stay
 			elif checkin_date <= start_date and checkout_date >= end_date:
 				eligible_nights = (end_date - start_date).days+1
 				eligible = True

	 		if eligible:
	 			#calculate deal value based on nights
	 			deal_value = calcDealValue(row[1], row[3], row[4], eligible_nights)
	 			
	 			#update best deal if required, ignore deals with same value
	 			if deal_value < best_deal[0]:
	 				best_deal = (deal_value, row[2])

	#print the best deal
	print (best_deal[1]) if best_deal[1] else print("no deal available")


if __name__ == '__main__':
	#check all arguments are present
	if len(sys.argv) != 5:
		print("Please provide all 4 inputs in the following order: /path/to/deals/file 'Hotel Name' date-of-booking nights")
		exit()
	
	#check hotel name is provided
	if not sys.argv[2]:
		print("Please enter a hotel name")
		exit()
	
	#check date is formatted
	try:
		checkin_date = datetime.datetime.strptime(sys.argv[3], "%Y-%m-%d")
	except ValueError:
		print("Please enter a valid date in the format: yyyy-(m)m-(d)d")
		exit()

	#check number of nights is a positive integer
	if not sys.argv[4].isdigit() or not int(sys.argv[4]):
		print("Please ensure that the number of nights you enter is positive and an integer")
		exit()
	
	#check deals file is accessible and print the best deal(s)
	try:
		with open(sys.argv[1]) as f:
			printBestDeal(f, sys.argv[2], checkin_date, int(sys.argv[4]))
	except EnvironmentError as err:
		print("Sorry, there was an error reading the file:", err)