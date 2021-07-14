
### Simple descriptive analytics 
### Computes and prints some statistics related to the input city

### Command to use the script 
### python-command current_script_file csv_file city_name 
### For example) python dstats.py yelp_business.csv Toronto




import sys
import csv

# taking command-line arguments into variables 
file = sys.argv[1] # csv_file
city = sys.argv[2] # name_of_city

numOfBus = 0
avgStars = 0
numOfRestaurants = 0
avgStarsRestaurants = 0
avgNumOfReviews = 0
avgNumOfReviewsBus = 0

# csv reader
# row[4] - name of city 
# row[9] - number of stars of the business
# row[12] - category of the business
with open(file, encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
    
        if line_count == 0:
            pass
        else:
            # if the business is in the city given in the command line, increment numOfBus.
            # to calculate values for Part A below
            if row[4].lower() == city.lower():
                numOfBus += 1
                avgStars += float(row[9])
                avgNumOfReviews += int(row[10])

            # if the category of the business in the city is "Restaurants", increment numOfRestaurants.
            # to calculate values for Part B below
            if row[12].lower().__contains__("restaurants"):
                numOfRestaurants += 1
                avgStarsRestaurants += float(row[9])
                avgNumOfReviewsBus += int(row[10])
        line_count += 1

## calculate and round
avgStars = round(avgStars / numOfBus, 1)
avgNumOfReviews = int(avgNumOfReviews / numOfBus)
avgStarsRestaurants = round(avgStarsRestaurants / numOfRestaurants, 1)
avgNumOfReviewsBus = int(avgNumOfReviewsBus / numOfRestaurants)


## print out the result to the console
## Part A
print("The number of businesses in ", city, ": ", numOfBus )
print("The average number of stars of a business in ", city, ": ",avgStars)
print("The average number of Reviews for all businesses in ", city, ": ", avgNumOfReviews)

## Part B
print("The number of restaurants in ", city, ": ", numOfRestaurants)
print("The average number of stars of a restaurant in ", city, ": ",avgStarsRestaurants)
print("The average number of Reviews for restaurants in ", city, ": ", avgNumOfReviewsBus)


