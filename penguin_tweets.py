import tweepy
from time import sleep

# Create variables for key, secret, token.

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Set up OAuth and integrate with API.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to Twitter account.

tweets = [	
'Finland - Russia - Hamburg - Netherlands - Ireland [Motion Picture Film] via @DPLA https://dp.la/item/2a7e14652a2899206e990a3c1bd49105',		
'Penguins at LAX / Mike Sergieff via @DPLA https://dp.la/item/ce5cbf8753715f38ec75324df6a5a160',		
'Emperor penguins, Antarctica ·via @DPLA https://dp.la/item/73db45fb93924587e55732e79ce8ba0a',		
'Penguins, Hagenback park. Hamburg via @DPLA https://dp.la/item/9baf7c5485e391262b2a7e0b8a9bac60',		
'Humboldt penguins · via @DPLA https://dp.la/item/ec3da428d114947cdbd642daf52c9818',		
'Antarctic penguins, a study of their social habits via @DPLA https://dp.la/item/296356a7b2206c6fd4b64fd58663d6b3',		
'Antarctic penguins; a study of their social habits via @DPLA https://dp.la/item/a9486b4c9fd38d1ecd9bc8a458b000ae',		
'Adelie penguins, McMurdo Station, Antarctica via @DPLAa https://dp.la/item/1aeeefdc7ff9a2d9f641ebcf34be7180',		
'Penguins on Dassen Island South Africa via @DPLA https://dp.la/item/57bb5e6651cbad56698b287d1143d337',	
'Penguins on an ice floe via @DPLA https://dp.la/item/b3096841e6a5727e66b435fd0ff3555a',		
'Air conditioning for the penguins via @DPLA https://dp.la/item/b8f225e598c0cc19b3418f4adac8990d',	
'Gentoo Penguins, Antarctic Peninsula via @DPLA https://dp.la/item/3df8081b482bc58323c3f0b0c3bc5dd9',		
'Penguins at the London Zoo via @DPLA https://dp.la/item/077bbfb6a5fe1d2b0238d20a4c0a3514',		
'Humboldt penguins at the zoo via @DPLA https://dp.la/item/1eeb65df664fdda72d3ce0acbf0a448d',		
'San Diego Zoo penguinsvia @DPLA https://dp.la/item/6581a65e348792298e0444dc785d3452',		
'Humboldt penguins via @DPLA https://dp.la/item/a352b3a207c30f42d4b32e739057759f',		
'Penguins in Long Beach ·via @DPLA https://dp.la/item/f59503c545d56029fe27cbb183013cbf',	
'Group Of Black-Footed Penguins via @DPLA https://dp.la/item/775b2374da9aeac86261984fc6204ebb',	
'Poems for penguins, and other lyrical lapses via @DPLA https://dp.la/item/1a0b91644869edefc2c340260cac64a3',		
'Penguins, Como Park, St. Paul via @DPLA https://dp.la/item/ad80431a384162f39f2d8bac04643437',		
'Rock Hopper Penguins Kerguelen Islands via @DPLA https://dp.la/item/4cce7713d540b72d4db6edd72918482e',	
'Penguins And Petrel · Digital Public Library of America https://dp.la/item/827d7d140216692af51e6277493e7a04',		
'King-Penguins · Digital Public Library of America https://dp.la/item/0e0e341b5730546642e54e818f1eebe5',		
'Penguins at the Bergen Aquarium via @DPLA https://dp.la/item/af071a10b1d67c017483a19de6b767f6',	
'["Penguins at Water" - Argentina] via @DPLA https://dp.la/item/92f1f3257a511bad472e7fb8d34aaa11',		
'Blank Postcard of Penguins at the Zoo via @DPLA https://dp.la/item/00223ff1d36f808f3c5fd3abe0e7e0dc',	
'The Hundreds--Tuxedo Penguinsvia @DPLA https://dp.la/item/170ee5e6ea0902e561ebe9c51ec7b70a',		
'Emperor penguins underwater, Antarctica, 1984 via @DPLA https://dp.la/item/d3dd6e7381c389a5d95d6109b05c2b0e',	
'Poems for penguins, and other lyrical lapses via @DPLA https://dp.la/item/aace25c83035096e38244ab9c32f886a',		
'Germany, penguins and bird in exhibit at Berlin Zoo via @DPLA https://dp.la/item/f54c2ee7e5dda21cdd4f1819204a88d4',		
'Olin Dows Decorative Wooden Screen with Penguins via @DPLA https://dp.la/item/cfaf09050950eb4184783086b00835d9',		
'Polar researchers photograph Adelie penguins on the ice pack via @DPLA https://dp.la/item/bdb5bbdce4509b74a004739ff660f05f',	
'Germany, penguins and bird in exhibit at Berlin Zoo via @DPLA https://dp.la/item/816762676e22fa65d72775cba3664123',		
'Amusements/Villages/Little Miracle Town/Midgets with penguins via @DPLA https://dp.la/item/e327b895b37c617b5b70ebdfe3a59142',		
'Penguins swimming. Hagenback Park. Hamburg, Germany via @DPLA https://dp.la/item/fff0d77987e76994d8b40321f5a129bf',		
'Penguins on Dassen Island, near Capetown, South Africa via @DPLA https://dp.la/item/69095d3d7a4facd20f82223a17e161e6',	
'Photos: The emperor penguins of Antarctica from space via @DPLA https://dp.la/item/47411095c86c57326782e97a6da0ccb0',		
'Cool Way West, Go Southwestern Limited to Indianapolis and St. Louis via @DPLA https://dp.la/item/600caabfa1e7b46cc6cde5d76c3e822f',		
'Penguins on an island off South African coast. via @DPLA https://dp.la/item/c1e7a78b7257f4cc14cf6c4054326270',		
'Penguins on the Palmer Peninsula, 10-11am January 28, 1963 via @DPLA https://dp.la/item/910b97405a4aa1f0e7b2a219a6e90769',		
'A pair of Adelie penguins. PHOTO from June 1984 All Hands Magazine via @DPLA https://dp.la/item/3cefb4c83a45f6cf55d4c8e4ddfbd460',		
'Penguins Playing on iPads · via @DPLA https://dp.la/item/92bf2224b6af7d5270bf12bfaa5750f0',		
'Two emperor penguins, McMurdo Ice Edge, Antarctica, 1989 via @DPLA https://dp.la/item/634eff220ad573d32b84b2559608d5e0',		
'Penguins on Dassen Island Near Cape Town, So. Africa via @DPLA https://dp.la/item/62dc9578c198606d23f8abf0b727cbaf',		
'Four emperor penguins & toy penguin McMurdo Ice Edge, Antarctica, 1989 via @DPLA https://dp.la/item/c046e7a2276eb4962a9795dc2c22da15',		
'Giant Penguins · Digital Public Library of America https://dp.la/item/b9f013d37b29850d221e50dc1e92b3c0',	
'NYWorld\'s Fair - Penguins at front door  via @DPLA https://dp.la/item/1413bf80ccbe006aca8ad4679af04aef',		
'Buffalo Zoo curator gets acquainted with Antarctic penguins via @DPLA https://dp.la/item/b7364617b1238442030721c470055813',
'Humboldt penguins · Digital Public Library of America https://dp.la/item/ec3da428d114947cdbd642daf52c9818',
'Penguins. From @nypl digital collections. http://digitalcollections.nypl.org/items/5e66b3e8-9204-d471-e040-e00a180654d7',		
'Penguins. From @nypl digital collections. http://digitalcollections.nypl.org/items/510d47e3-e872-a3d9-e040-e00a18064a99',		
'Penguins. From @nypl digital collections. http://digitalcollections.nypl.org/items/5e66b3e8-a13b-d471-e040-e00a180654d7',		
'[Penguins] · via @ DPLA https://dp.la/item/c1d3cf7943c7a0a4aba7c3dc279081c9',
'Penguins at the London Zoo via @DPLA https://dp.la/item/077bbfb6a5fe1d2b0238d20a4c0a3514',	
'Penguins on Dassen Island South Africa via @DPLA https://dp.la/item/57bb5e6651cbad56698b287d1143d337',	
'Antarctic penguins, a study of their social habits via @DPLA https://dp.la/item/296356a7b2206c6fd4b64fd58663d6b3',		
'Antarctic penguins; a study of their social habits via @DPLA https://dp.la/item/a9486b4c9fd38d1ecd9bc8a458b000a',		
'Penguins and flamingos via @DPLA https://dp.la/item/5774f09fe7b0d927861b541e0433653d',	
'Penguins in Antarctica via @DPLA https://dp.la/item/ef58411d30bdf01ae5af97f59a5164d4',		
'["Penguins" - Argentina] via @DPLA https://dp.la/item/8099ee000616801293942ad4fc5138f2',		
'Humboldt penguins via @DPLAhttps://dp.la/item/a352b3a207c30f42d4b32e739057759f',	
'University of Wash Penguin Research and Experiments in the Antarctic, n.d via @DPLA https://dp.la/item/d670b2235a490901ea7363c1b6ed5805',		
]

for tweet in tweets:
	print(tweet)
	api.update_status(status=tweet)
	
	#Tweet every three hours. 
	
	sleep(10800)
