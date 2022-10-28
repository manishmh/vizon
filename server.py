from flask import Flask, render_template, redirect, request
import os
import csv
 
# declare the Flask function in varibale app
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

# use this code to route all other pages.
@app.route('</string:page_name>')
def html_page(page_name):
 	return render_template(page_name)

# Write data into a csv file
def write_to_csv(data):
	with open('database.csv', mode='a', newline= '') as database:
		email = data['email']
		name = data['name']
		message = data['message']
		csv_writer = csv.writer(database, delimiter=' ', quotechar="'", quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,message])

# Get the data from the submit form to store into csv file
@app.route('/submit_form', methods= ["POST", "GET"])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'Something went wrong. Try again!'


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True, host='0.0.0.0', port=port)
