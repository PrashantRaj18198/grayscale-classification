#!/usr/bin/python3

import wget
import requests
import os

# If the scripts fail while downloading images continue from the last save point
try:
    f = open('lastCall.txt', 'r+')
    start = int(f.readline().strip())
    f.write('-1')
    f.close()
except FileNotFoundError:
    start = 0

# quality = 'thumb', 'small, 'regular', 'full'
quality = 'small'
# List of random objects to query for

lis = ['Flowers', 'Trees', 'Vines', 'Leaves', 'Fruits', 'Vegetables', 'Driftwood', 'Tall+Grass' , 'Fields', 'Orchard', 'Pumpkin+patch', 'Sunflower+field', 'Water', 'Rain', 'Creek', 'Waves', 'Ice', 'Snow', 'Steam', 'Rocks', 'Sand', 'Gravel', 'Soil', 'Newborn', 'Toddler', 'Child', 'Teen', 'Siblings', 'Hobby', 'Music', 'Farm', 'Sports', 'Chef', 'Tools', 'Business', 'Zoo', 'Aquarium', 'Bugs', 'Birds', 'Fish', 'festival', 'Street+photography', 'Parade', 'Sunrise', 'Midday', 'Sunset', 'Night', 'Moonlight', 'Cloudy+day', 'Stormy+day'
 ]

downloadDestination = './images/'
if not os.path.exists(downloadDestination):
    os.makedirs(downloadDestination)

n = start * 10
try:
    for counter in range(start, len(lis)):
        
        query = "grayscale+"+lis[counter]
        apiKey = "3BXDIauODJFjftLnzqUl-mI4V3afLgygr6k_FM7IZis"
        unsplashUrl = "https://api.unsplash.com/search/photos/?client_id=" + apiKey + "&query=" + query

        r = requests.get(url = unsplashUrl)
        r = r.json()

        print("\nDownloading {} pics\n".format(lis[counter]))
        for i in r["results"]:
            print("\nDownloading {}.jpg".format(n))
            wget.download(i["urls"][quality], downloadDestination+str(n)+'.jpg')
            n += 1
            

        
except:
    # An error occured so save till this point
    f = open('lastCall.txt', 'w+')
    f.write(str(counter))
    f.close()
    print("Executed till", counter)