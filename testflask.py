#!/usr/bin/env python -v
import os
import random
import feedparser
from flask import Flask


app = Flask(__name__)

@app.route("/")
def articlesTitlesList():
	titlelist = []
	#titlelist = "111"
	feed = feedparser.parse('http://www.dailymail.co.uk/news/index.rss')
	for article in feed.entries:
		titlelist.append(article.title)
	titlestring = str(titlelist) 
	return str(titlestring)

if __name__ == "__main__":
    app.run()

