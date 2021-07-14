#! python3
# -*- coding: utf-8 -*-

import random
import spacy #code: pip install spacy
from textblob_de import TextBlobDE
from textblob_de.lemmatizers import PatternParserLemmatizer
import docx 	#python-docx module
try:
	import docxprint, languageload
except ImportError:
	from learny import docxprint, languageload


def word_translate(inputtext, language):
	Aufgabe = {
		"Kopfzeile": "Name: 				Klasse: 				Datum:  \n ",
		"Titel": "",
		"1. Aufgabe": "Übersetze!\n",
		"Hinweise": "Hier ist die Wortliste: \n",
		"Rätselwörter": "Hier ein paar Rätselwörter aus dem Text: \n",
	}
	doc = docx.Document()# initializing python-docx
	save_path = docxprint.docx_print(Doc= doc, save= 'word-translate')

	docxprint.docx_print(printText=Aufgabe["Kopfzeile"], Bold=True, Doc=doc)
	docxprint.docx_print(printText=Aufgabe["1. Aufgabe"], Bold=True, Doc=doc)

	nlp = languageload.language_load(language)
	docnlp = nlp(inputtext) #load to spacy

	#prepare to control, only unsorted and unfiltered
	inputtext_prepared = []
	for token in docnlp:
		if str(token).isalpha() == True:
			inputtext_prepared.append(str(token))
	inputtext_prepared = " \n ".join(inputtext_prepared)

	print(inputtext_prepared)
	blob = TextBlobDE(inputtext_prepared)
	translation = blob.translate(from_lang= 'en',to="de")# bg - bulgarisch, de - deutsch, en - englisch
	print(translation)

	wordlist_translated	= translation.split("\n")
	inputtext_prepared = inputtext_prepared.split("\n")

	print(len(inputtext_prepared), len(wordlist_translated))
	print(inputtext_prepared)
	print(wordlist_translated)

	result = []
	for i in range(len(wordlist_translated)):
		result.append(inputtext_prepared[i].lower() + "\t-" + wordlist_translated[i])
	result = list(set(result))
	result.sort()

	docxprint.docx_print(printText=inputtext , Doc=doc)
	docxprint.docx_print(printText=Aufgabe["Hinweise"], Bold=True, Doc=doc)

	for translation in result:
		print(translation)
		docxprint.docx_print(printText=translation , Doc=doc)
	doc.save(save_path)

text="""Hi, is it your job to do the dishes too?
Yes, it is. I do the same job every day.
I'm Jenny. Who are you?
I‘m Kevin.
Are you on a school trip  here in Cornwall?
No, I'm not. I'm on holiday with my family. And you?
I'm on a school trip. We don't have holidays in Bonn now.
You're from Bonn ?
Yes, I am. Why is that funny?
 """

word_translate(inputtext=text, language= "Sprache: Englisch")
