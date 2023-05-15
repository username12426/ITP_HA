from numpy import arccos, sin, cos
from math import radians
from copy import deepcopy

# git add .
# git commit -m "Meine Änderungen"
# git push origin master

airports = {
    "Berlin": {
        "lat": "52.365",
        "long": "13.51",
        "zielflughäfen": ["Marrakesch", "Montreal"]
    },
    "Marrakesch": {
        "lat": "31.6",
        "long": "-8.025",
        "zielflughäfen": ["Berlin", "Lima", "Montreal"]
    },
    "Montreal": {
        "lat": "45.67",
        "long": "-74.04",
        "zielflughäfen": ["Berlin", "Marrakesch", "Lima", "Ulaanbaatar"]
    },
    "Lima": {
        "lat": "12.02",
        "long": "-77.11",
        "zielflughäfen": ["Marrakesch", "Montreal"]
    },
    "Ulaanbaatar": {
        "lat": "47.85",
        "long": "106.76",
        "zielflughäfen": ["Montreal"]
    }
}

while True:
    print("expt")
    print("Possible destinations: ")
    for i, airport_name in enumerate(airports):     # iterate all possible destinations
        if i == len(airports) - 1:
            print(airport_name)     # last airport is printed in same line without comma in the end
        else:
            print(airport_name, end=", ")   # add comma to format string

    departure_airport = input("Choose departure airport: ")
    if type(departure_airport) != str and departure_airport not in airports:    # check correct input
        print("Fehler: Unbekannter Flughafen")
        break   # end script if wrong input

    zielflughaefen = deepcopy(airports[departure_airport]["zielflughäfen"])

    print("Zielflughäfen: ", end="")    # print possible destinations from starting airport
    for i, flughafen in enumerate(zielflughaefen):  # enumerate for string format
        if i == len(zielflughaefen) - 1:  # don't add comma to string of last airport
            print(flughafen)
        else:
            print(flughafen, end=", ")  # add commas between two airports

    arrival_airport = input("Choose Destination: ")
    if type(arrival_airport) != str and arrival_airport not in zielflughaefen:    # check correct input
        print("Fehler: eingegebener Flughafen existiert nicht oder wird vom Startflughafen nicht angeflogen!")
        break   # end script if wrong input

    dep_lat, dep_long = radians(float(airports[departure_airport]["lat"])), radians(float(airports[departure_airport]["long"]))
    arrival_lat, arrival_long = radians(float(airports[arrival_airport]["lat"])), radians(float(airports[arrival_airport]["long"]))

    flight_distance = 6371 * arccos(((sin(dep_lat) * sin(arrival_lat)) + (cos(dep_lat) * cos(arrival_lat)) *
                                    cos(abs(arrival_long - dep_long))))

    print(f"Distance to departure: {flight_distance:.2f}")
    break



