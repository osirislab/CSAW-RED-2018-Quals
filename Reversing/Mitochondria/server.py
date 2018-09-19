from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/submit')
def submit():

	test = request.args.get('test')
	print(test)
	if (int(test) != 1):
		return "WrOnG 1"

	first = request.args.get('first')
	if (first != '1123581321'):
		return "WrOnG 2"

	second = request.args.get('second')
	if (int(second) + 12 != 65):
		return "WrOnG 3"

	third = request.args.get('third')
	fourth = request.args.get('fourth')
	fifth = request.args.get('fifth')
	sixth = request.args.get('sixth')
	if (int(fourth) % int(third) != int(fifth) + int(sixth)):
		return "WrOnG 4"

	seventh = request.args.get('seventh')
	eighth = request.args.get('eighth')
	ninth = request.args.get('ninth')
	tenth = request.args.get('tenth')
	if (int(seventh) + int(eighth) + int(ninth) != 2 * int(tenth)):
		return "WrOnG 5"

	eleventh = request.args.get('eleventh')
	asciiSum = sum([ord(c) for c in eleventh])
	if (asciiSum != 4034):
		return "WrOnG 6"

	twelfth = request.args.get('twelfth')
	if (int(twelfth) % 2 != 0):
		return "WrOnG 7"

	thirteenth = request.args.get('thirteenth')
	fourteenth = request.args.get('fourteenth')
	fifteenth = request.args.get('fifteenth')
	sixteenth = request.args.get('sixteenth')

	if (int(sixteenth) / 3 != len(fourteenth)):
		return "WrOnG 8"
	if (int(int(int(fifteenth) ^ int(thirteenth, 16)) / (1+1+2+3+5+8+13+21)) != 234229):
		return "WrOnG 9"

	seventeenth = request.args.get('seventeenth')
	summation = 0
	for i in range(1, int(seventh) + 1):
		summation = summation + (2 + (3 * (i - 1)))

	if (summation % int(seventeenth) != int(ninth)):
		return "WrOnG 10"

	return "flag{you_done_did_it}"

if __name__=='__main__':
	app.run(port=8080)