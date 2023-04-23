# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:42:12 2023

@author: 91809
"""

import snscrape.modules.twitter as tw
import pandas as pd
import pymongo
import streamlit as st
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["twitter_data"]


def store_data(tweet_data,keyword):
   collection = db[f'{keyword}']
   data = tweet_data.to_dict('records')
   collection.insert_many(data)


def scrape_twitter_data(keyword,start_date,end_date,tweet_limit):
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
        
     
    tweet_data= pd.DataFrame(tweets,columns=["date","id","url","content","user","reply_count","retweet_count","language","source","like_count"])
    return tweet_data



st.title("Twitter Data scraper")

keyword = st.text_input("Enter keyword or hashtag to search:")
start_date = st.date_input("Enter the start date:")
end_date =st.date_input("Ender end date:")
tweet_limit = st.number_input("Enter the number of tweets to scrape:",min_value=1,max_value=10000)


#scrape Twitter data and display in streamlit

if st.button("Scrape Twitter Data"):
    tweet_data= scrape_twitter_data(keyword, str(start_date), str(end_date), int(tweet_limit))
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
