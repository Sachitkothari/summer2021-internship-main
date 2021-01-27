import DateFunction
import DistanceFunction


def popularitySort(onlineRestaurants: list,offlineRestaurants: list): # Given the required 10 restaurants sorted by popularity
    sortedOnline = sorted(onlineRestaurants, key = lambda i: i['popularity'],reverse=True)
    if(len(offlineRestaurants)==0):
        return sortedOnline[:10]
    else:
        sortedOffline = sorted(offlineRestaurants, key = lambda i: i['popularity'],reverse=True)
        lengthOffline = len(sortedOffline)
        j=0
        while(len(onlineRestaurants)<10 and j<lengthOffline):
            sortedOnline.append(sortedOffline[j])
            j+=1
        return sortedOnline


def dateSort(onlineRestaurants: list,offlineRestaurants: list): # Given the required 10 restaurants sorted by date of opening
    sortedOnline = sorted(onlineRestaurants, key = lambda i: i['launch_date'],reverse=True)
    if(len(offlineRestaurants)==0):
        returnSortedOnline = []
        j=0

        while(j<10 and j<len(sortedOnline) and (DateFunction.compareMonths(sortedOnline[j]['launch_date']))<=4 ): # Loop that makes sure restaurants older than 4 months are not selected
            returnSortedOnline.append(sortedOnline[j])
            j+=1
        return returnSortedOnline
    else:
        sortedOffline = sorted(offlineRestaurants, key = lambda i: i['launch_date'],reverse=True)
        lengthOffline = len(sortedOffline)
        j=0
        while(len(onlineRestaurants)<10 and j<lengthOffline):
            sortedOnline.append(sortedOffline[j])
            j+=1
        return sortedOnline


def nearestSort(onlineRestaurants: list,offlineRestaurants: list,lon: float,lat: float): # Given the required 10 restaurants sorted by distance

    def distanceByDictionary(restaurant: dict): # Function to find distance between customer location and restaurant for sorting
         longit = restaurant['location'][0]
         latit = restaurant['location'][1]
         return DistanceFunction.distance(longit,latit,lon,lat)

   
    sortedOnline = sorted(onlineRestaurants, key=distanceByDictionary)
    if(len(offlineRestaurants)==0):
        return sortedOnline[:10]
    else:
        sortedOffline = sorted(offlineRestaurants, key=distanceByDictionary)
        lengthOffline = len(sortedOffline)
        j=0
        while(len(onlineRestaurants)<10 and j<lengthOffline):
            sortedOnline.append(sortedOffline[j])
            j+=1
        return sortedOnline
