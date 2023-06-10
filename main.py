import twitter
api = twitter.Api(consumer_key='dB5olcSqt4kFs8PWBOjewSeHH',
                  consumer_secret='ANXUAZdWwIZ52227d39d5fjZGopQ46XwWGehG0MQsmefRa2Xpq',
                  access_token_key='756634151642595329-lytDEE7J08OSWlsbWbS7IQpnQbqaAQi',
                  access_token_secret='bl1Fb549QrXVhjlBkCI9EtPixdeLEnPzwBJpP8unaKJyr')

# GET rate limit for basic accounts is 15 per 15 minutes
# A Tweet ID is the string of numbers at the end of a tweet URL

# How to get searches
# api.GetSearch(query="q=") where q is the query
# Commands are '&' separated. Order doesn't matter but q text must come first.
# Example: 15 latest tweets containing 'Ukraine':
#   results = api.GetSearch(raw_query="q=Ukraine&result_type=recent&count=15")
#   for tweet in results:
#     print(tweet.text+'\n') # tweet.text prints just the tweet text

# q = query string, max character count 500
# include_ext_edit_control = true/false, determines if tweet edit metadata is returned. Default false.
# geocode = Returns tweets of users within a specified geocode
# lang = Specify language
# result_type = mixed/recent/popular. Determines which type of result is desired.
# count = number of tweets to return
# until = YYYY-MM-DD. Returns tweets before the given date.
# since_id = Returns results with an ID more recent than that which is provided.
# max_id = Returns results with an ID older than that which is provided.
'''
results = api.GetSearch(raw_query="q=Ukraine&result_type=recent&count=15")
for tweet in results:
    print(tweet.text+'\n')
'''

# Logical searches
# Advanced operators are available to accounts with Academic Research access
# Searching for results with 'Ukraine' AND 'Refugee' is default via space-separated variables
'''
results = api.GetSearch(raw_query="q=Ukraine refugee&result_type=recent&count=15")
for tweet in results:
    print(tweet.text+'\n')
'''
# Searching for results with 'Ukraine' OR 'Poland' is done via the 'OR' operator
'''
results = api.GetSearch(raw_query="q=Ukraine OR Poland&result_type=recent&count=15")
for tweet in results:
    print(tweet.text+'\n')
'''
# Searching for results with 'Ukraine' AND NOT 'war' is done via the negation '-' operator
'''
results = api.GetSearch(raw_query="q=Ukraine -war&result_type=recent&count=15")
for tweet in results:
    print(tweet.text+'\n')
'''
# Search logic can be grouped with parenthesis: 'Ukraine' AND 'war' but NOT 'Poland' and 'war'
# DOES NOT WORK, returns error 32. Not sure why, will fix if needed.
'''
results = api.GetSearch(raw_query="q=(Ukraine war) OR (Poland -war)&result_type=recent&count=15")
for tweet in results:
    print('tweet:\n\t'+tweet.text+'\n')
'''

# Filter searches
# Filter retweets

results = api.GetSearch(raw_query='q=Ukraine&result_type=recent&count=5')
for tweet in results:
    print('tweet:\n\t' + tweet.text + '\n')
