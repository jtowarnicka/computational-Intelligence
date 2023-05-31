import snscrape.modules.twitter as sntwitter
import nest_asyncio
import pandas as pd
import datetime

nest_asyncio.apply()

TWEETS_PER_DAY = 200
tweets = []

start_date = datetime.datetime(2022, 8, 1)
end_date = datetime.datetime(2022, 10, 1)
# start_date = datetime.datetime(2022, 10, 1)
# end_date = datetime.datetime(2023, 1, 1)
# start_date = datetime.datetime(2023, 1, 1)
# end_date = datetime.datetime(2023, 6, 1)
current_date = start_date

while current_date.date() != end_date.date():
    tweets_per_day = 0
    for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(
            f"kanye west lang:en until:{(current_date + datetime.timedelta(days=1)).strftime('%Y-%m-%d')} since:{current_date.strftime('%Y-%m-%d')}"
        ).get_items()
    ):
        tweets.append([tweet.date, tweet.content])
        print(f"Tweet {len(tweets)} added")

        tweets_per_day += 1
        if tweets_per_day >= TWEETS_PER_DAY:
            break

    current_date += datetime.timedelta(days=1)

df = pd.DataFrame(tweets, columns=["Date", "Content"])
df.to_csv("tweets_before.csv", index=False)

print("Data saved to .csv file")
