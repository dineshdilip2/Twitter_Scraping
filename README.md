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


