from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	d = request.get_json()
	flat = set([i for r in d for i in r])
	if len(flat) < 81:
		return "Complete the grid"

	if ref[0][0] != d[0][0] or ref[9][9] != d[9][9]:
		return "Wrong"

	sums = [sum(r) for r in d]
	sums += [sum([d[i][j] for i in range(len(d))]) for j in range(len(d))]
	sums.append(sum([d[i][i] for i in range(len(d))]))
	sums.append(sum([d[len(d)-i][i-1] for i in range(len(d),0,-1)]))
	if len(set(sums)) > 1:
		return "Try Again"
	return 'flag{y3r_a_wiz3rd_h4rry}'

ref = [
	[65,None,None,None,1,4,None,None,None,60],
	[None,66,None,None,3,2,None,None,59,None],
	[None,None,17,20,None,None,53,56,None,None],
	[None,None,19,18,None,None,55,54,None,None],
	[13,16,None,None,52,49,None,None,85,88],
	[15,14,None,None,51,50,None,None,87,86],
	[None,None,48,45,None,None,84,81,None,None],
	[None,None,47,46,None,None,83,82,None,None],
	[None,41,None,None,100,97,None,None,36,None],
	[42,None,None,None,98,99,None,None,None,35],
]

if __name__=='__main__':
	app.run(host="0.0.0.0",port=4000)
