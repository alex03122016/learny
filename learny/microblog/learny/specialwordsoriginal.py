#! python3
# -*- coding: utf-8 -*-
try:
	import languageload
except ImportError:
	from learny import languageload


def nounsoriginal(inputtext, language):
	skip = False # it has to be hereque!nearly went crazy to figure it out
	nlp = languageload.language_load(language)
	docnlp = nlp(inputtext) #load to spacy
	noun_list= []
	some_nouns_token = []
	export_some_nouns = []
	#create some_nouns_token, noun_list
	for token in docnlp:
		if 'NOUN' == token.pos_:
			noun_list.append(token)# complete list of nouns
			skip = not skip #like that every second noun will be substituted
			if skip == True:
				some_nouns_token.append(token)# later for the solution box
				substitute = [] # erases contend of substitute
				for l in str(token):
					substitute.append(' _') #substitutes nouns with _
				subStr = ''.join(substitute)
				#docxprint.docx_print(printText=subStr, Paragraph=paragraph, Doc=doc)
			else:
				#docxprint.docx_print(printText=str(token) + ' ', color="red", Paragraph=paragraph, Doc=doc)
				pass
		else:
			#docxprint.docx_print(printText=str(token) + ' ', Paragraph=paragraph, Doc=doc)	#adds the text
			pass

	wordsearch_nouns = list(set([word.lemma_ for word in some_nouns_token]))#replace with lemmata, delete duplicates, make uppercase
	wordsearch_nouns_all = list(set([word.lemma_ for word in noun_list]))#replace with lemmata, delete duplicates, make uppercase
	wordsearch_nouns_extra = set(wordsearch_nouns_all) - set(wordsearch_nouns)

	#export some nouns for word search
	permitted_number_of_words = 15
	for word in wordsearch_nouns_extra:
		if len(wordsearch_nouns) == permitted_number_of_words:
			break
		elif len(wordsearch_nouns) > permitted_number_of_words:
			wordsearch_nouns = wordsearch_nouns[0:permitted_number_of_words]
			break
		elif len(wordsearch_nouns) < permitted_number_of_words:
			print("appending")
			wordsearch_nouns.append(word)

	return wordsearch_nouns

inputtext= """ Im letzten Jahr wurden in Deutschland 123 Frauen durch ihren (Ex-)Partner getötet. Das bedeutet: Alle zwei bis drei Tage stirbt eine Frau aufgrund von häuslicher Gewalt. Doch diese Zahlen sind nur die Spitze des Eisbergs. Darunter verbergen sich versuchter Mord, schwere Körperverletzung, Vergewaltigung und Misshandlung – und Mord an Frauen, bei denen nicht der (Ex-)Partner der Täter war.
Wer sich einen aktuellen Überblick über die Gewalt an Frauen und Mädchen in Deutschland verschaffen möchte, muss nur die Petition der Professorin Kristina Wolff bei change.org verfolgen: Beinahe täglich werden dort neue Fälle dokumentiert – ein düsteres Bild von frauenverachtender Gewalt, das so direkt keiner Statistik zu entnehmen ist.

"""

"""Patriarchales und diskriminierendes Gedankengut
Auch Strafverfolgung und Rechtsprechung sind von patriarchalem und diskriminierendem Gedankengut durchsetzt. Ein Beispiel dafür ist der Fall Juliet H., der gerade in Hamburg verhandelt wird. Juliet H. floh bereits 2017 aus Angst vor ihrem Ex-Partner ins Frauenhaus. Dennoch wurde sie von ihm im Dezember 2018 getötet. Die Staatsanwaltschaft erhob Anklage – nicht wegen Mordes, sondern wegen Totschlags. Die Argumentation: Weil er in der Vergangenheit bereits gewalttätig geworden sei, habe Juliet H. davon ausgehen können, dass er sie erneut angreifen würde. Somit seien die Voraussetzungen zu einer Anklage wegen Mordes nicht gegeben."""
language= "Sprache: Deutsch"

#nouns(inputtext, language)
