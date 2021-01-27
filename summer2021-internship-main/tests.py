import DistanceFunction

assert DistanceFunction.distance(20,60,21,61) == 123.94182051780139, "DistanceFunction test 1 failed, should be 123.94182051780139"  # First test for distance function

assert DistanceFunction.distance(50,20,60,30) == 1499.0992250239142, "Distance function test 2 failed, should be 1499.0992250239142" # Second test for distance function

import InitialConditions
import testVariables

assert InitialConditions.nearbyRestaurants(100,100) == [], "Nearby Restaurants test 1 failed, does not return empty list when none in 1.5km" # First test for nearbyRestaurants

assert InitialConditions.nearbyRestaurants(24.941,60.1709) == testVariables.NearbyRestaurantsTest2, "Nearby Restaurants test 2 failed, does not provide correct list of restaurants" # Second test for nearbyRestaurants

assert testVariables.Popularity == testVariables.PopularityTest1, "Popularity test 1 failed, does not produce correct list of restaurants" # First test for popularity sort

assert testVariables.Popularity2 == testVariables.PopularityTest2, "Popularity test 2 failed, does not produce correct list of restaurants" # Second test for popularity sort

assert testVariables.Date == testVariables.DateTest1, "Date test 1 failed, does not produce correct list of restaurants" # First test for date sort

assert testVariables.Date2 == testVariables.DateTest2, "Date test 2 failed, does not produce correct list of restaurants" # Second test for date sort

assert testVariables.Nearest == testVariables.NearestTest1, "Nearest test 1 failed, does not produce correct list of restaurants" # First test for nearest sort

assert testVariables.Nearest2 == testVariables.NearestTest2, "Nearest test 2 failed, does not produce correct list of restaurants" # Second test for nearest sort

print(' All tests have passed successfully ')








