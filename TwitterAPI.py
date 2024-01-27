import snscrape.modules.twitter as sntwitter
import pandas as pd
import billboardapi as bbp

class Twitter:
        def getTweets(title):
                
                q = title
                # Figure out how to Billboard.get song and artist name from Adams code
                # since searching generic takes too log to compile, gonna search song name and artist tweets

                 
                # add get locations, get date blah blah from team

                since_date = '2023-03-10'
                until_date = '2023-03-28'
                #Gonna change date, depending on relavance
                
                query = f'{q} since:{since_date} until:{until_date}' 
                # took location out of query since we are searching for song name and artist name better time complilation

                # Scraping...
                tweets = sntwitter.TwitterSearchScraper(query).get_items()
                num_tweets = len(list(tweets))

                return title, num_tweets








# Sort songs
def rank_tweets(df):
    ranked_df = df.sort_values(by=['Song_Tweets'], ascending=False)
    ranked_df.reset_index(drop=True, inplace=True)
    return ranked_df

def get_sorted_tweets(songs):
    # empty list that will hold song name/artist and tweets 
    tweet_comp = []
    # Call em'  
    twitter = Twitter
    for tweet in songs:
            tweet_comp.append(twitter.getTweets(tweet))

    # Create a Pandas DataFrame from the video data
    columns = ["Song_Artist-Title","Song_Tweets"]
    df = pd.DataFrame(tweet_comp, columns=columns)
    
    # Ranks songs based on number of tweets per song
    ranked_songs = rank_tweets(df)
    return list(ranked_songs["song"])

