# Top Spotify Songs of 2023 - Python Project
## Introduction
Final project as a part of my Computer Programming II course. We were given the opportunity to choose whatever dataset we wanted.  I wanted to check out the most popular songs from a Spotify 2023 dataset. My plan was to take a look at which artists had the most songs in the list, what songs were the most streamed and finally play with one of the unique column categories in this particular dataset.

## Data Sources
The dataset used in this project was retrieved from a fairly popular Kaggle dataset found here: [Most Streamed Spotify Songs 2023](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/data).

The data provides information regarding song's various attributes, popularity, information and streaming stats in Spotify, Apple Music, Deeze, and Shazam.

## Analysis Report
This section is a quick summary of my findings. You can find the full code and comments in the [Analysis](https://github.com/stgordillo/spotify_2023_python_project/blob/main/ANALYSIS.py).

### Initial
To start, there was a compatibility problem with the unicode in the csv, and so I had to change the encoding from UTF-8 using encoding="ISO-8859-1" for it to read it as Latin-1. 

### Exploration
I explored the data, checking for nulls, data types and what would interest me in the analysis.  Found some nulls in two columns I didn't think I'd like to use, so I moved on to creating a new dataset without those and other columns.  

While I do think it would be interesting to look at some of the columns I wanted to remove, I think think it would be better in a more dedicated analysis looking at those specific parameters in a future project. I wasn't interested in charts besides Spotify so I removed Applem, Deeze and Shazam, as well as a lot of the unique song features like acousticness. I did leave danceability in as I did think it would be worth looking at. Lastly for this section, I checked for duplicates and nulls again, found none. 

At a later point in my analysis, I also ran into a problem with the streams column containing multiple datatypes in it, so I changed to change the data type to numeric in order to complete the particular analysis, explained later. 

### Findings
Initially I found that 2018 had the most popular songs in 2023. I also found that Taylor Swift had the most songs in the most streamed songs list with 34 songs compared to the next highest, TThe Weeknd with 22 songs.  I decided to visualize that information with a horizontal bar chart. 

I then wanted to see which songs had the most streams. Interestingly, the Weeknd had the most streams with nearly 4 trillion streams and Taylor Swift wasn't even in the top 10, despite having the most songs in the list. I decided to show this information in both a bar chart and a pie chart in order to showcase the different ways to look at this information. 

Finally, I wanted to make use of that song attribute, "danceability".  Here, I compared the danceability trait compared to the release year of songs and visualized it with a line chart in order to see that danceability had a large spike right before 2000, but has overall steadily increased over the years. 

## Visualizations
You can find my visualizations for the the analysis in [Visualizations](https://github.com/stgordillo/spotify_2023_python_project/blob/main/VISUALIZATIONS.md).
