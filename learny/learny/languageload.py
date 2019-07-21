def language_load(language):
	import spacy #code: pip install spacy
	#load language from kivy to spacy
	lang = ""
	if language == "Sprache: Deutsch":
		lang = "de_core_news_sm"
	elif language == "Sprache: Englisch":
		lang = "en_core_web_sm"
	else:
		print(	"You didn't choose language. I will select german as language."
				+ "\n"*5)
		lang = "de_core_news_sm"
	nlp = spacy.load(lang)
	return nlp
