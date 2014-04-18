from dico import box

def lettres_check(lettres,mot):
	for l in mot:
		if l in lettres:
			lettres.remove(l)
		else:
			return [False,0]
	if mot in box:
		return [True,len(mot)]
	else:
		return [False,0]
