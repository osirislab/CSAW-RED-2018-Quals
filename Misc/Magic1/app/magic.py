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
	sums = [sum(r) for r in d]
	sums += [sum([d[i][j] for i in range(len(d))]) for j in range(len(d))]
	sums.append(sum([d[i][i] for i in range(len(d))]))
	sums.append(sum([d[len(d)-i][i-1] for i in range(len(d),0,-1)]))
	if len(set(sums)) > 1:
		return "Try Again"
	return 'flag{b_th3r3_0r_bee_squ4re}' 

if __name__=='__main__':
	app.run(host="0.0.0.0",port=4000)
