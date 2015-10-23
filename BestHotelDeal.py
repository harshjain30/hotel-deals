import csv
import sys

def readCSV(f):
	reader = csv.reader(f)
	for row in reader:
		print(row)

if __name__ == '__main__':
	try:
		with open(sys.argv[1]) as f:
			readCSV(f)
	except EnvironmentError as err:
		print("Error reading csv file:" + err)