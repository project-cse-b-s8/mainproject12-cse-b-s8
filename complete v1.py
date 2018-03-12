text="I'm currently installing some programs. They were made by a giant company which maintains the appearance of a 'make world better' sort of organisation but really isn't. They want to control the people. Handing out licences to which the people have no choice but agree blindly and forcing them to remain connected to their servers so as to sustain and enhance the company's hold over their unfortunate 'customer' or user."

import io
f=io.open('input.txt', mode='r', encoding='utf-8')
text=f.read()


import nltk
import numpy as np

#from nltk.book import *
from nltk.tokenize import *
from nltk.cluster.util import cosine_distance
from nltk.corpus import stopwords


def sent_similarity(s1, s2, stop_words=None):
    if(stop_words is None):
        stop_words=[]

    #convert sentence to list of words
    s1 = s1.split()
    s2 = s2.split()

    #convert the words to lower case
    s1 = [w.lower() for w in s1]
    s2 = [w.lower() for w in s2]

    all_words=list(set(s1+s2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words) #the weights, I guess

    #build vector for the first sentence
    for w in s1:
        if w in stop_words:
            continue
        vector1[all_words.index(w)] += 1

    #build vector for the second sentence
    for w in s2:
        if w in stop_words:
            continue
        vector2[all_words.index(w)] += 1

    return 1-cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words=None):
	s=np.zeros((len(sentences), len(sentences)))

	for idx in range(len(sentences)):
		for idx2 in range(len(sentences)):
			if(idx==idx2):
				continue
			s[idx][idx2] = sent_similarity(sentences[idx], sentences[idx2], stop_words)
	for idx in range(len(s)):
		s[idx]/=s[idx].sum()
	return s

sent_list=sent_tokenize(text) #text converted to sentences
similarity_matrix=build_similarity_matrix(sent_list, stopwords.words('english'))




