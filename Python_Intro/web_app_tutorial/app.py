from flask import Flask, render_template, request
import mymodule

# declare the app to be flask object
app = Flask(__name__)

#defines what to do when someone visits the home page of web app denoted #by  '/', it will run what ever is in the function below the decorator (@..)
@app.route('/')
def home() -> 'html':
	''' This function just returns a string for fun'''
	# now we can return a page called entry 
	# make sure to make a templates directory to hold all your templates

	return render_template('entry.html', page_title='Play with Functions')

# this calls the function we made earlier called find_common_letters
@app.route('/findcommonletters', methods=['POST'])
def findcommonletters() -> 'html':
	results = mymodule.find_common_letters(request.form['sentence', request.form['letters']])
	return render_template('results.html', results_title='Common_Letters:', the_results= results)

@app.route('/countvowels', methods=['POST'])
def countvowels() -> 'html':
	results = mymodule.countvowels(request.form['sentence'])
	return render_template('results.html', results_title = 'Vowel Count', the_results = results)
	


#run the app
app.run()