import itertools
import networkx as nx
import nltk

class Everything:

	def filter_for_tags(self, tagged, tags=['NN', 'JJ', 'NNP']):
		return [item for item in tagged if item[1] in tags]

	def normalize(self, tagged):
		return [(item[0].replace('.', ''), item[1]) for item in tagged]

	def unique_everseen(self, iterable, key=None):
		seen = set()
		seen_add = seen.add
		if key is None:
			for element in [x for x in iterable if x not in seen]:
				seen_add(element)
				yield element
		else:
			for element in iterable:
				k = key(element)
				if k not in seen:
					seen_add(k)
					yield element

	def levenshtein_distance(self, first, second):
		if len(first) > len(second):
			first, second = second, first
		distances = range(len(first) + 1)
		for index2, char2 in enumerate(second):
			new_distances = [index2 + 1]
			for index1, char1 in enumerate(first):
				if char1 == char2:
					new_distances.append(distances[index1])
				else:
					new_distances.append(1 + min((distances[index1], distances[index1 + 1], new_distances[-1])))
			distances = new_distances
		return distances[-1]

	def build_graph(self, nodes):
		gr = nx.Graph() 
		gr.add_nodes_from(nodes)
		nodePairs = list(itertools.combinations(nodes, 2))

		for pair in nodePairs:
			firstString = pair[0]
			secondString = pair[1]
			levDistance = self.levenshtein_distance(firstString, secondString)
			gr.add_edge(firstString, secondString, weight=levDistance)

		return gr

	def extract_key_phrases(self, text):
		word_tokens = nltk.word_tokenize(text)

		tagged = nltk.pos_tag(word_tokens)
		textlist = [x[0] for x in tagged]

		tagged = self.filter_for_tags(tagged)
		tagged = self.normalize(tagged)

		unique_word_set = self.unique_everseen([x[0] for x in tagged])
		word_set_list = list(unique_word_set)

		graph = self.build_graph(word_set_list)
		calculated_page_rank = nx.pagerank(graph, weight='weight')
		keyphrases = sorted(calculated_page_rank, key=calculated_page_rank.get,
							reverse=True)

		one_third = len(word_set_list) // 3
		keyphrases = keyphrases[0:one_third + 1]

		modified_key_phrases = set([])
		dealt_with = set([])
		i = 0
		j = 1
		while j < len(textlist):
			first = textlist[i]
			second = textlist[j]
			if first in keyphrases and second in keyphrases:
				keyphrase = first + ' ' + second
				modified_key_phrases.add(keyphrase)
				dealt_with.add(first)
				dealt_with.add(second)
			else:
				if first in keyphrases and first not in dealt_with:
					modified_key_phrases.add(first)

				if j == len(textlist) - 1 and second in keyphrases and \
						second not in dealt_with:
					modified_key_phrases.add(second)

			i = i + 1
			j = j + 1

		return modified_key_phrases


	def extract_sentences(self, text, summary_length=100, clean_sentences=False):
		sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		sentence_tokens = sent_detector.tokenize(text.strip())
		graph = self.build_graph(sentence_tokens)

		calculated_page_rank = nx.pagerank(graph, weight='weight')
		sentences = sorted(calculated_page_rank, key=calculated_page_rank.get,
						   reverse=True)

		summary = ' '.join(sentences)		
		summary_words = summary.split()
		summary_words = summary_words[0:summary_length]
		dot_indices = [idx for idx, word in enumerate(summary_words) if word.find('.') != -1]
		if clean_sentences and dot_indices:
			last_dot = max(dot_indices) + 1
			summary = ' '.join(summary_words[0:last_dot])
		else:
			summary = ' '.join(summary_words)

		return summary

	
	def mine(self, text):
		keyphrases=self.extract_key_phrases(text)
		summary=self.extract_sentences(text)
		return summary
