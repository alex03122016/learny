
try:
	import colorsyllables, clozetest, wordsearch, mergeDocxModule, PresentOrPast, specialwords, wordshuffle, infinitive, shufflesyl, specialwordsoriginal
except ImportError:
	from . import colorsyllables, clozetest, wordsearch, mergeDocxModule, PresentOrPast, specialwords, wordshuffle, infinitive, shufflesyl, specialwordsoriginal

import os
def learny(inputtext, language):

	print("input text:", inputtext, "language:", language)
	colorsyllables.color_syllables(inputtext)
	clozetest.cloze_test(inputtext, language)
	some_nouns = clozetest.cloze_test(inputtext, language)
	some_nouns = specialwords.nouns(inputtext, language)
	original_nouns = specialwordsoriginal.nounsoriginal(inputtext, language)
	wordsearch.wordsearch(some_nouns)
	PresentOrPast.present_or_past(inputtext, language)
	wordshuffle.word_shuffle(some_nouns)
	shufflesyl.syl_shuffle(original_nouns)
	infinitive.infinitive(inputtext, language)
	files = [os.path.join(os.path.expanduser('~'), 'wordsearch'+"fileTitle.docx"),
	    os.path.join(os.path.expanduser('~'), 'clozeTest'+"fileTitle.docx"),
		os.path.join(os.path.expanduser('~'), 'infinitive'+"fileTitle.docx"),
		os.path.join(os.path.expanduser('~'), 'wordshuffle'+"fileTitle.docx"),
		os.path.join(os.path.expanduser('~'), 'sylshuffle'+"fileTitle.docx"),
	    os.path.join(os.path.expanduser('~'), 'presentorpast'+"fileTitle.docx")]

	mergeDocxModule.combine_word_documents(files)


	inputtext = ""

	return
