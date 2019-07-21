
def search_known_verbs(knownVerbs, Tense, found_verb):

	if (knownVerbs[1][0]['LEMMA'] == found_verb.lemma_
		and knownVerbs[1][0]['TENSE'] == Tense
		and knownVerbs[1][0]['PERSON'] == '1per'
		and knownVerbs[1][0]['NUMERUS'] == 'sing'
		and knownVerbs[1][0]['MODE'] == 'ind'):
		return True
	else:
		return False

def search_unknown_verbs(foundInDEMorphy, word, Tense, known_verb_list, printString, found_verb):
	if (word[1].lemma == found_verb.lemma_
		and word[1].tense == Tense
		and word[1].person == '1per'
		and word[1].numerus == 'sing'
		and word[1].mode == 'ind'):

		print(f'		{Tense}: ich ' + word[0])
		#print(word)
		#foundInDEMorphy += 1
		pres1 = 'ich ' + word[0]
		printString[f'{Tense}1'] = pres1

		newResult =[word[0], [{'LEMMA': word[1].lemma,
									'MODE': word[1].mode,
									'NUMERUS': word[1].numerus,
									'PERSON': word[1].person,
									'TENSE': word[1].tense}]]
		alreadyin = False
		for knownVerbs in known_verb_list:
			#print(known_verb_list)
			if newResult[0] == knownVerbs[0] and word[1].mode == knownVerbs[1][0]['MODE']:
				print(f'{Tense}1: already in known verb list: ' + knownVerbs[0])
				alreadyin = True
			elif alreadyin == False and knownVerbs[0] == known_verb_list[-1][0]:
				print('					new word saved: '+ str(newResult))
				known_verb_list.append(newResult)
				print('append')
				#print('important verb list: ' + str(known_verb_list[0][0]))
	return known_verb_list, printString, foundInDEMorphy
