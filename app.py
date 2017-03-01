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

	CLIENT_ACCESS_TOKEN = "d896faa13fe34c1ea714a86531f913b5"

	if request.method == 'GET':
		
		return render_template("index2.html")	

		
	elif request.method == 'POST':
		#print("inside post1")
		ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
		#print("inside post2")
		req = ai.text_request()
		#print("inside post3")
		req.query = request.form['message']
		#print("inside post4")
		res = req.getresponse()
		#print("inside post5")
		response_message = res.read()
		#print("inside post6")
		response_message = json.loads(response_message)
		#print("inside post7")
		#print("purna res : "+str(response_message) +"__________")
		#print( str(response_message["result"]['fulfillment']['speech'] ) )
		return response_message["result"]['fulfillment']['speech']


@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)
	#print("Inside webhook")
	res = {"speech": "<a href='www.google.com'>GOOGLE</a>",
			"displayText": "<a href='www.google.com'>GOOGLE</a>",
			"data": {"speech":"<a href='www.google.com'>GOOGLE</a>" }
			}
	res = json.dumps(res, indent=4)
	#print res
	r = make_response(res)
	
	r.headers['Content-Type'] = 'application/json'
	return r


if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
