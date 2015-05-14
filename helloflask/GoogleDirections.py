__author__ = 'Sebastian Fiorini'
from googlemaps import Client

"""Receives a starting location or an ending location and returns a list of steps based on the
    google map api
"""
def getDirections(start = "Sinclair Secondary School, Whitby, Ontario, Canada", end = "University of Windsor, Windsor, Ontario, Canada"):
    gmaps = Client(key = 'AIzaSyDYYj3lEniXBaV0wQCO4tnkkXl_OnxrdE0')
    dirs = gmaps.directions(start, end, units = 'metric', mode = "driving")
    #print (dirs)
    directions = []
    distance = []
    for step in dirs:
        if type(step) is dict:
            for i in step:
                if type(step[i] is list):
                    try:
                        for stepNumber in step[i]:
                            if (type(stepNumber) is dict):
                                for key in stepNumber:
                                    if key == "steps":
                                        for stepInstruction in stepNumber["steps"]:
                                            directions.append(stepInstruction.get("html_instructions"))
                                            distance.append(stepInstruction.get("distance").get("text"))
                    except: Exception

    for i in range(0, len(directions)):
        directions[i] = directions[i].replace("<b>", "")
        directions[i] = directions[i].replace("</b>", "")
        directions[i] = directions[i].replace('<div style=\"font-size:0.9em">', " [")
        directions[i] = directions[i].replace("</div>", "] ")
    return directions, distance

"""receives a string as a text with the form
        "From: starting location To: Ending Location"
    and returns a starting point and an ending point pulled out from the text"""
def parseText(text):
    parts =  text.split(":")
    parts[1] = parts[1] [:-3]
    return parts[1], parts[2]


getDirections()