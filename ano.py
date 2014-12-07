#!/usr/bin/env python -v
import os
import random
import feedparser

feed_url = 'http://www.dailymail.co.uk/news/index.rss'
parsedfeed = feedparser.parse(feed_url)
print parsedfeed

feed_url = 'http://www.dailymail.co.uk/news/index.rss'
parsedfeed = feedparser.parse('http://www.dailymail.co.uk/news/index.rss')
print parsedfeed
