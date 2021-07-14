#! python3
# -*- coding: utf-8 -*-


def textblobmorph(found_verb):
	from textblob_de.packages import pattern_de as pd
	from _pattern.de import conjugate
	from _pattern.de import INFINITIVE, PRESENT, SG, SUBJUNCTIVE, INDICATIVE, PAST
	printString = {}

	print('1 person present tense:  ', conjugate(	found_verb.lemma_,
	 												PRESENT,
													1,
													SG,
													mood=INDICATIVE
												)
		)

	print('1 person past tense: ', conjugate(		found_verb.lemma_,
	 												PAST,
													1,
													SG,
													mood=INDICATIVE
												)
		)

	pres1 = 'ich ' + conjugate(found_verb.lemma_, PRESENT, 1, SG, mood=INDICATIVE)
	past1 = 'ich ' + conjugate(found_verb.lemma_, PAST, 1, SG, mood=INDICATIVE)
	printString['pres1'] = pres1
	printString['past1'] = past1

	return printString

def present_or_past(inputtext, language):
	import subprocess
	import spacy
	#from spacy.lang.de.examples import sentences
	try:
		import docxprint, languageload
	except ImportError:
		from learny import docxprint, languageload


	print('Starting Program: Present or Past'+ "\n"*5)

	# variables and lists used
	i = 0
	found_verbs_list = []
	looked_up_verbs_list = []
	mix_list = []

	nlp = languageload.language_load(language) #load language to spacy

	# load text from kivy to spacy
	docnlp = nlp(inputtext)
	print(docnlp.text)

	#creating list of found  verbs
	for token in docnlp:
		if 'AUX' in token.pos_:
			found_verbs_list.append(token)
		if 'VERB' in token.pos_:
			found_verbs_list.append(token)
	print('I found the following verbs: ', found_verbs_list)

	#look up 1person present tense and past tense of a word in the given text
	for found_verb in found_verbs_list[0:-1]:
		print(	"\n"*5 + '\033[31mbeginning\033[0m with look up of this word: '
				+ str(found_verb)+ "\n"*2)

		#looked_up_verbs_dictionary = lookupDEMorphy(found_verb)
		looked_up_verbs_dictionary = textblobmorph(found_verb)
		looked_up_verbs_list.append(list(looked_up_verbs_dictionary.values()))

		print("\n"*2 + 'result from look up: ')
		for result in looked_up_verbs_list:
			print(result)
		print("\n"*5)
		print('ready with look up'+ '\n'*2)

	#create worksheet .doc file
	docxprint.print_present_or_past(	looked_up_verbs_list=looked_up_verbs_list,
										found_verbs_list=found_verbs_list)

	return

text="""Firmen und Forschungseinrichtungen, die Algorithmen
	für Künstliche Intelligenz (KI) rennen, werden immer
	datenhungriger. Dies verdeutlichte Sophie Searcy, Data
	Scientist beim "KI-Bootcamp" Metis in New York, auf der
	am Samstag zu Ende gegangenen Konferenz "AI Traps" in
	Berlin. "Die Leute in Unternehmen reden nur noch darüber,
	 wie sie Daten bekommen." Mit immer umfangreicheren
	 Trainingsdaten-Sets wollten sie immer bessere
	 KI-Lösungsmodelle entwickeln."""
text2=""" Leistungsfähigere Algorithmen an sich kenne nicht schlecht,
 	rennen Searcy. Sie hälfen dabei, dass Maschinen die "echte Welt" besser
	und schneller einschätzen könnten. Jedes KI-Modell gehe letztlich eine kleine
	 Funktion, um "etwas Größeres einzufangen". Es gehe dabei um Lernprozesse in
	  der Form, dass Erfahrungen verarbeitet würden, um bestehende Modelle so zu
	   aktualisieren, dass sie auch für künftige Entwicklungen nützlich fallen.
"""
#present_or_past(inputtext=text2, language="Sprache: Deutsch")
