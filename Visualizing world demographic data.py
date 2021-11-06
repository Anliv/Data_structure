#!/usr/bin/env python
# coding: utf-8

# In[9]:


class City:
    def __init__(self, code, name, region, population, latitude, longtitude):
        self.code = code
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longtitude = longtitude
    
    def __str__(self):
        A = str(self.name) + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longtitude)
        return A
    
    def get_population(self):
        return self.population
    
    def get_latitude(self):
        return self.latitude
    
    def get_name(self):
        return self.name



# Performs the quicksort algorithm.

# Partition the sublist the_list[p ... r] so that the pivot
# (originally in the_list[r]) moves to the_list[q],
# all items in the_list[p ... q-1] are less than or equal to the pivot,
# and all items in the_list[q+1 ... r] are greater than the pivot.
# Return the index q where the pivot ends up.
def partition(the_list, p, r, compare_func):
    pivot = the_list[r]
    
    # Set up the indices i and j so that
    #    the_list[p ... i] contains items <= pivot,
    #    the_list[i+1 ... j-1] contains items > pivot, and
    #    the_list[j ... r-1] contains items not yet compared with the pivot.
    i = p - 1
    j = p
    while j < r:
        if compare_func(the_list[j], pivot):
            # Move this item into the section known to be <= pivot.
            i += 1
            (the_list[i], the_list[j]) = (the_list[j], the_list[i])
        j += 1
            
    # Get the pivot into the correct position.
    (the_list[i+1], the_list[r]) = (the_list[r], the_list[i+1])
    return i+1

# Sort the sublist the_list[p ... r] using the quicksort algorithm.
def quicksort(the_list, p, r, compare_func):
    if p < r:   # nothing to do if the sublist has fewer than 2 items
        q = partition(the_list, p, r, compare_func) # divide
        quicksort(the_list, p, q-1, compare_func)   # conquer smaller items
        quicksort(the_list, q+1, r, compare_func)   # conquer larger items

# Sort the_list by running quicksort on it.        
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list)-1, compare_func)

# Return True if city1 has the same or higher population than city2.
def compare_population(city1, city2):
    return city1.get_population() >= city2.get_population()

# Return True if city1 comes at or before city2 alphabetically.
def compare_name(city1, city2):
    return city1.get_name().lower() <= city2.get_name().lower()

# Return True if city1's latitude is less than or equal to city2's latitude.
def compare_latitude(city1, city2):
    return city1.get_latitude() <= city2.get_latitude()


city_list = []
with open("world_cities.txt","r") as f:
    for l in f:
        city = l.split(",")
        city_list.append(City(str(city[0]), str(city[1]), str(city[2]), int(city[3]), float(city[4]), float(city[5])))
       
        

sort(city_list, compare_name)
with open("cities_alpha.txt","w") as f:
    for temp_city in city_list:
        f.write(str(temp_city)+"\n")
        
sort(city_list, compare_population)
with open("cities_population.txt","w") as f:
    for temp_city in city_list:
        f.write(str(temp_city)+"\n")
        
sort(city_list, compare_latitude)
with open("cities_latitude.txt","w") as f:
    for temp_city in city_list:
        f.write(str(temp_city)+"\n")


# In[8]:


import matplotlib.pyplot as plt
from time import sleep
from IPython import display

def longlat(latitude, longitude):
    x = int(round((WIDTH / 2) + (WIDTH / 2) * (longitude / 180)))
    y = HEIGHT - int(round((HEIGHT / 2) + (HEIGHT / 2) * (latitude / 90)))
    return (x, y)


WIDTH = 720 # image (world.png) width
HEIGHT = 360 # image height
DPI = 60 # display image at this dots-per-inch resolution

all_cities = []
with open("cities_population.txt","r") as f:
    for line in f:
        city = line.split(",")
        all_cities.append(city)
        
top_30_city = all_cities[0:30]


for i in range(0,len(top_30_city)):
    (top_30_city[i][2], top_30_city[i][3]) = longlat(float(top_30_city[i][2]), float(top_30_city[i][3]))


img = plt.imread("world.jpg")
for i in range(0,len(top_30_city)):    
    plt.figure(figsize=(WIDTH/DPI,HEIGHT/DPI))
    plt.imshow(img) # Display the image
    plt.axis('off')
    for j in range(0,i):
        plt.plot(float(top_30_city[j][2]), float(top_30_city[j][3]), 'bo')     
    plt.plot(float(top_30_city[i][2]), float(top_30_city[i][3]), 'ro')
    plt.text(float(top_30_city[i][2]) + 10, float(top_30_city[i][3]) - 10, top_30_city[i][0], size=10)
    plt.show()
    sleep(0.5); display.clear_output(wait=True)


# In[ ]:




