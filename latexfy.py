def latexfy(s):
	s = list(s)
	simbols = {
	'é' : "\\'e",
	'ê' : "\\^e",
	'á' : "\\'a",
	'â' : "\\^a",
	'à' : "\\`a",
	'ã' : "\\~a",
	'ç' : "\\c{c}",
	'í' : "\\'i",
	'ó' : "\\'o",
	'ô' : "\\^o",
	'õ' : "\\~o",
	'ú' : "\\'u"
	}

	for n, l in enumerate(s):
		if l in simbols:
			s[n] = simbols[l]
		elif l.lower() in simbols:
			s[n] = simbols[l.lower()].upper()

	return ''.join(s)

if __name__ == '__main__':
	string = '''
	'''

	print(latexfy(string))
