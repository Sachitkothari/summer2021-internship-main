import JSONload
import DistanceFunction

restaurantData = JSONload.js_r('restaurants.json')
restaurantData = restaurantData['restaurants']

def nearbyRestaurants(lon,lat): #Returns a list of restraunts within 1.5km of the given coordinates
    restaurantsNear = [] #List to be returned

    for key in restaurantData:
        longit = key['location'][0]
        latit = key['location'][1]
        if(DistanceFunction.distance(lon,lat,longit,latit)<1.5):
          restaurantsNear.append(key)
    return restaurantsNear


def onlineSort(restaurantsNear: list): # Sorts nearby restaurants into online and offline
    onlineSorted = []
    offlineSorted = []
    for i in range(len(restaurantsNear)):
        if(restaurantsNear[i]['online']== True):
            onlineSorted.append(restaurantsNear[i])
        else:
            offlineSorted.append(restaurantsNear[i])

    return (onlineSorted,offlineSorted)         # Tuple of online and offline restaurants    
            

def offlineFilterer(onlineRestaurants: list,offlineRestaurants: list): # Returns only online if it has 10 or more online, returns everything back if there are less than 10 online
    if(len(onlineRestaurants)>=10):
        return (onlineRestaurants,[])      # Only online restaruants returned if 10 or more
    else:
        return (onlineRestaurants,offlineRestaurants) # Online and offline is less than 10 online restaurants