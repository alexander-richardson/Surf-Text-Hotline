from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from scrapper import get_soup, get_report
from spots import spotsdict
from messages import formats, wrong, kook, spots


app = Flask(__name__)



@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a MMS message."""
    # Start our TwiML response
    resp = MessagingResponse()
    
    #create variable to incoming message
    body = request.values.get('Body', None)
    
    #bariable for formated message 
    inp = formats(body)


    if inp in spotsdict.keys():
        resp.message(get_report(inp))
    elif inp == 'KOOK':
        resp.message(kook)
    elif inp == 'SPOTS':
        resp.message(spots)
    else:
        resp.message(wrong)

    

    return str(resp)
    
    
if __name__ == "__main__":
    app.run(debug=True)