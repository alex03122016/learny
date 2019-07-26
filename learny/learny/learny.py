
try:
	import colorsyllables, clozetest, wordsearch, mergeDocxModule, PresentOrPast, specialwords, wordshuffle, infinitive
except ImportError:
	from . import colorsyllables, clozetest, wordsearch, mergeDocxModule, PresentOrPast, specialwords, wordshuffle, infinitive

import os
def learny(inputtext, language):

	print("input text:", inputtext, "language:", language)
	colorsyllables.color_syllables(inputtext)
	clozetest.cloze_test(inputtext, language)
	some_nouns = clozetest.cloze_test(inputtext, language)
	some_nouns = specialwords.nouns(inputtext, language)
	#wordsearch.wordsearch(some_nouns)
	PresentOrPast.present_or_past(inputtext, language)
	#wordshuffle.word_shuffle(some_nouns)
	infinitive.infinitive(inputtext, language)
	files = [os.path.join(os.path.expanduser('~'), "learny", "learny", 'wordsearch'+"fileTitle.docx"),
	    os.path.join(os.path.expanduser('~'), "learny", "learny", 'clozeTest'+"fileTitle.docx"),
	    os.path.join(os.path.expanduser('~'), "learny", "learny", 'presentorpast'+"fileTitle.docx")]

	mergeDocxModule.combine_word_documents(files)


	inputtext = ""

	return
