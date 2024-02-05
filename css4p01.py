# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:10:34 2024

@author: KeolebogileSebogodi
"""


import pandas as pd
df=pd.read_csv("movie_dataset.csv.")

# Display data types of each column
data_types = df.dtypes
print(data_types)


# Check for missing values
missing_values = df.isnull()

# Display the DataFrame with True/False indicating missing values
print(missing_values)


# Count the number of missing values in each column
missing_count = df.isnull().sum()
print(missing_count)


# Replace NaN values with a specific value, e.g., 0
df_filled = df.fillna(0)

# Check the filled
print(df_filled)

#QUESTION 1: What is the highest rated movie in the dataset?

highest_rated_movie = df.loc[df['Rating'].idxmax()]

print("Highest Rated Movie:")
print(highest_rated_movie)



#QUESTION 2:What is the average revenue of all movies in the dataset?
average_revenue = df['Revenue (Millions)'].mean()
print("Average Revenue of All Movies:", average_revenue)



# QUESTION 3: What is the average revenue of movies from 2015-2017?
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()

print("Average Revenue (Millions) from 2015 to 2017:", average_revenue_2015_to_2017)



#QUESTION 4: How many movies were released in Year 2016
movies_2016_count = df['Year'].value_counts().get(2016, 0)

print("Number of Movies Released in 2016:", movies_2016_count)



#QUESTION 5:How many movies were directed by Christopher Nolan?
movies_directed_by_nolan = df[df['director'] == 'Christopher Nolan'].shape[0]

print("Number of Movies Directed by Christopher Nolan:", movies_directed_by_nolan)



#QUESTION 6:How many movies in the dataset have a rating of at least 8.0
highly_rated_movies_count = df[df['Rating'] >= 8.0].shape[0]

print("Number of Movies with a Rating of at Least 8.0:", highly_rated_movies_count)



#QUESTION 7:What is the median rating of movies directed by Christopher Nolan
nolan_movies_ratings = df[df['Director'] == 'Christopher Nolan']['Rating']

median_rating_nolan_movies = nolan_movies_ratings.median()

print("Median Rating of Movies Directed by Christopher Nolan:", median_rating_nolan_movies)



#QUESTION 8:Find the year with the highest avaerage rating
average_rating_by_year = df.groupby('Year')['Rating'].mean()

year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print("Year with the Highest Average Rating:", year_highest_average_rating)
print("Highest Average Rating:", highest_average_rating)



#QUESTION 9:What is the percentage increase in number of movies made between 2006 and 2016?
movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]

percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print(f"Percentage Increase in Number of Movies between 2006 and 2016: {percentage_increase:.2f}%")



#QUESTION 10:Find the most common actor in all movies.
# Sample dataset
data = {
    "Title": ["Guardians of the Galaxy", "Prometheus", "Split", "Sing", "Suicide Squad"],
    "Actors": [
        "Chris Pratt, Vin Diesel, Bradley Cooper, Zoe S...",
        "Noomi Rapace, Logan Marshall-Green, Michael Fa...",
        "James McAvoy, Anya Taylor-Joy, Haley Lu Richar...",
        "Matthew McConaughey,Reese Witherspoon, Seth Ma...",
        "Will Smith, Jared Leto, Margot Robbie, Viola D...",
    ],
}

df = pd.DataFrame(data)

# Splitting and flattening the 'Actors' column
all_actors = [actor.strip() for actors in df['Actors'] for actor in actors.split(',')]

# Counting occurrences of each actor
actor_counts = pd.Series(all_actors).value_counts()

# Extracting the most common actor
most_common_actor = actor_counts.idxmax()

print(f"The most common actor is: {most_common_actor}")



#QUESTION 11: How many unique genres are there in the dataset?
# Sample dataset
data = {
    "Title": ["Guardians of the Galaxy", "Prometheus", "Split", "Sing", "Suicide Squad"],
    "Genre": [
        "Action,Adventure,Sci-Fi",
        "Adventure,Mystery,Sci-Fi",
        "Horror,Thriller",
        "Animation,Comedy,Family",
        "Action,Adventure,Fantasy",
    ],
}

df = pd.DataFrame(data)

# Splitting and flattening the 'Genre' column
all_genres = [genre.strip() for genres in df['Genre'] for genre in genres.split(',')]

# Finding the number of unique genres
unique_genres_count = len(set(all_genres))

print(f"The number of unique genres is: {unique_genres_count}")



#QUESTION 12:Do a correlation of the numerical features, what insight can you deduce ? 
#The numerical features in the dataset are "Year," "Runtime (Minutes)," "Rating," "Votes," "Revenue (Millions)," and "Metascore."
# Sample dataset
data = {
    "Title": ["Guardians of the Galaxy", "Prometheus", "Split", "Sing", "Suicide Squad"],
    "Year": [2014, 2012, 2016, 2016, 2016],
    "Runtime (Minutes)": [121, 124, 117, 108, 123],
    "Rating": [8.1, 7.0, 7.3, 7.2, 6.2],
    "Votes": [757074, 485820, 157606, 60545, 393727],
    "Revenue (Millions)": [333.13, 126.46, 138.12, 270.32, 325.02],
    "Metascore": [76.0, 65.0, 62.0, 59.0, 40.0],
}

df = pd.DataFrame(data)

# Calculate correlation matrix
correlation_matrix = df.corr()

# Extracting top 10 correlations
top_correlations = correlation_matrix.unstack().sort_values(ascending=False).drop_duplicates()[1:11]

print("Top 10 correlations:")
print(top_correlations)