import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')
length = len(countries)
print(countries[1])
print(countries)

# Start your search algorithm here.
def binarySearch(countries, search):
	
	first = 0
	last = len(countries)-1
	found = False
	
	while first<=last and not found: 
		midpoint = (first + last)//2 #once the fist becomes bigger than last, it is not in the list, (since each element of the list corresponds to the numbers)
		if countries[midpoint] == search:
			found = True
		else:
			if search < countries[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1 #first keeps getting bigger/ changing

	if not found:
		print("that country is not in the list")
	else:
		print(countries[midpoint] + " was found")
	
search = input("What country do you want to find?")	
binarySearch(countries, search)
		