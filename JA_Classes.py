#!/usr/bin/env python 
import os
import random
import feedparser


class ArticleFeed():
	def __init__(self, name, thumbnail_image, rss_feed_url):
		self.feed_name = name
		self.feed_url = rss_feed_url

	def articlesTitlesList(self):
		parsedfeed = feedparser.parse(self.feed_url)
		index_list_of_lists = []
		num = 0
		for article in parsedfeed.entries:
			pairing_list = []
			article_num =  str(num) + "-" + article['title']
			print article_num
			num = num + 1
			pairing_list.append(num)
			pairing_list.append(article.title)
			index_list_of_lists.append(pairing_list)
		return index_list_of_lists

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


class ArticleShortList():
	def __init__(self, timestamp):
		self.timestamp = timestamp
	
	# Get the list of lists generated ArticleFeed instance and the choices for shortlist and return those article tiles as a list
	# Worth keeping as class as they may be more than one short list needed - if not convert to module or keep in script.

	def getArticlesShortListFromIndexChoice(self, index_article_list, indexchoicestring):
		indexChoiceList = indexchoicestring.split(" ")
		article_shortlist = []
		print "---------"
		print "shortlist"
		print "---------"
		for num in indexChoiceList:
			for sublist in index_article_list:
				if str(sublist[0]) == str(num):
					article_shortlist.append(sublist[1])
					print sublist[1]
		return article_shortlist



		


















class Article():
	def __init__(self, name, rss_feed_url):
		self.article_name = name
		self.feed_url = rss_feed_url
		print "hello"
	def printArticle(self):
		 '''follow link grab text and print to stdout'''
		 print "hello"

	def saveArticletoDB(self):
		 print "hello"	
	def loadArticleFromDB(self):
		print "hello"	
	def RemoveArticleFromDB(self):
		print "hello"	

class Draft():
		def __init__(self, name, jtype, jsetup, jpunchline, rss_feed_url):
			self.name = name
			self.jtype = jtype
			self.jsetup = jsetup
			self.jpunch = jpunchline
			self.rss_feel_url = rss_feed_url

		def printSetup(self):
			print self.jsetup

		def printPunch(self):
			print self.jpunch

class Joke():
	def __init__(self, name, setup, punchline, rss_feed_url):
		self.name = name
	

