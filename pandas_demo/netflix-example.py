import pandas as pd
from functools import reduce
import os
# author: Dax Patel

# script to analyze netflix data
# for given list of actors and actresses, we use
# pandas to extract and manipulate data to compare
# different stars' presence on Netflix per year
# data source: https://www.kaggle.com/shivamb/netflix-shows/
#
# In this script we
# 1. Create a table dataset from CSV 
# 2. print the dataset
# 3. perform dataset manipulation by adding a column for year_added
# 4. perform dataset string search using regex filter
# 5. perform data analysis function for aggregating movie titles per star

# netflix titles data, with corresponding meta data, 6236 rows
fname = './netflix_titles.csv'

# read the csv as data frame object
df = pd.read_csv(fname)

# example list of starts to draw analysis from
stars = ['Jon Hamm','Ellie Kemper', 'Morgan Freeman']

# extract just the year and save it as a column
df['year_added'] = pd.DatetimeIndex(df['date_added']).year

# build a regex to search within the cast column and return relevant rows containing
# all stars in the list, and don't search inside the cells with invalid values

# initialize list of data frames for all stars
result = []
# for each start get a sum of their starring occurrences by year
for star in stars:
    data = df[df['cast'].str.contains(star, case=False, na=False)]
    res = data.groupby(data['year_added'])['show_id'].count().reset_index(name=star)
    result.append(res)

# apply outer join for all data frames
stars_by_releases = reduce(lambda left,right: pd.merge(left,right,how='outer',on='year_added').fillna(0), result)

# print by year 
print(stars_by_releases.sort_values(by=['year_added']))