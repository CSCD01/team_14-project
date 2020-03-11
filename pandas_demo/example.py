# @@ -1,21 +1,50 @@
import pandas as pd

# author: William Song

# the BRICS are a set of countries: Brazil, Russia, India, China, and South Africa who are the major emerging national economies

# In this script we will"
# 1. Create a table dataset
# 2. print that dataset
# 3. perform dataset manipulation
# 4. perform dataset manipulation
# 5. perform a data analysis function on that dataset

# create a dictionary because it's easier
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

# 1. convert it to a DataFrame, a pandas datatype
brics = pd.DataFrame(dict)

# 2. print it out, notice how it's now in a numbered order?
print(brics)
print("\n================================\n")

# 3. now we will index this numbered order
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# print it out and now you can see the indexing happened in order
print(brics)
print("\n================================\n")

# 4. let's define a lambda function to calculate the population density
def populationDensity (row):
    return row["population"] / row["area"]

brics['density'] = brics.apply (lambda row: populationDensity(row), axis=1)
# we'll add a density column and apply this population density to every row
# (don't worry about axis for now)
brics["density"] = brics.apply (lambda row: populationDensity(row), axis=1)

# print it out and we have done all the manipulations we need
print(brics)
print("\n================================\n")

# finding the maximum density value (mdv)
maximum_index = brics["density"].idxmax()

# get the location of the mdv index in the density column
maximum_loc = brics.index.get_loc(maximum_index)

# printing the country name (denoted with the 0) with the mdv
print("The BRICS country with the highest population density is: " + brics.iloc[maximum_loc , 0])
