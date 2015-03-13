file = open("CurrentTermWorkshopSchedule.csv")

import csv
import sys

reader =csv.DictReader(file)



for row in reader:
	workshop_name = row['value']
	if not workshop_name=="Introduction to Python (October 24)": continue
	
	email_address = row["Email.Address"]

	sys.stdout.write(email_address+"; ")
