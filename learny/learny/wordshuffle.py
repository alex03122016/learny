#! python3
# -*- coding: utf-8 -*-

import random
import docx
from . import docxprint
def word_shuffle(some_nouns):
	Aufgabe = {
		"Kopfzeile": "Name: 				Klasse: 				Datum:  \n ",
		"Titel": "",
		"1. Aufgabe": "Finde die Wörter aus den Lücken!\n",
		"Hinweise": "Hier sind die Wörter aus den Lücken: \n",
		"Rätselwörter": "Hier ein paar Rätselwörter aus dem Text: \n",
	}
	doc = docx.Document()# initializing python-docx
	save_path = docxprint.docx_print(Doc= doc, save= 'wordshuffle')
	some_nouns = list(set(some_nouns))
	#list(dict.fromkeys(some_nouns)) #erase duplicates
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

	doc.save(save_path)
