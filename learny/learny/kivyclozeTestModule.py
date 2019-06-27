#! python3
#
#cloze test generator(all nouns): this program searches a given docx documents for nouns and substitutes them with ' _'
#
def clozeTest(inputtext, langspinner):
	import random
	import subprocess
	import os
	import spacy #code: pip install spacy
	from spacy.lang.de.examples import sentences
	import docx 	#python-docx module
	from docx.shared import RGBColor
	from docx.shared import Pt
	from learny import docxprint

	# variables and lists used
	save_path = os.path.join(os.path.expanduser('~'),'python-project' ,'kivy-test', 'learny', 'cloze-Test-' + 'fileTitle.docx')
	i = 0
	noun_list = [] # list of nouns that will be part of the cloze
	some_nouns = [] #für Rätselwörter
	export_some_nouns = []#for returning some nouns for word search
	substitute = []
	Aufgabe = {
		"Kopfzeile": "Name: 				Klasse: 				Datum:  \n ",
		"Titel": "",
		"1. Aufgabe": "Finde die Wörter aus den Lücken!\n",
		"Hinweise": "Hier sind die Wörter aus den Lücken: \n",
		"Rätselwörter": "Hier ein paar Rätselwörter aus dem Text: \n",
	}

	doc = docx.Document()# initializing python-docx
	print('-------------------GENERATE gloze test----------------------')

	skip = False # it has to be hereque!nearly went crazy to figure it out

	# load language from kivy
	lang = ""
	if langspinner == "Sprache: Deutsch":
		lang = "de_core_news_sm"
	elif langspinner == "Sprache: Englisch":
		lang = "en_core_web_sm"
	else:
		print("didnt choose language")
	nlp = spacy.load(lang)

	#load text from kivy
	rawText = inputtext
	docnlp = nlp(rawText) #load to spacy
	text = rawText.split()
	#docx_print = docxprint.docx_print(Doc=doc)

	docxprint.docx_print(printText=Aufgabe["Kopfzeile"], Doc=doc)
	docxprint.docx_print(printText=Aufgabe["1. Aufgabe"], Bold=True, Doc=doc)

	#making the cloze test
	paragraph = docxprint.docx_print(Doc=doc)
	for token in docnlp:
		if 'NOUN' in token.pos_:
			noun_list.append(token)# complete list of nouns
			skip = not skip #like that every second noun will be substituted
			if skip == True:
				some_nouns.append(token)# late for the solution box
				substitute = [] # erases contend of substitute
				for l in str(token):
					substitute.append(' _') #substitutes nouns with _
				subStr = ''.join(substitute)
				docxprint.docx_print(printText=subStr, Paragraph=paragraph, Doc=doc)
			else:
				docxprint.docx_print(printText=str(token) + ' ', color="red", Paragraph=paragraph, Doc=doc)
		else:
			docxprint.docx_print(printText=str(token) + ' ', Paragraph=paragraph, Doc=doc)	#adds the text

	docxprint.docx_print(pageBreak=True, Doc=doc)

	docxprint.docx_print(printText=Aufgabe["Hinweise"], Bold=True, Doc=doc)
	paragraph = docxprint.docx_print(Doc=doc)
	random.shuffle(some_nouns)
	for word in some_nouns:
		docxprint.docx_print(printText=str(word) + ', ', Paragraph=paragraph, Doc=doc)

	random.shuffle(some_nouns) #shuffle für Rätselwörter
	docxprint.docx_print(printText=Aufgabe["Rätselwörter"], Bold=True, Doc=doc)
	print(some_nouns)
	for word in some_nouns:
		if word == some_nouns[-1]:
			break
		word = str(word)
		shuffled = list(word)
		random.shuffle(shuffled)
		shuffled = ''.join(shuffled)
		docxprint.docx_print(printText=shuffled + ' ______________________________', Doc=doc)

	#export some nouns for word search
	for word in some_nouns:
		export_some_nouns.append(str(word))

	print('done and saving to:', save_path)
	doc.save(save_path)


	return export_some_nouns
