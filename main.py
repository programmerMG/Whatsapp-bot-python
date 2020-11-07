from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

dictionary=PyDictionary()

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    #msg is the message sent by user

    
    resp = MessagingResponse()
    
    resp.message(f"You said {msg}")
    #this sends a message to the user

    
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
