# Tweet_Analysis


## Description

Twitter's API limits you to querying the most recent 3200 tweets.  I have  created a python program that will take input of whatever topic you would like to research / analyze.  it will return the English tweets and provide a sentimate anaysis on the tweets and display a grapic depiction.


## Requirements (or rather, what I used)

* python3
* Modules (via `pip`):
  * import tweepy
  *from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
  * from textblob import TextBlob
  * import matplotlib.pyplot as plt
  * import tkinter as tk
  * from tkinter import scrolledtext
  *[Twitter API developer credentials](https://dev.twitter.com)

## Example:

I'll run the script on Artifical Intelligence (AI) with 100 tweets.
![Run_script](https://github.com/Manchu505/Tweet_Analysis/assets/19881829/39603b87-b69c-4ad4-89cd-65d176f9d15d)
![results_script](https://github.com/Manchu505/Tweet_Analysis/assets/19881829/15355820-0dd7-4998-b130-b44aab85910d)

## Using the Scraper

* run `Tweet_Analysis.py` and add the arguments you desire.

## Twitter API credentials

* sign up for a developer account here https://dev.twitter.com/
* get your key here: https://apps.twitter.com/
* once you have your key, create a file 'config.py'  and fill in your info


