import numpy

def pageRank(matr, eps=0.0001, d=0.85):
	p=np.ones(len(matr))/len(matr)
	while True:
		newP=np.ones(len(matr))/len(matr)*(1-d)/len(matr)+d*matr.T.dot(p)
		delta=abs((newP-p).sum())
		if delta <= eps:
			return newP
		p=newP
		