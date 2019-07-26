#! python3
# -*- coding: utf-8 -*-
#cloze test maker: this program searches a given text for nouns and substitutes them with ' _'
#
def cloze_test(inputtext, language):
	import random
	import os
	import spacy #code: pip install spacy
	import docx 	#python-docx module
	try:
		import docxprint, languageload
	except ImportError:
		from learny import docxprint, languageload

	# variables and lists used
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
	save_path = docxprint.docx_print(Doc= doc, save= 'clozeTest')

	print('-------------------make cloze test----------------------')

	skip = False # it has to be hereque!nearly went crazy to figure it out

	nlp = languageload.language_load(language)
	docnlp = nlp(inputtext) #load to spacy

	docxprint.docx_print(printText=Aufgabe["Kopfzeile"], Doc=doc)
	docxprint.docx_print(printText=Aufgabe["1. Aufgabe"], Bold=True, Doc=doc)

	#making the cloze test
	paragraph = docxprint.docx_print(Doc=doc)
	for token in docnlp:
		if 'NOUN' in token.pos_:
			noun_list.append(token)# complete list of nouns
			skip = not skip #like that every second noun will be substituted
			if skip == True:
				some_nouns.append(str(token))# later for the solution box
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


	doc.save(save_path)
	return export_some_nouns
