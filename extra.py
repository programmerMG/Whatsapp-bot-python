'''

This doesn't contain commands that starter should start right now.
I would nor suggest that starter should go for it.
Those who know how to work with this can use just install the extra modules needed in it
'''
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import wikipedia
from googlesearch import search 
import random
from PyDictionary import PyDictionary
from time import sleep

dictionary=PyDictionary()

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    
    # Create reply
    if msg[:4]=='wiki':
        try:
            result = wikipedia.summary(msg[4:], sentences = 2)
        except Exception:
            result='there is some error in the command\ntry some other query'
    elif msg[:6]=='google':
        try:
            for j in search(msg[6:], tld="co.in", num=1, stop=1, pause=2):
                result=str(j)
        except Exception:
            result='there is some error in the command\ntry some other query'
    elif msg[:3]=='ask':
        choices=['yes','maybe','no']
        try:
            result=random.choice(choices)
        except Exception:
            result='there is some error in the command\nuse it properly'
    elif msg=='your commands':
        result='wiki <query> \ngoogle <query>\nask <questions> (results in yes/maybe/no)\nmeaning <word>\nsynonym <word>\nantonym <word>'
    
    elif msg=='hello':
        result='hello human'
    elif msg[:7]=='meaning':
        try:
            means=dictionary.meaning(msg[8:])
            result=''
            for x in means:
                result+=str(x)+':'+str(means[x])+'\n \n'              
        except Exception:
            result='No results found'
    elif msg[:7]=='synonym':
        try:
            result=''
            for i in dictionary.synonym(msg[8:]):
                result+=str(i)+'\n'
        except Exception:
            result='No results found'
    elif msg[:7]=='antonym':
        try:
            result=''
            for i in dictionary.antonym(msg[8:]):
                result+=i+'\n'
        except Exception:
            result='No results found'        
    else:
        result='no command like that\ntype your commands for using me'
        
    resp = MessagingResponse()
    resp.message(result)

    
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
