Intructions on use

Requirements: Flask

Steps:

Run file main.py

Open local browser and enter http://localhost:5000/discovery?lat=[lattitude here]&lon=[longitude here]

It should now show the required response

The Function to parse a json file is in JSONload.py
The function to find distance between two coordinates is in DistanceFunction.py
The functions to search for all possible restaurants and sort online and offline are in InitialConditions.py
The functions to sort into the 3 lists are in Sorts.py
main.py contains the app that is run
Run tests.py to run unit tests
testVariables.py contains the variables to check values with in unit tests
