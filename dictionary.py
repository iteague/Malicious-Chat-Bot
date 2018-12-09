from textblob import TextBlob
def main():
	userInfo = open('userInfo.txt','r')

	text = userInfo.read()
	blob = TextBlob(text)
	blob.tags
	blob.noun_phrases

	print(blob.tags)
		
	wordList = []
	#needed tags: NNP, NN,  NNS
	#create a list of words with needed tags
	for i in blob.tags:
		tag = i[1]
		if tag == 'NNP' or tag == 'NN' or tag =='NNS':
			wordList.append(i[0])
	print(wordList)
	#write each word in wordlist to a file
	passwordDictionary = open('dictionary.txt','w')
	commonWords = ['i','yeah','stuff','something','me','oh','ok','lot','just','ah','wow']
	for i in wordList:
		word = i.lower()
		if word not in commonWords:
			passwordDictionary.write(i+'\n')

	#match each word together and write it to a file as a new phrase
	wordList2 = []
	for i in wordList:
		word = i.lower()
		for j in wordList:
			if word not in commonWords:
				if i + j not in wordList2:
					wordList2.append(i+j)
	for i in wordList2:
		passwordDictionary.write(i + '\n')
				
	passwordDictionary.close()
	
main()
