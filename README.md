# Problem Description:         
Today, data is scattered everywhere in the world. Especially in social media, there may be a big quantity of data on Facebook, Instagram, Youtube, Twitter, etc. This consists of pictures and films on Youtube and Instagram as compared to Facebook and Twitter. To get the real facts on Twitter, you want to scrape the data from Twitter. You Need to Scrape the data like (date, id, url, tweet content, user,reply count, retweet count,language, source, like count etc) from twitter.
 
## Approach: 
* By using the “snscrape” Library, Scrape the twitter data from Twitter ReferenceSocial media scraping is one of the best things to happen to researchers looking to gather information about a particular social media platform.
* Create a dataframe with date, id, url, tweet content, user,reply count, retweet count,language, source, like count.
* Store each collection of data into a document into Mongodb along with the hashtag or key word we use to  Scrape from twitter. 
eg:({“Scraped Word”            : “Elon Musk”,
        “Scraped Date”             :15-02-2023,
        “Scraped Data”             : [{1000  Scraped data from past 100 days }]})
* Create a GUI using streamlit that should contain the feature to enter the keyword or Hashtag to be searched, select the date range and limit the tweet count need to be scraped. After scraping, the data needs to be displayed in the page and need a button to upload the data into Database and download the data into csv and json format.


# Introduction about Twitter Scraping:
  Social media scraping is one of the best things to happen to researchers looking to gather information about a particular social media platform.With this, you can extract the required data for your analysis while saving your time, effort, and money because bots automate the process. Twitter scraping is easy, as there are numerous Twitter scrapers in the market to pick from.
  
  
# Details about Library's and mpodules used in this project:
## snscrape:
snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts. The following services are currently supported: Facebook: user profiles, groups, and communities (aka visitor posts).

## pandas:
Pandas is an open-source library that is made mainly for working with relational or labeled data both easily and intuitively. It provides various data structures and operations for manipulating numerical data and time series. This library is built on top of the NumPy library. Pandas is fast and it has high performance & productivity for users.
## pymongo:
MongoDB is a document database used to build highly available and scalable internet applications. With its flexible schema approach, it's popular with development teams using agile methodologies.
## streamlit:
Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. It is a Python-based library specifically designed for machine learning engineers. 
# Explanation about project with codes:

### Step 1
import the necessary libraries/modules

* snscrape is used to scrape data from Twitter
* pandas is used for data manipulation
* pymongo is used to connect to MongoDB
* streamlit is used to build the web app.

~~~ python
import snscrape.modules.twitter as tw
import pandas as pd
import pymongo
import streamlit as st.
~~~
### Step 2
This function can be used to connect the mongodb server and store the scraped data 
in database named as twitter data

~~~python
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["twitter_data"]
~~~
### Step 3
Scraped twitter data taken as a pandas data frame and store the data in mongdb collection name as keyword.
~~~python
def store_data(tweet_data,keyword):
   collection = db[f'{keyword}']
   data = tweet_data.to_dict('records')
   collection.insert_many(data)
~~~
### Step 4
This is a Python function that uses the `TwitterSearchScraper` class from `twint` to scrape Twitter data. Here's how the function works:

1. The function takes four parameters: `keyword` (the keyword or hashtag to search), `start_date` and `end_date` (the date range to search), and `tweet_limit` (the number of tweets to scrape).

2. The function creates an empty list called `tweets`.

3. The function loops through the tweets returned by `TwitterSearchScraper`, adding each tweet's relevant information to the `tweets` list. The loop continues until the number of tweets in `tweets` is equal to `tweet_limit`.

4. The function creates a Pandas DataFrame called `tweet_data` from the `tweets` list, with columns for the tweet's date, ID, URL, content, user, reply count, retweet count, language, source, and like count.

5. The function returns the `tweet_data` DataFrame containing the scraped Twitter data.
~~~python
    tweets =[]
    
    for tweet in tw.TwitterSearchScraper (f"{keyword} since:{start_date} until:{end_date}").get_items():
        if len(tweets)==tweet_limit:
            break
        tweets.append([
            tweet.date,
            tweet.id,
            tweet.url,
            tweet.content,
            tweet.user.username,
            tweet.replyCount,
            tweet.retweetCount,
            tweet.lang,
            tweet.sourceLabel,
            tweet.likeCount
         ]) 
        
     
    tweet_data= pd.DataFrame(tweets,columns=["date","id","url","content",
     "user","reply_count","retweet_count","language","source","like_count"])
    return tweet_data
  ~~~
    
    
  ### Step 5
  This is a part of a Python script that uses the `streamlit` library to create a web app for the Twitter data scraper. Here's what this code does:

1. The `st.title()` function sets the title of the web app to "Twitter Data scraper".

2. The `st.text_input()` function creates a text box where the user can enter a keyword or hashtag to search on Twitter. The function returns the text entered by the user as a string.

3. The `st.date_input()` function creates two date pickers where the user can select the start and end dates for the Twitter search. The function returns the dates selected by the user as Python `datetime.date` objects.

4. The `st.number_input()` function creates a number input where the user can select the number of tweets to scrape. The function returns the number selected by the user as an integer, which is constrained between 1 and 10000 by the `min_value` and `max_value` arguments.

Together, these code snippets create a simple web app interface where the user can input the search parameters for the Twitter data scraper.


~~~python
st.title("Twitter Data scraper")

keyword = st.text_input("Enter keyword or hashtag to search:")
start_date = st.date_input("Enter the start date:")
end_date =st.date_input("Ender end date:")
tweet_limit = st.number_input("Enter the number of tweets to scrape:",
                              min_value=1,max_value=10000)
~~~
### Step 6
The above code block represents the Streamlit app's user interface for the Twitter data scraper. It includes three buttons, namely "Scrape Twitter Data," "Upload," and "Download." The code block checks for which button the user clicks and performs the respective action.

The first button "Scrape Twitter Data" uses the `scrape_twitter_data` function to get the desired data from Twitter based on the keyword or hashtag, start and end dates, and tweet limit, and then displays the data on the Streamlit app. If the data is successfully scraped, it shows a success message using `st.success()`.
 
The second button "Upload" also uses the `scrape_twitter_data` function to get the desired data from Twitter based on the keyword or hashtag, start and end dates, and tweet limit, and then stores the data in MongoDB using the `store_data()` function. If the data is successfully uploaded, it shows a success message using `st.success()`.

The third button "Download" first retrieves the data from Twitter based on the keyword or hashtag, start and end dates, and tweet limit using the `scrape_twitter_data` function, then prompts the user to enter a filename, converts the data to CSV and JSON formats, and provides download buttons to download the data in CSV and JSON formats.

~~~python
if st.button("Scrape Twitter Data"):
    tweet_data= scrape_twitter_data(keyword, str(start_date), str(end_date), 
                                    int(tweet_limit))
    st.write(tweet_data)
    st.success('Scraped Successfully!')

if st.button("Upload"):
    tweets_data=scrape_twitter_data(keyword, start_date, end_date, tweet_limit)
    store_data(tweets_data, keyword) 
    st.success('File Uploaded successfully')
    
if st.button("Download"):
    tweet_data=scrape_twitter_data(keyword, start_date, end_date, tweet_limit)    
    filename=st.text_input("Enter Filename:")
    csv =tweet_data.to_csv().encode('utf-8')
    json = tweet_data.to_json(orient='records')
    
    st.download_button(
             label="Download data as CSV",
             data=csv,
             file_name='filename.csv',
             mime='text/csv',
             )
    
    st.download_button(
             label = "Download data as json",
             data=json,
             file_name='filename.json',
             mime='application/json',
             )
~~~


  



