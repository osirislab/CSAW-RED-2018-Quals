from flask import Flask, request, abort
import json

app = Flask(__name__)

def empty(s):
	return s == '' or s == None

@app.route('/submit')
def submit():
	ua = "Mozilla/5.0 (compatible; GoogleDocs; apps-spreadsheets; +http://docs.google.com)"
	if request.headers.get('User-Agent') != ua:
		print request.headers.get('User-Agent')
		return abort(403)
	
	test = request.args.get('test')
	try:
		if (empty(test) or int(test) != 1):
			return "WrOnG 1"
	except ValueError:
		return "It'S jUsT a TeSt..."
	# get request returns strings, so first will always be a string no matter what's in the cells
	first = request.args.get('first')
	if (empty(first) or first != '1123581321'):
		return "WrOnG 2"

	second = request.args.get('second')
	if empty(second):
		return "MiSsInG sOmEtHiNg?"
	try:
		if (int(second) + 12 != 65):
			return "WrOnG 3"
	except ValueError:
		return "ThAt'S nOt A nUmBeR"

	third = request.args.get('third')
	fourth = request.args.get('fourth')
	fifth = request.args.get('fifth')
	sixth = request.args.get('sixth')

	if (empty(third) or empty(fourth) or empty(fifth) or empty(sixth)):
		return "MiSsInG sOmEtHiNg?"

	try:
		if (int(fourth) % int(third) != int(fifth) + int(sixth)):
			return "WrOnG 4"
	except ValueError:
		return "ThAt'S nOt A nUmBeR"
	except ZeroDivisionError:
		return "ThAt'S dAnGeRoUs"

	seventh = request.args.get('seventh')
	eighth = request.args.get('eighth')
	ninth = request.args.get('ninth')
	tenth = request.args.get('tenth')
	if (empty(seventh) or empty(eighth) or empty(ninth) or empty(tenth)):
		return "MiSsInG sOmEtHiNg?"
	try:
		if (int(seventh) + int(eighth) + int(ninth) != 2 * int(tenth)):
			return "WrOnG 5"
	except ValueError:
		return "ThAt'S nOt A nUmBeR"

	eleventh = request.args.get('eleventh')
	if (empty(eleventh)):
		return "MiSsInG sOmEtHiNg?"

	asciiSum = sum([ord(c) for c in eleventh])
	if (asciiSum != 4034):
		return "WrOnG 6"

	twelfth = request.args.get('twelfth')
	if (empty(twelfth)):
		return "MiSsInG sOmEtHiNg?"
	try:
		if (int(twelfth) % 2 != 0):
			return "WrOnG 7"
	except ValueError:
		return "ThAt'S nOt A nUmBeR"

	thirteenth = request.args.get('thirteenth')
	fourteenth = request.args.get('fourteenth')
	fifteenth = request.args.get('fifteenth')
	sixteenth = request.args.get('sixteenth')

	if (empty(thirteenth) or empty(fourteenth) or empty(fifteenth) or empty(sixteenth)):
		return "MiSsInG sOmEtHiNg?"

	try:
		if (int(sixteenth) / 3 != len(fourteenth)):
			return "WrOnG 8"
		if (int(int(int(fifteenth) ^ int(thirteenth, 16)) / (1+1+2+3+5+8+13+21)) != 234229):
			return "WrOnG 9"
	except ValueError:
		return "ThErE's A pRoBlEm HeRe"

	seventeenth = request.args.get('seventeenth')
	summation = 0
	if empty(seventeenth):
		return "MiSsInG sOmEtHiNg?"
	try:
		for i in range(1, int(seventh) + 1):
			summation = summation + (2 + (3 * (i - 1)))

		if (summation % int(seventeenth) != int(ninth)):
			return "WrOnG 10"
	except ValueError:
		return "ThErE's A pRoBlEm HeRe"
	except ZeroDivisionError:
		return "ThAt'S dAnGeRoUs"

	return "flag{u_cant_contain_meeeeeeeeee}"

if __name__=='__main__':
	app.run(host="0.0.0.0",port=4000)
