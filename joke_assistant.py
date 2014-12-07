#!/usr/bin/env python -v
import os
import random
import feedparser


# Create A Shortlist From Our 3 Article Sources


# Article Sources 
feed = feedparser.parse('http://www.dailymail.co.uk/news/index.rss')


def listAllTitles(article_source):
	for article in article_source.entries:
		print article['title']

def articlesTitlesList(article_source):
	titlelist = []
	for article in article_source.entries:
		titlelist.append(article)
	return titlelist


def listAllLinks(article_source):
	for article in article_source.entries:
		print "* " + article['link']

def listAllSummaries(article_source):
	for article in article_source.entries:
		print "* " + article['summary']
		#print "* " + article.summary_detail.type
def listRandomTitles(article_source, count):
	articletitlelist = []
	randolist = []
	for article in article_source.entries:
		articletitlelist.append(article.title)
	for articletitle in random.sample(articletitlelist, int(count)):
		randolist.append(articletitle)
	for article in randolist:
		print article
		
def getAuthor(article_source):
	for article in article_source.entries:
		print article.entries.author


def returnHtmlPageWithLinks(article_source):
	for article in article_source.entries:
		print article['title']

print feed
print "ba"
#print articlesTitlesList(feed)
#listRandomTitles(dailyMail, 10)
#listAllTitles(feed)
#listAllLinks(dailyMail)
#listAllSummaries(dailyMail)
#getAuthor(dailyMail)
#print dailyMail.entries[1].links
#print dailyMail.entries[1].summary_detail.type
#print dailyMail.feed.title.encode('utf-8')
#print feed.feed.link
#listAllLinks(dailyMail)