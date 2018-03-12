from nltk.cluster.util import cosine_distance
from nltk.corpus import stopwords

def sent_similarity(s1, s2, stopwords=None):
    if(stopwords is None):
        stopwords=[]

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
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    #build vector for the second sentence
    for w in s2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1-cosine_distance(vector1, vector2)


print(sent_similarity("hello world", "helli world", stopwords.words('english')))
