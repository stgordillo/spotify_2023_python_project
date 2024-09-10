import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# There is an error with the dataframe reading some unicode in the csv, 
# so I've added the encoding part so the data is readable
df = pd.read_csv("spotify2023.csv", encoding="ISO-8859-1")
df.head()

# Exploring dataframe
df.info()
df.describe()

# Removing columns and exploring for new dataframe
da = df.loc[:, ["track_name","artist(s)_name","artist_count","released_year","in_spotify_playlists", "in_spotify_charts", "streams", "danceability_%"]]
da.head()

da.info()
da.describe()

# Checking for duplicates/null values
da[da.duplicated()]
da.isnull().sum()

# Creating viz for top 10 artists
top_ten = da["artist(s)_name"].value_counts().head(10)

plt.figure(figsize=(12, 6))
plt.barh(top_ten.index[::-1], top_ten.values[::-1], color="purple")
plt.xlabel("Amount of Songs")
plt.ylabel("Artists")
plt.title("Top 10 Artists with the Most Songs")
plt.show()

print("Here is the list of the Top 10 Artists and how many songs they had in 2023:\n", top_ten)

# Troubleshooting data type to find why "streams" cannot be sorted by it's values 
da["streams"].dtype

# Changing the data types in "streams" from objects into useable numbers
da['streams'] = pd.to_numeric(da['streams'], errors="coerce")
da["streams"].dtype

# Creating viz for 10 most streamed songs
most_streamed = da[["track_name", "artist(s)_name", "streams"]].sort_values(by="streams", ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(most_streamed["track_name"], most_streamed["streams"], color="orange")
plt.xlabel("Number of Streams (In Billions)")
plt.ylabel("Song Name")
plt.title("Most Streamed Songs on Spotify in 2023")
plt.xticks(rotation=75)
plt.show()

print("Here is the list of the Top 10 most streamed songs:\n")
most_streamed

# Creating pie chart viz
most_streamed = da[['track_name', 'streams']].sort_values(by='streams', ascending=False).head(10)

plt.figure(figsize=(10, 8))
plt.pie(most_streamed['streams'], labels=most_streamed['track_name'], autopct='%1.1f%%', colors=plt.cm.tab10.colors)
plt.title('Most Streamed Songs on Spotify in 2023')
plt.show()

print("Here is the list of the Top 10 most streamed songs:\n")
most_streamed

# Averaging danceability
avg_dance = da.groupby("released_year")["danceability_%"].mean()

# Creating line chart viz
plt.figure(figsize=(10, 6))
sns.lineplot(x=avg_dance.index, y=avg_dance.values, color="purple")
plt.xlabel("Year")
plt.ylabel("Average Percent Danceability")
plt.title("Danceability over Time")
plt.xticks(rotation=45)
plt.show()
