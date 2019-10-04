



def prepare_search(inputtext, language):
	import spacy #code: pip install spacy
	try:
		import languageload
	except ImportError:
		from learny import languageload

	# variables and lists used
	noun_list = [] # list of nouns that will be part of the cloze

	nlp = languageload.language_load(language)
	docnlp = nlp(inputtext) #load to spacy

	for token in docnlp:
		if 'NOUN' in token.pos_:
			noun_list.append(str(token.lemma_))# complete list of nouns
	return noun_list

def get_categories(searchquery="", resultDict={}):

	import wptools
	#https://github.com/siznax/wptools/wiki/Examples#get-a-representative-image
	import requests
	import os
	import spacy #code: pip install spacy
	try:
		import languageload
	except ImportError:
		from learny import languageload
	nlp = languageload.language_load(language="")

	#https://github.com/siznax/wptools/wiki/Examples#get-wikidata
	page = wptools.page(searchquery, lang="de")
	number = page.get_wikidata()
	givenid = page.data['wikibase']
	print("id:", givenid)


	#https://towardsdatascience.com/where-do-mayors-come-from-querying-wikidata-with-python-and-sparql-91f3c0af22e2
	url = 'https://query.wikidata.org/sparql'
	query = f"""
	SELECT ?item ?itemLabel
	WHERE
	{{
	  wd:{givenid} wdt:P279/wdt:P31* ?item.
	  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de". }}
	}}

	"""
	file_path  = os.path.join(os.path.expanduser('~'),'learny', 'learny', 'learny', 'b1.txt')

	with open(file_path) as f:
	  grundwortschatz = f.readlines()
	resultDict[searchquery] = []
	grundwortschatz = " ".join(grundwortschatz)
	#https://www.datacamp.com/community/tutorials/f-string-formatting-in-python
	r = requests.get(url, params = {'format': 'json', 'query': query})
	data = r.json()
	for i in range(len(data["results"]["bindings"])):
		value = data["results"]["bindings"][i]["itemLabel"]["value"]
		"""
		if "Meta" in value or value == "":
			print("something with meta")
		else:
			print("data: ", value)
			resultDict[searchquery].append(value)
			print(resultDict)
		"""
		value.strip(" ")
		if value in grundwortschatz and value != "":
			print("data: ", value)
			resultDict[searchquery].append(value)
			print(resultDict)
		else:
			print(value, "not in grundwortschatz")
			valuelist = value.split(" ")
			wordexists = False

			for word in valuelist:
				docnlp = nlp(word) #load to spacy
				print(docnlp)
				for token in docnlp:
					word = str(token.lemma_)
					print(word, "word lemma????????????????????????????????????")
				if word in grundwortschatz and word != "":
					print(word, "exists")
					wordexists = True
				else:
					wordexists = False
					#insert charsplit?
					print(word, "doesn't exist")
					break
			if wordexists == True:
				resultDict[searchquery].append(value)
				print(resultDict)




	return resultDict

input= """

Pascal sitzt im Bus in der zweitletzten Reihe .
 Ein großer Junge mit einer Wasserflasche
 setzt sich hinter ihn , nimmt einen Schluck
 Wasser aus der Flasche und spuckt es ihm auf
 den Kopf . Haare und Klamotten sind nass .

 Der 14-jährige Kevin sitzt im Rollstuhl . Jeden
 Morgen wartet er auf das Taxi und wird von
 einigen Jugendlichen gemobbt . Sie stellen sich
 in den Weg , sodass er auf dem Bürgersteig
 nicht mehr weiter kann . „ Hast du ein Problem ? ” ,
 fragt ihn einer . Die anderen lachen .

"""

list = prepare_search(input, language="")
print(list)

for word in list:
	try:
			resultDict = get_categories(word)
	except:
			print(f"Error!! Couldn't get result category searching with: {word}")
			continue
#get_categories("Ritter")
for key in resultDict:
	if resultDict[key] != []:
		print(key,": ")
		print(", ".join(resultDict[key]))
