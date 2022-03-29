# Filename: scraping.py
# Description: A very simple example of how to get data via web scraping from a website. This small script retrieves conversion values and displays them via the terminal.
# Date: 09-10-2021
# Author: Greg Shalay

import time
import requests
from bs4 import BeautifulSoup

# URL prefix that will be used with the suffix and the desired conversion dollar type.
URL_PREFIX = "https://www.x-rates.com/table/?from="
URL_AMT_PREFIX = "&amount="
FROM = "from="
TO = "to="
OTHER_CURRENCIES = 10 # Represents a constant that holds the number of other currencies conversions displayed in the table.
NUM_COLS = 3
ONE_TRILLION = 1000000000000
NOT_FOUND = -1

#Currency Names
USDName = "US Dollar"
CADName = "Canadian Dollar"
EURName = "Euro"
GBPName = "British Pound"
INRName = "Indian Rupee"
AUDName = "Australian Dollar"
SGDName = "Singapore Dollar"
CHFName = "Swiss Franc"
MYRName = "Malaysian Ringgit"
JPYName = "Japanese Yen"
CNYName = "Chinese Yuan Renminbi"

# Currency Shorthands
USDShrt = "USD"
CADShrt = "CAD"
EURShrt = "EUR"
GBPShrt = "GBP"
INRShrt = "INR"
AUDShrt = "AUD"
SGDShrt = "SGD"
CHFShrt = "CHF"
MYRShrt = "MYR"
JPYShrt = "JPY"
CNYShrt = "CNY"

# Returns the currency name based on the shorthand version provided.
def shorthandToCurrencyName(shorthand):
	if(shorthand == USDShrt):
		return USDName
	elif(shorthand == CADShrt):
		return CADName
	elif(shorthand == EURShrt):
		return EURName
	elif(shorthand == GBPShrt):
		return GBPName
	elif(shorthand == INRShrt):
		return INRName
	elif(shorthand == AUDShrt):
		return AUDName
	elif(shorthand == SGDShrt):
		return SGDName
	elif(shorthand == CHFShrt):
		return CHFName
	elif(shorthand == MYRShrt):
		return MYRName
	elif(shorthand == JPYShrt):
		return JPYName
	elif(shorthand == CNYShrt):
		return CNYName

# Converts the integer input to the appropriate shorthand string version.
def convertInput(sel):
	if(sel.isdigit() == True):
		sel = int(sel)
		if(sel == 1):
			return USDShrt
		elif(sel == 2):
			return CADShrt
		elif(sel == 3):
			return EURShrt
		elif(sel == 4):
			return GBPShrt
		elif(sel == 5):
			return INRShrt
		elif(sel == 6):
			return AUDShrt
		elif(sel == 7):
			return SGDShrt
		elif(sel == 8):
			return CHFShrt
		elif(sel == 9):
			return MYRShrt
		elif(sel == 10):
			return JPYShrt
		elif(sel == 11):
			return CNYShrt
	else:
		sel = sel.upper()

	return sel

# Builds the request URL based on the user's input and then retrieves the data and presents it to the user.
def scrapeInfo(sel, amt):
	selection = ""
	selection = convertInput(sel)

	# Build URL
	URL = URL_PREFIX + str(selection) + URL_AMT_PREFIX + str(amt)

	req = requests.get(URL) 
	soup = BeautifulSoup(req.content, 'html.parser') 
	ratelist = soup.findAll("table", {"class": "ratesTable"})[0].findAll("tbody")

	for tableVal in ratelist:
		trList = tableVal.findAll('tr')
		for trVal in trList[:OTHER_CURRENCIES]:
			print()
			for tdVal in trVal:
				currentItem = str(tdVal)
				if(currentItem.find(FROM + selection) != NOT_FOUND): # Then the entry is converted from the selection.
					if(currentItem.find(TO + USDShrt) != NOT_FOUND):
						print(str(amt) + " " + shorthandToCurrencyName(selection) + " is " + tdVal.text + " " + shorthandToCurrencyName(USDShrt) + ".")
					elif(currentItem.find(TO + CADShrt) != NOT_FOUND):
						print(str(amt) + " " + shorthandToCurrencyName(selection) + " is " + tdVal.text + " " + shorthandToCurrencyName(CADShrt) + ".")
					elif(currentItem.find(TO + EURShrt) != NOT_FOUND):
						print(str(amt) + " " + shorthandToCurrencyName(selection) + " is " + tdVal.text + " " + shorthandToCurrencyName(EURShrt) + ".")
					elif(currentItem.find(TO + GBPShrt) != NOT_FOUND):
						print(str(amt) + " " + shorthandToCurrencyName(selection) + " is " + tdVal.text + " " + shorthandToCurrencyName(GBPShrt) + ".")
					elif(currentItem.find(TO + INRShrt) != NOT_FOUND):
						print(str(amt) + " " + shorthandToCurrencyName(selection) + " is " + tdVal.text + " " + shorthandToCurrencyName(INRShrt) + ".")
					elif(currentItem.find(TO + AUDShrt) != NOT_FOUND):
						print(str(amt) + " " + shorthandToCurrencyName(selection) + " is " + tdVal.text + " " + shorthandToCurrencyName(AUDShrt) + ".")
					elif(currentItem.find(TO + SGDShrt) != NOT_FOUND):
						print(str(amt) + " " + shorthandToCurrencyName(selection) + " is " + tdVal.text + " " + shorthandToCurrencyName(SGDShrt) + ".")
					elif(currentItem.find(TO + CHFShrt) != NOT_FOUND):
						print(str(amt) + " " + shorthandToCurrencyName(selection) + " is " + tdVal.text + " " + shorthandToCurrencyName(CHFShrt) + ".")
					elif(currentItem.find(TO + MYRShrt) != NOT_FOUND):
						print(str(amt) + " " + shorthandToCurrencyName(selection) + " is " + tdVal.text + " " + shorthandToCurrencyName(MYRShrt) + ".")
					elif(currentItem.find(TO + JPYShrt) != NOT_FOUND):
						print(str(amt) + " " + shorthandToCurrencyName(selection) + " is " + tdVal.text + " " + shorthandToCurrencyName(JPYShrt) + ".")
					elif(currentItem.find(TO + CNYShrt) != NOT_FOUND):
						print(str(amt) + " " + shorthandToCurrencyName(selection) + " is " + tdVal.text + " " + shorthandToCurrencyName(CNYShrt) + ".")
				elif(currentItem.find(TO + selection) != NOT_FOUND):
					if(currentItem.find(FROM + USDShrt) != NOT_FOUND):
						print(tdVal.text + " " + shorthandToCurrencyName(USDShrt) + " is 1 " + shorthandToCurrencyName(selection) + ".")
					elif(currentItem.find(FROM + CADShrt) != NOT_FOUND):
						print(tdVal.text + " " + shorthandToCurrencyName(CADShrt) + " is 1 " + shorthandToCurrencyName(selection) + ".")
					elif(currentItem.find(FROM + EURShrt) != NOT_FOUND):
						print(tdVal.text + " " + shorthandToCurrencyName(EURShrt) + " is 1 " + shorthandToCurrencyName(selection) + ".")
					elif(currentItem.find(FROM + GBPShrt) != NOT_FOUND):
						print(tdVal.text + " " + shorthandToCurrencyName(GBPShrt) + " is 1 " + shorthandToCurrencyName(selection) + ".")
					elif(currentItem.find(FROM + INRShrt) != NOT_FOUND):
						print(tdVal.text + " " + shorthandToCurrencyName(INRShrt) + " is 1 " + shorthandToCurrencyName(selection) + ".")
					elif(currentItem.find(FROM + AUDShrt) != NOT_FOUND):
						print(tdVal.text + " " + shorthandToCurrencyName(AUDShrt) + " is 1 " + shorthandToCurrencyName(selection) + ".")
					elif(currentItem.find(FROM + SGDShrt) != NOT_FOUND):
						print(tdVal.text + " " + shorthandToCurrencyName(SGDShrt) + " is 1 " + shorthandToCurrencyName(selection) + ".")
					elif(currentItem.find(FROM + CHFShrt) != NOT_FOUND):
						print(tdVal.text + " " + shorthandToCurrencyName(CHFShrt) + " is 1 " + shorthandToCurrencyName(selection) + ".")
					elif(currentItem.find(FROM + MYRShrt) != NOT_FOUND):
						print(tdVal.text + " " + shorthandToCurrencyName(MYRShrt) + " is 1 " + shorthandToCurrencyName(selection) + ".")
					elif(currentItem.find(FROM + JPYShrt) != NOT_FOUND):
						print(tdVal.text + " " + shorthandToCurrencyName(JPYShrt) + " is 1 " + shorthandToCurrencyName(selection) + ".")
					elif(currentItem.find(FROM + CNYShrt) != NOT_FOUND):
						print(tdVal.text + " " + shorthandToCurrencyName(CNYShrt) + " is 1 " + shorthandToCurrencyName(selection) + ".")
			print()

# Validates the user provided input for the dollar type.
def isValidInput(sel):
	if(sel.isdigit() == True):
		sel = int(sel) # Convert the string to an integer so that it can be compared against other integer literals.
		if(sel >= 1 and sel <= OTHER_CURRENCIES + 1):
			return True
		else:
			return False
	else:	
		sel = sel.upper()
		if(sel == USDShrt or sel == CADShrt or sel == EURShrt or sel == GBPShrt or sel == INRShrt or sel == AUDShrt or sel == SGDShrt or sel == CHFShrt or sel == MYRShrt
						  or sel == JPYShrt or sel == CNYShrt):
			return True
		else:
			return False
	
# Main function that executes the main loop of the program.
def menu():
	while True:
		print("Welcome to a simple Currency Converter. Select one of the following options to convert:")
		print(" 1. USD")
		print(" 2. CAD")
		print(" 3. EUR")
		print(" 4. GBP")
		print(" 5. INR")
		print(" 6. AUD")
		print(" 7. SGD")
		print(" 8. CHF")
		print(" 9. MYR")
		print("10. JPY")
		print("11. CNY")

		selection = input("Enter either the number beside the entry or the abbreviated dollar form. (ex. CAD or USD): ")

		# Run the input through the guantlet. (Check if it matches any of the shortforms or numeric assosiations from the menu.)
		if(isValidInput(selection) == True):
			break
		else:
			print("The input you entered was incorrect. Rerunning the program...")
			time.sleep(3) # Sleep for 3 seconds so that the user can read the error message.

	while True:
		amt = input("Please enter the amount you want to convert from. (must be a number greater than 0 and at most 1 000 000 000 000 ): ")

		if(amt.isdigit() == True):
			amt = float(amt)
			if(amt >= 0 and amt <= ONE_TRILLION):
				break
			else:
				print("Incorrect input. Reprompting for input...")
				time.sleep(2)

	scrapeInfo(selection, amt)
	

menu()
