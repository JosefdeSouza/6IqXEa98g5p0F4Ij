import twint
#Every relevant information about tweets should be visible, such as author, date, tweet contents, number of likes, number of retweets and number of discussions.
# # Configure
# c = twint.Config()
# c.Search = "request for startup"
# c.Limit = 1
# c.Store_csv = True
# c.Output = "none"
# # Run
# twint.run.Searcj(c)

import twint

c = twint.Config()

c.Search = "request for startup"
# c.Custom["tweet"] = ["id"]
# c.Custom["user"] = ["bio"]
# c.Date = "created_at"
# c.Tweet = "tweet"
# c.Likes = "likes_count"
# c.Retweets = "retweets_count"
# c.Replies = "replies_count"
# c.Mentions = "mentions"
# c.Format = "ID {id} clear\n {tweet} \n Likes {{likes_count}, Retweets {retweets_count}, Mentions {mentions}"
c.Custom["tweet"] = ["date", "username", "tweet", "likes_count", "retweets_count", "mentions"]
c.Custom["user"] = ["bio"]
c.Limit = 1
c.Store_csv = True
c.Output = "tweets.csv"

twint.run.Search(c)