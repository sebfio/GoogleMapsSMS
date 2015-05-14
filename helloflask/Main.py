__author__ = 'Sebastian Fiorini'

from twilio.rest import TwilioRestClient
import twilio.twiml
from flask import Flask, request, redirect
direction =  __import__ ("GoogleDirections")

# put your own credentials here
ACCOUNT_SID = "AC661f3b2e9a88f232a643df46196cfec1"
AUTH_TOKEN = "cce4162f1d6ddef1bb19762b26887666"
app = Flask(__name__)
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def sendText(text):
    #from_="+13658000276",
    client.messages.create(
	    to="+19055509650",
	    from_="+14155992671",
        body=text,
    )


@app.route("/", methods=['GET', 'POST'])
def getText():
    from_number = request.values.get('From', None)
    message = "Getting Directions now!"
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    #app.run(debug=True)
    begin, stop = direction.parseText('from:Sinclair Secondary School, Whitby, ON, Canada To:Crescent School, Toronto, ON, Canada')
    dirs, dist = direction. getDirections(begin, stop)


    print ("Here are the directions!")
    for i in range(0, len(dirs)):
        print (str(int(i)+1) + ". " + dirs[i] + "  (" + dist[i] + ")")

