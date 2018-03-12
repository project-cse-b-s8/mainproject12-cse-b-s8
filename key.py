import nltk
import string
import numpy as np
from nltk.tokenize import *
from nltk.corpus import stopwords
CONST_N = 10

with_punct_txt=open('input.txt', 'r', encoding='utf-8').read()
txt=with_punct_txt.translate(with_punct_txt.maketrans({key: None for key in string.punctuation})) #remove punctuation
txt_list=txt.split()

word_list=word_tokenize(txt)
word_list=[w.lower() for w in word_list]


def get_uniq_words(word_list, stop_words):
	uniq=[]
	punct=list(string.punctuation)
	for w in word_list:
		if w in stop_words:
			continue 
		if w in uniq: # if already in there
			continue
		if w in punct:
			continue
		temp=[w]
		uniq+=temp
	#uniq_set=set(uniq)
	#uniq=list(uniq_set)
	return uniq

def create_graph(uniq_word_list):
	word_graph=np.zeros((len(uniq_word_list), len(uniq_word_list)))#no edge
	for i in uniq_word_list:
		word_indices=[q for q,val in enumerate(txt_list) if val==i]
		for j in word_indices:
			for k in uniq_word_list:
				if i==k:
					continue
				srch_list=txt_list[j+1:j+1+CONST_N]
				if k in srch_list:
					word_graph[uniq_word_list.index(i)][uniq_word_list.index(k)]=1
					word_graph[uniq_word_list.index(k)][uniq_word_list.index(i)]=1
					
					
	#graph_vector_sum_list=[w.sum()/len(uniq_word_list) for w in word_graph]
	temp_list=[w.sum()/len(uniq_word_list) for w in word_graph]
	graph_vector_sum_list=np.array([])
	graph_vector_sum_list=np.append(graph_vector_sum_list, temp_list)
	print("graph_vector_sum_list: ")
	print(graph_vector_sum_list)
	#print(type(graph_vector_sum_list))
	
	sorted_indices=np.argsort(-graph_vector_sum_list) #indices in descending order
	print("sorted: ")
	print(sorted_indices)	
	
	return sorted_indices.tolist()
	
stop_words=stopwords.words('english')
uniq_word_list=get_uniq_words(word_list, stop_words)
tagged_uniq_words = nltk.pos_tag(uniq_word_list)

word_graph=create_graph(uniq_word_list)


