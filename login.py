
from flask import Flask, render_template, request
from os import listdir

app= Flask(__name__)

@app.route('/', methods=['GET'])
def initiali():
	inpo=request.form['age']
	if request.method == 'GET':
		with open('ages.txt', 'w') as f:
			f.write(str(inpo))
	return render_template("login.html", ages=inpo)

@app.route('/cipher')
def index():
	return """<form method="POST">
					<input type="text" name="Name">
					<input type="submit" value="give">
					</form>"""

if __name__ == '__main__':
	app.run(debug=true)