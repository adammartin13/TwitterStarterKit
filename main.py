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
#   for result in results:
#     print(result)

# q = query string, max character count 500
# include_ext_edit_control = true/false, determines if tweet edit metadata is returned. Default false.
# geocode = Returns tweets of users within a specified geocode
# lang = Specify language
# result_type = mixed/recent/popular. Determines which type of result is desired.
# count = number of tweets to return
# until = YYYY-MM-DD. Returns tweets before the given date.
# since_id = Returns results with an ID more recent than that which is provided.
# max_id = Returns results with an ID older than that which is provided.

results = api.GetSearch(raw_query="q=Ukraine&result_type=recent&count=15")
for result in results:
    print(result)
