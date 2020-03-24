#!/usr/bin/python3

import wget
import requests
import os

try:
    f = open('lastCall.txt')
    start = int(f.readline().strip()) + 1
    f.close()
except FileNotFoundError:
    start = 0

imageUrls = []
lis = ['Flowers', 'Trees', 'Vines', 'Leaves', 'Fruits', 'Vegetables', 'Driftwood', 'Tall+Grass' , 'Fields', 'Orchard', 'Pumpkin+patch', 'Sunflower+field', 'Water', 'Rain', 'Creek', 'Waves', 'Ice', 'Snow', 'Steam', 'Rocks', 'Sand', 'Gravel', 'Soil', 'Newborn', 'Toddler', 'Child', 'Teen', 'Siblings', 'Hobby', 'Music', 'Farm', 'Sports', 'Chef', 'Tools', 'Business', 'Zoo', 'Aquarium', 'Bugs', 'Birds', 'Fish', 'festival', 'Street+photography', 'Parade', 'Sunrise', 'Midday', 'Sunset', 'Night', 'Moonlight', 'Cloudy+day', 'Stormy+day'
 ]

downloadDestination = './images/'
if not os.path.exists(downloadDestination):
    os.makedirs(downloadDestination)

n = 0
try:
    for counter in range(start, len(lis)):
        query = "grayscale+"+lis[counter]
        apiKey = "3BXDIauODJFjftLnzqUl-mI4V3afLgygr6k_FM7IZis"
        unsplashUrl = "https://api.unsplash.com/search/photos/?client_id=" + apiKey + "&query=" + query

        r = requests.get(url = unsplashUrl)
        r = r.json()

        # print(r["results"][0]["urls"][""])
        print("Downloading {} pics".format(lis[counter]))
        for i in r["results"]:
            print("\nDownloading {}.jpg".format(n))
            wget.download(i["urls"]["regular"], downloadDestination+str(n)+'.jpg')
            n += 1
            # imageUrls.append(i["urls"]["small"])

        print(imageUrls)
        # localImage = wget.download(imageUrl)  
except:
    # An error occured so save till this point
    f = open('lastCall.txt', 'w+')
    f.write(str(counter))
    f.close()
    print("Executed till")