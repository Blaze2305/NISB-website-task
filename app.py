from flask import Flask,render_template,request,url_for,redirect


app=Flask(__name__)


@app.route("/",methods=["GET"])
def index():
	return render_template('home.html')

if(__name__ == "__main__"):
	app.run(debug=True,host='0.0.0.0',port=8080)