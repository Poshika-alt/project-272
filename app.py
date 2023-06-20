# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
	username = request.form['username']
	password = request.form['password']
	mobile_number = request.form['number']

	if username == 'verify' and password == '12345':   
		account_sid = 'AC2f041f6dd5e9ca1cd3241b051118866a'
		auth_token = 'a018ffa3d3a6b505a38590942869cdb9'
		client = Client(account_sid, auth_token)

		verification = client.verify \
			.services('ISf29ee6814c2be66091a564dc6e2371fe') \
			.verifications \
			.create(to=mobile_number, channel='sms')

		print(verification.status)
		return render_template('otp_verify.html')
	else:
		return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
	print('processing')

	received_otp = request.form['received_otp']
	mobile_number = request.form['number']

	account_sid = 'AC2f041f6dd5e9ca1cd3241b051118866a'
	auth_token = 'a018ffa3d3a6b505a38590942869cdb9'
	client = Client(account_sid, auth_token)
											
	verification_check = client.verify \
		.services('ISf29ee6814c2be66091a564dc6e2371fe') \
		.verification_checks \
		.create(to=mobile_number, code=received_otp)
	print(verification_check.status)

	if verification_check.status == "pending":
		return render_template('otp_error.html')    # Write code here
	else:
		return redirect("http://localhost:5001/")


if __name__ == "__main__":
	app.run()

