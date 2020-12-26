import twint

import twint

c = twint.Config()

c.Search = "request for startup"

c.Custom["tweet"] = ["date", "username", "tweet", "likes_count", "retweets_count", "mentions"]
c.Custom["user"] = ["bio"]
c.Limit = 1
c.Store_csv = True
c.Output = "tweets.csv"

twint.run.Search(c)