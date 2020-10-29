import time
from twython import Twython
import random

# Authenticate to Twitter
run = True
# Place the information from your twitter development page into these variables below. Request developer access here --> https://developer.twitter.com/en/apply-for-access
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

client_args = {
    'verify': False
}

twitter = Twython(consumer_key, consumer_secret, access_key, access_secret, client_args=client_args)
hash_tag_list = ["#RecognizeArtsakh ", "#SanctionTurkey ", "#SanctionAzerbaijan ", "#TurkeyOutOfNATO "]
statement_list = ["We call on the UN office of counter-terrorism to condem the recruitment and deployment of terrorists by Azerbaijan and Turkey. ",
                  "We call on the UN general assembly to recognize the republic of Artsakh. ", "We call on the UN Security Council to stop all offensive attacks by Azerbaijan. ",
                  "We call on the UN Security Council to impose an embargo on the sale of arms to Azerbaijan. ", "We call on the UN Security Council to impose an embargo on the sale of arms to Turkey. ",
                  "We call on the UN Security Council to adopt a resolution condemning Azerbaijani and Turkish aggression against the peaceful population of Artsakh and Armenia. ",
                  "We call on the UN to provide humanitarian assistance to the peaceful population of Artsakh. "]
# twitter.update_status(status='I posted this with #Python!')
while run:
    try:
        # Randomly selects statements and hash tags from the lists defined above
        statement = random.choice(statement_list)
        hash_tag_a = random.choice(hash_tag_list)
        hash_tag_b = random.choice(hash_tag_list)
        # Makes sure the hash tags randomly selected are not the same
        if hash_tag_a == hash_tag_b:
            hash_tag_b = random.choice(hash_tag_list)
        time.sleep(900) # 15 minutes in seconds
        twitter.update_status(status=statement + hash_tag_a + hash_tag_b)
    except Exception as e:
        run = False
        print(e)






# class listener(StreamListener):
#     def on_data(self, data):
#         print(data)
#         return True
#
#     def on_error(self, status):
#         print(status)
#         return False
#
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth_url = auth.get_authorization_url(signin_with_twitter=True)
# auth.set_access_token(access_key, access_secret)
# api = tweepy.API(auth).update_status('whats up')
# api.update_status("Test tweet from Tweepy Python")
# twitterStream = Stream(auth, listener())
# twitterStream.filter(track=["Armenia"])



