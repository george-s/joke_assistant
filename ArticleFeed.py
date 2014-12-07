#!/usr/bin/env python -v
import os
import random
import feedparser


class ArticleFeed():
	def __init__(self, name, rss_feed_url):
		self.feed_name = name
		self.feed_url = rss_feed_url

	def articlesTitlesList(self):
		parsedfeed = feedparser.parse(self.feed_url)
		print parsedfeed
		for article in parsedfeed.entries:
			print "-" + article['title']

	def articlesLinksList(self):
		parsedfeed = feedparser.parse(self.feed_url)
		print parsedfeed
		for article in parsedfeed.entries:
			print "-" + article['link']

	def articlesTitleLinkList(self):
		parsedfeed = feedparser.parse(self.feed_url)
		print parsedfeed
		for article in parsedfeed.entries:
			print '<a href="' + article['link'] + '">' + article['title'] + "</a><br>"



#	<a href="http://www.w3schools.com/html/">Visit our HTML tutorial</a>

dave = ArticleFeed('bbc','http://www.dailymail.co.uk/news/index.rss')

#print dave.articlesTitlesList()
#print dave.articlesLinksList()
print dave.articlesTitleLinkList()
