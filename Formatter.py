import TwitterApi as tw
import Youtube as yt
import billboardapi as bbd
import pandas as pd

class Formatter:
    def parseResults():

        tweets = list(tw.sorted_tweets())
        views = list(yt.sorted_songs())

        tweets_pos = 1

        for twiiter_results in tweets:
            twiiter_results.append(tweets_pos)
            tweets_pos += 1

        watch_pos = 1
        
        for youtube_results in views:
            youtube_results.append(watch_pos)
            watch_pos += 1

        song_pos = 1

        ranked_song_list = []
        for billboard_entry in bbd.billboardApi():
            song_info = billboard_entry
            pos = song_pos
            song_pos += 1
            
            for twiiter_results in tweets:
                if twiiter_results[0] == song_info:
                    twitter_score = twiiter_results[2]
                    break
           
            for youtube_results in views:
                if youtube_results[0] == song_info:
                    youtube_score = twiiter_results[6]
                    break

            ranked_song = (billboard_entry,pos,twitter_score,youtube_score)   
            ranked_song_list.append(ranked_song)
        return ranked_song_list

    def twiiterAccuracy():

        ranked_song_list = Formatter.parseResults()
        tweet_accuracy = []
        twiiter_accuracy = 1
        for song in ranked_song_list:
            if song[1] > song[2]:
                twiiter_accuracy = (len(bbd.billboardAPI()) - (song[1]-song[2]))/len(bbd.billboardAPI())
            elif song[1] < song[2]:
                twiiter_accuracy = (len(bbd.billboardAPI()) - (song[2]-song[1]))/len(bbd.billboardAPI())

            artist_and_song = song[0].split(' AND ')
            artist = artist_and_song[0]
            title = artist_and_song[1]
        
            tweet_specs = (artist,title,twiiter_accuracy)
            tweet_accuracy.append(tweet_specs)

    def youtubeAccuracy():

        ranked_song_list = Formatter.parseResults()
        views_accuracy = []
        youtube_accuracy = 1
        for song in ranked_song_list:
            if song[1] > song[3]:
                youtube_accuracy = (len(bbd.billboardAPI()) - (song[1]-song[3]))/len(bbd.billboardAPI())
            elif song[1] < song[3]:
                youtube_accuracy = (len(bbd.billboardAPI()) - (song[3]-song[1]))/len(bbd.billboardAPI())
            
            artist_and_song = song[0].split(' AND ')
            artist = artist_and_song[0]
            title = artist_and_song[1]

            views_specs = (artist,title,youtube_accuracy)
            views_accuracy.append(views_specs)

    def billboardAccuracy():

        ranked_song_list = Formatter.parseResults()
        twitter_accuracy = Formatter.twiiterAccuracy()
        youtube_accuracy = Formatter.youtubeAccuracy()
        percentage = "{:.2%}"
        song_pos = 0
        billboard_accuracy = []
        for song_entry in ranked_song_list:
            ranking_accuracy = (twitter_accuracy[song_pos][1] + youtube_accuracy[song_pos][1])/2

            artist_and_song = song_entry[0].split(' AND ')
            artist = artist_and_song[0]
            title = artist_and_song[1]

            billboard_accuracy.append(artist,title,percentage.format(twitter_accuracy[song_pos][1]),percentage.format(youtube_accuracy[song_pos][1]),percentage.format(ranking_accuracy))

    def formatAllValues():
        ranked_list = Formatter.billboardAccuracy()
        titles = ['Artist','Title','Twitter Accuracy','Youtube Accuracy','Billboard Accuracy']
        formatted_output = pd.DataFrame(ranked_list,columns=titles)
        return formatted_output

class OutputFormattedInformation:
    
    def printByBillboard():
        print(Formatter.formatAllValues())

    def printByBillboardAccuracy():
        print("Printed by Billboard Accuracy")
        ranked_by_billboard_accuracy = Formatter.formatAllValues().sort_values(by=['Billboard Accuracy'], ascending=False)
        print(ranked_by_billboard_accuracy)

    def printByTwitterAccuracy():
        print("Printed by Twiiter Accuracy")
        ranked_by_billboard_accuracy = Formatter.formatAllValues().sort_values(by=['Twitter Accuracy'], ascending=False)
        print(ranked_by_billboard_accuracy)

    def printByYoutubeAccuracy():
        print("Printed by Youtube Accuracy")
        ranked_by_billboard_accuracy = Formatter.formatAllValues().sort_values(by=['Youtube Accuracy'], ascending=False)
        print(ranked_by_billboard_accuracy)