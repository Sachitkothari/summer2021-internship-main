from flask import Flask,request
import json
import JSONload
import DistanceFunction
import Sorts
import InitialConditions

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/discovery',methods=['GET'])


def discovery():
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))
    
    RestaurantsNear = InitialConditions.nearbyRestaurants(lon,lat)  #Finds restaurants within 1.5km
    onlineOfflineSorted = InitialConditions.onlineSort(RestaurantsNear) #Sorts into online and offline
    onlineOfflineSorted = InitialConditions.offlineFilterer(onlineOfflineSorted[0],onlineOfflineSorted[1]) #Removes offline if 10 or more online


    Popularity = (Sorts.popularitySort(onlineOfflineSorted[0],onlineOfflineSorted[1]))   #Popularity sorted
    Date = (Sorts.dateSort(onlineOfflineSorted[0],onlineOfflineSorted[1]))               #Date sorted
    Nearest = (Sorts.nearestSort(onlineOfflineSorted[0],onlineOfflineSorted[1],lon,lat)) #Nearest sorted
    
    listOfSorts = [Popularity, Date, Nearest]                               #List of lists of the final results to be displayed
    titles = ["Popular Restaurants", "New Restaurants", "Nearby Restaurants"]  

    result = {'sections': []} #result to be returned
    
    for i in range(3): 
        
        if len(listOfSorts[i] )> 0: #Makes sure empty lists are not added
            
            result['sections'].append({'title': titles[i], 'restaurants': listOfSorts[i]}) #Appends non empty list
       
    
    return json.dumps(result) #returns result
    
    
app.run() #Runs app

