from flask import request, render_template, redirect, url_for
from app import app
import os
import sys
from flask import send_file
sys.path.insert(1, os.path.join(os.path.expanduser('~'), 'learny', 'learny'))
from learny import learny

#import learny
@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'learnY'}
	test = {'name': 'Alex'}
	return render_template('index.html', title ='learnY', user = user, test = test)

@app.route('/file-downloads/')
def file_downloads():
	try:
		return render_template('downloads.html')
	except Exception as e:
		return str(e)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    language = request.form['language_options']
    learny.learny(text, language)
    return redirect(url_for('file_downloads'))

@app.route('/return-merged/')
def return_merged():
	try:
		return send_file(os.path.join(os.path.expanduser('~'), 'merged.docx'), attachment_filename='merged.docx', as_attachment=True)
	except Exception as e:
		return str(e)
