#!/usr/bin/env python

import urllib
import json
import os
import os.path
import sys
from flask import Flask
from flask import render_template
from flask import request, url_for, make_response
import logging
import apiai


# Flask app should start in global layout
app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def main_page():

	CLIENT_ACCESS_TOKEN = "92959dbce0734a66b5da9b485e88542b"

	if request.method == 'GET':
		
		return render_template("index2.html")	

		
	elif request.method == 'POST':
		print("inside post")
		
		ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
		req = ai.text_request()
		req.query = request.form['message']
		res = req.getresponse()
		response_message = res.read()
		response_message = json.loads(response_message)
		print("purna res : "+str(response_message) +"__________")
		print( str(response_message["result"]['fulfillment']['speech'] ) )
		return response_message["result"]['fulfillment']['speech']


@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)
	print("Inside webhook")
	res = {"speech": "<a href='www.google.com'>GOOGLE</a>",
			"displayText": "GOOGLE",
			"data": {"speech":"<a href='www.google.com'>GOOGLE</a>" }
			}
	res = json.dumps(res, indent=4)
	print res
	r = make_response(res)
	
	r.headers['Content-Type'] = 'application/json'
	return r


if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
