import csv
import string

# Open the CSV File and read it in.
f = open('cities.csv')
data = f.read()

# Split the data into an array of countries.
cities = data.split('\n')

length = len(cities)
# Start your search algorithm here.
def bubbleSort(cities):
    for x in range(len(cities)-1,0,-1):
        for i in range(x):
            if cities[i]>cities[i+1]:
                temp = cities[i]
                cities[i] = cities[i+1]
                cities[i+1] = temp
bubbleSort(cities)
print("The cities are: ") 
print(cities)

def binarySearch(cities, search):
	
	first = 0
	last = len(cities)-1
	found = False
	
	while first<=last and not found: 
		midpoint = (first + last)//2 #once the fist becomes bigger than last, it is not in the list, (since each element of the list corresponds to the numbers)
		if cities[midpoint] == search:
			found = True
		else:
			if search < cities[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1 #first keeps getting bigger/ changing

	if not found:
		print("Sorry, that city is not in the list")
	else:
		print(cities[midpoint] + " was found")
	
search = input("What city do you want to find?")	
binarySearch(cities, search)
		
