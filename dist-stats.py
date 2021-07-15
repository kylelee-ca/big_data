##  import libraries
import csv, sys 
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np


# taking command-line arguments into variables 
file = sys.argv[1] # csv_file
city = sys.argv[2] # name_of_city

# Common catogories 
categories = ["Korean", "Japanese", "Chinese", "Italian", "Mexican", "British", "American", "Vietnamese", "Thai", "Greek", "Pakistani", "Indian", "Canadian", "Himalayan", "Hawaiian", "Irish", "Egyptian", "Nepalese", ]
# A dictionary where key is category and the value is the list of freq, #reviews, avg_stars
dict = {}

# csv reader
# row[4] - name of city 
# row[9] - number of stars of the business 
# row[10] - number of reviews 
# row[12] - category of the business
with open(file, encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader: 
        if line_count == 0:
            pass
        else :
            ## if the business is in the city given and the category of the business is "Restaurants"
            if row[4].lower() == city.lower() and row[12].lower().__contains__("restaurants"):
                for type in categories:
                    # if the category of restaurant exists in the category list
                    if row[12].__contains__(type):
                        # if the dictionary already has values for the type, increment by correct values
                        if type in dict.keys(): 
                            values = dict.get(type)
                            values[0] += 1 
                            values[1] += int(row[10])
                            values[2] += float(row[9])
                        # else, add list of values to the dictionary 
                        else :
                            dict[type] = [1, int(row[10]), float(row[9])]
        line_count += 1

# rounding numbers of stars 
for i in dict.values():
    i[2] = round(i[2]/i[0],1)
        
"""
PART 1
"""

# sort the dictionary by the number of restaurants in descending order
# then print to the console
category_sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
print("### ### ###")
# print("restaurantCategoryDist")
print("category : #restaurants")
for i in category_sorted_dict:
    print(i[0],":", i[1][0])

"""
PART 2
"""
# sort the dictionary by the number of reviews in descending order
# then print to the console
review_sorted_dict = sorted(dict.items(), key=lambda x: x[1][1], reverse=True)
print("### ### ###")
# print("restaurantReviewDist")
print("category : #reviews : avg_stars")
for i in review_sorted_dict:
    print(i[0],":", i[1][1],":", i[1][2])


"""
PART 3
"""


objects = []
performance = []

# append the top 10 key-value pairs of the category_sorted_dict to 2 separate lists
for i in range(10):   
    objects.append(category_sorted_dict[i][0])
    performance.append(category_sorted_dict[i][1][0])


y_pos = np.arange(len(objects))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('# Restaurants')
plt.title('The Top 10 Restaurant Categories')

plt.show()