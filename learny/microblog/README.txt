learnY
===============================================================================
Learny returns worksheets for learning. ﻿Learny uses the wordmaterial of your
text input. It is aimed at people who have problems with basic aspects of the
language and therefore difficulties to anderstand texts.

source code and usage docs: https://github.com/alex03122016/learny

Installation
-------------------------------------------------------------------------------
set up flask server in Linux

$ git clone https://github.com/alex03122016/learny
$ virtualenv -p /usr/bin/python3.6 flask_venv
$ pip install -r /home/alex/learny/learny/microblog/requirements-flask.txt
$ python -m spacy download de_core_news_sm
$ Source flask_venv/bin/activate
$ cd learny
$ cd microblog
$ flask run –host=0.0.0.0

for pyhyphen maybe needs to be installed on ubuntu 20.04
sudo apt-get install build-essential python-dev

Usage
-------------------------------------------------------------------------------

You can enter a small text (200 words) into the textbox. After that you can
click on "submit" - Button. Finally you have to click on "Download" - Button.

Example input text in german:
"Die ersten bekannten Ritter gab es schon im Römischen Reich, noch vor Christi
Geburt. Jedoch waren sie noch nicht das, was wir heute unter einem Ritter
verstehen. Der Begriff "Ritter" lässt sich aus dem mitteldeutschen Wort
"riddare" ableiten, welches so viel wie "Reiter" bedeutet.

Auch der Name "Eques", der einen römischen Ritter bezeichnet, hat die gleiche
Bedeutung: Das lateinische Wort "eques" heißt wörtlich Reiter, das Wort "equus"
 bedeutet Pferd. Unter einem Ritter stellt man sich also im Allgemeinen einen
 adeligen Krieger auf einem edlen Ross vor - schwer gerüstet und mit Lanze
 bewaffnet."

Index of the output docx file
-------------------------------------------------------------------------------

page 1: 	- It hides nouns in a wordsearch.
					- competence: spelling
page 3: 	- It hides nouns in a cloze test. It substitutes every letter with an
						underscore symbol "_".
					- competence: spelling, context of use
page 8: 	- It gives you verbs in infinite form and finit form. You have to bring
						them together.
					- competence:  verb conjugation, infinitive
page 9:		- It changes the order letters of nouns.
					- competence: spelling
page 10: 	- It changes the order of hyphens of nouns.
					- competence spelling, word separation,
page 11: 	- It gives you verbs in first person present tense and first person past
						tense
					- competence:  verb conjugation, tense

Known bugs
-------------------------------------------------------------------------------
If you have words that are larger than 20 letters there might result an internal
server error due to problems with the wordsearch.

Authors
-------------------------------------------------------------------------------
Alexander Tanck

License
-------------------------------------------------------------------------------
GPLv3
