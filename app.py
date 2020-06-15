from flask import Flask,render_template,request,url_for,redirect


app=Flask(__name__)


@app.route("/",methods=["GET"])
def index():
	return render_template('home.html')


@app.route("/register",methods=['GET',"POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	if request.method == "POST":
		app.logger.info(request.form)
		# return redirect(url_for('index'))
		return render_template("register.html")

@app.route("/login",methods=['GET',"POST"])
def login():
	if request.method == 'GET':
		return render_template('login.html')


@app.route("/about")
def about():
	return render_template('about.html')

	
@app.route("/gallery")
def gallery():
	return render_template('gallery.html')

@app.route("/events")
def events():
	return 'events'
if(__name__ == "__main__"):
	app.run(debug=True,host='0.0.0.0',port=8080)