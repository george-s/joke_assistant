from  JA_Classes import ArticleFeed, Draft
import sys
# Chose Feeds for Joke Assistant
bbc_feed = ArticleFeed('bbc', "bbc.png", 'http://feeds.bbci.co.uk/news/rss.xml?edition=uk')
daily_mail_feed = ArticleFeed('daily_mail', "dailymail.jpeg", 'http://www.dailymail.co.uk/news/index.rss')
fox_feed = ArticleFeed('fox', "fox.png", 'http://feeds.foxnews.com/foxnews/latest')


feeds = [bbc_feed, daily_mail_feed, fox_feed]
print "----"
for feed in feeds:
	print feed.feed_name
print "----"
print "Pick a feed"
chosenfeed = eval(str(raw_input("Please enter your choice: ")) + "_feed")


# List Of Articles Numbers So We Can Pick one
index_article_list = chosenfeed.articlesTitlesList()
	
# List Of Articles Numbers So We Can Pick one
print "Pick 5 articles by their index numbers"
indexchoices = raw_input("Please enter your choice: ")

shortlist =  chosenfeed.getArticlesFromIndex(indexchoices)
print shortlist
