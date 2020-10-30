import time
from twython import Twython
import random

# Authenticate to Twitter
run = True
# Place the information from your twitter development page into these variables below. Request developer access here --> https://developer.twitter.com/en/apply-for-access
consumer_key = "uxvmTSBhgTUUAW0gKSbtmR6XZ"
consumer_secret = "KbYAjTSoGJCFugpgdhCqH5SEclS3Mo4k0Tcis6OlHxwYfDSrWB"
access_key = "1233412993-FDCUBOKmbkbx9FME04UufbxUx4ek4MgsSecWthh"
access_secret = "o4uEZEv9tXBCn0vMOaz7RXw6f0k8D8hLnaOmWHuiYtp0J"

client_args = {
    'verify': False
}

twitter = Twython(consumer_key, consumer_secret, access_key, access_secret, client_args=client_args)
hash_tag_list = ["#RecognizeArtsakh ", "#SanctionTurkey ", "#SanctionAzerbaijan ", "#TurkeyOutOfNATO "]

statement_list = ["We call on the UN office of counter-terrorism to condem the recruitment and deployment of terrorists by Azerbaijan and Turkey. ",
                  "We call on the UN general assembly to recognize the republic of Artsakh. ", "We call on the UN Security Council to stop all offensive attacks by Azerbaijan. ",
                  "We call on the UN Security Council to impose an embargo on the sale of arms to Azerbaijan. ", "We call on the UN Security Council to impose an embargo on the sale of arms to Turkey. ",
                  "We call on the UN Security Council to adopt a resolution condemning Azerbaijani and Turkish aggression against the peaceful population of Artsakh and Armenia. ",
                  "We call on the UN to provide humanitarian assistance to the peaceful population of Artsakh. ",
                  "Friendly reminder to @UN that Armenians in Artsakh voted for independence in 91, in accordance with your own 'peoples right to self-determination'. Yet u repeatedly refuse to acknowledge this because u don’t want to upset dictators & despots? ",
                  "The irony of @UN having an Office on Genocide Prevention yet remaining disturbingly silent about the real time genocide happening against Armenians is not lost on me… ",
                  "The toothless tiger that is the @UN has behaved precisely as expected. All bark & no bite, talking about human rights, peace & justice but turning a blind eye to gross atrocities & war crimes being committed by 2 member states. ",
                  "Dear @UN your legitimacy as an international body for peace and cooperation is at stake here! Condemn & #SanctionTurkey & #SanctionAzerbaijan ",
                  "The @UN must stop its sad mollycoddling of dictators Erdogan & Aliyev. Your failure to hold your member states to account RE their unrelenting campaign of aggression towards Artsakh is embarrassing at best, & disturbingly dangerous at worst. ",
                  "I know @UN is often criticised for its lack of efficacy, but this failure to condemn Turkey & Azerbaijan for their genocidal agenda against Armenians is something else! Congrats on exceeding expectations here. ",
                  "I know @UN is often criticised for its inaction generally, but this failure to condemn Turkey & Azerbaijan for their genocidal agenda against Armenians is something else! Congrats on exceeding expectations here. ",
                  "Way to go @UN your failure to unequivocally condemn Azerbaijan & Turkey for their acts of aggression against Artsakh showed all the bad actors you are as weak as they think you are #SanctionAzerbaijan #SanctionTurkey ",
                  "The @UN & international community's policy of appeasement against Turkey & Azerbaijan echoes of Hitler in WW2. Remember how that one ended? You can stop Armenians having the same fate if you #SanctionTurkey & #SanctionAzerbaijan ",
                  "The @UN does little to dispel its public image as a toothless tiger when it fails to emphatically condemn Azerbaijan’s attacks on Artsakh. The time for being an international wallflower is over. Time to #RecognizeArtsakh & #SanctionTurkey ",
                  "We call on the UNGA @UN to recognize the Republic of Artsakh as the 194th member of the United Nations #RecognizeArtsakh ",
                  "How can @UN sit on the fence about the Nagorno-Karabakh issue when Azerbaijan’s use of illegal cluster munitions targeting civilians is well-documented? We demand the UN #SanctionAzerbaijan & #RecognizeArtsakh now! ",  # https://www.hrw.org/news/2020/10/23/azerbaijan-cluster-munitions-used-nagorno-karabakh

                  "Hey @UN when are you going to draw a line in the sand & demand that 2 member states end their barbaric campaign of aggression against peaceful Armenians of Artsakh? #SanctionAzerbaijan #SanctionTurkey ",
                  "Hey @UN remember when you called for a global ceasefire due to the COVID-19 pandemic & Armenia signed but Azerbaijan didn’t? Have you woken up yet? How can you still remain silent, after the mountain of evidence of #AzeriWarCrimes? We demand you #SanctionAzerbaijan ",
                  "Hey @UN will you unequivocally condemn the acts of aggression by Azerbaijan & Turkey against Artsakh or do you want to tell the world that you are a redundant international body who only cares about human rights on paper & not in practice #SanctionTurkey #SanctionAzerbaijan ",
                  "UN Charter talks about “suppression of acts of aggression & breaches of peace” but @UN is doing quite the opposite by failing to condemn Azerbaijan & Turkey for their genocidal campaign against Artsakh & disturbing the peace of the region during a pandemic #SanctionAzerbaijan ",
                  "Remember when @UN cared about its purpose & principles? Chpt 1 of their Charter still says “All Members shall settle their international disputes by peaceful means” yet 2 of its members are proudly flouting this principle with zero consequence #SanctionTurkey #SanctionAzerbaijan ",
                  "Hey @UN nice precedent you are setting for future bad actors who decide to wage war & genocide against peaceful, vulnerable states. You know that a crime unpunished is a crime encouraged #SanctionTurkey #SanctionAzerbaijan ",
                  "The @UN does little to dispel its public image as a toothless tiger when it fails to emphatically condemn Azerbaijan’s attacks on Artsakh. The time for being an international wall flower is over. Time to #RecognizeArtsakh & #SanctionAzerbaijan "
                  ]

at_list = ['@UN ', '@UNDPPA ', '@hrw ', '@antonioguterres ', '@UN_PGA ', '@UN_Valovaya ', '@UN_Spokesperson ', '@UN_HRC ',
           '@UNOCHA ', '@UN_Vienna ', '@UN_OCT ', '@GermanyUn ', '@RichardGowan1 ', '@SCRtweets ', '@Refugees ',
           '@AminaJMohammed ']
# twitter.update_status(status='I posted this with #Python!')
while run:
    try:
        # Randomly selects statements and hash tags from the lists defined above
        statement = random.choice(statement_list)
        hash_tag_a = random.choice(hash_tag_list)
        hash_tag_b = random.choice(hash_tag_list)
        at_1 = random.choice(at_list)
        at_2 = random.choice(at_list)
        # Makes sure the hash tags randomly selected are not the same
        if hash_tag_a == hash_tag_b:
            hash_tag_b = random.choice(hash_tag_list)
        time.sleep(900) # 5 minutes in seconds
        tweet = statement + at_1 + at_2 # + hash_tag_a + hash_tag_b
        print(tweet)
        twitter.update_status(status=tweet)

    except Exception as e:
        run = False
        print(e)

# "The chair of the Cluster Munitions Coalition, in reference to Azerbaijan, stated “The continued use of cluster munitions – particularly in populated areas – shows flagrant disregard for the safety of civilians” @UN it’s time to #SanctionAzerbaijan now! https://www.hrw.org/news/2020/10/23/azerbaijan-cluster-munitions-used-nagorno-karabakh ",
# "Stop perpetuating the false equivalence narrative @UN & note @hrw made repeated requests to the Azerbaijani govt for access to conduct investigations, which were denied. While Artsakh welcomed them into Stepanakert to examine remnants of exploded munitions #SanctionAzerbaijan ",
# "How does @UN reconcile its own Convention on the Prevention & Punishment of the Crime of Genocide with Genocide Watch’s latest declaration of Genocide Emergency due to Azerbaijan’s aggression against Artsakh? #RecognizeArtsakh #SanctionAzerbaijan https://www.genocidewatch.com/single-post/genocide-emergency-azerbaijan-s-attack-in-artsakh ",
# "Not a good look when your own member state is designated at being at Stage 9 (extermination) & Stage 10 (denial) of the Genocidal Process & you are silent about it @UN you must unequivocally condemn this genocide & #SanctionAzerbaijan #RecognizeArtsakh https://www.genocidewatch.com/single-post/genocide-emergency-azerbaijan-s-attack-in-artsakh ",
# "How embarrassing to be the very Org that was established to prevent another Holocaust yet remain completely silent about a genocide being enacted against Armenians! @UN you must do better, condemn this genocide & #SanctionAzerbaijan #RecognizeArtsakh https://www.genocidewatch.com/single-post/genocide-emergency-azerbaijan-s-attack-in-artsakh ",
# "Azerbaijan’s use of prohibited weapons like cluster munitions against Armenians has been documented by various reports & human rights groups. @UN when will you step up & condemn these barbaric acts by Azerbaijan? #SanctionAzerbaijan #RecognizeArtsakh https://www.amnesty.org/en/latest/news/2020/10/armenia-azerbaijan-civilians-must-be-protected-from-use-of-banned-cluster-bombs/ ",



