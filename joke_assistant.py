from  JA_Classes import ArticleFeed, ArticleShortList, Draft, Joke
import sys

# Chosen Feeds for Joke Assistant
bbc_feed = ArticleFeed('bbc', "bbc.png", 'http://feeds.bbci.co.uk/news/rss.xml?edition=uk')
daily_mail_feed = ArticleFeed('daily_mail', "dailymail.jpeg", 'http://www.dailymail.co.uk/news/index.rss')
fox_feed = ArticleFeed('fox', "fox.png", 'http://feeds.foxnews.com/foxnews/latest')



feeds = [bbc_feed, daily_mail_feed, fox_feed]
print "----"
for feed in feeds:
	print feed.feed_name
print "----"
print "Pick a feed"

#testing swap comments
#chosenfeed = eval(str(raw_input("Please enter your choice: ")) + "_feed")
chosenfeed = eval("bbc_feed")

# List Of Articles Numbers So We Can Pick one
index_article_list = chosenfeed.articlesTitlesList()
	
# List Of Articles Numbers So We Can Pick one
#print "Pick 5 articles by their index numbers"
#indexchoices = raw_input("Please enter your choice: ")
indexchoices = str("1 2 3")
shortlist = ArticleShortList("now")

shortlist.getArticlesShortListFromIndexChoice(index_article_list, indexchoices )



