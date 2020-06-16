from flask import Flask,render_template,request,url_for,redirect,session
from flask_mysqldb import MySQL
from os import environ
from hashlib import sha256
from uuid import uuid4

app=Flask(__name__)
app.config['SECRET_KEY']="THIS IS A SECRET!!!!"
app.config['MYSQL_USER'] = environ['mysql-user']
app.config['MYSQL_PASSWORD'] = environ['mysql-pass']
app.config['MYSQL_DB'] = 'NISB'

mysql = MySQL()
mysql.init_app(app)


@app.route("/",methods=["GET"])
def index():
	return render_template('home.html')


@app.route("/register",methods=['GET',"POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	if request.method == "POST":
		app.logger.info(request.form)
		

		cursor = mysql.connection.cursor()
		first_name = request.form['fname']
		last_name = request.form['lname']
		email = request.form['email']
		ieee_num = request.form['ieee_num']
		branch = request.form['branch']
		password = request.form['password']
		salt = str(uuid4()).replace('-','')[2:8]
		pass_hash = sha256((salt[:4]+password+salt[4:]).encode()).hexdigest()
		
		query_string = "INSERT INTO users (first_name,last_name,email,ieee_num,branch,pass_hash,pass_salt) VALUES (%s, %s, %s, %s, %s, %s, %s);"
		cursor.execute(query_string,(first_name,last_name,email,ieee_num,branch,pass_hash,salt))

		session['user']=cursor.lastrowid
		app.logger.info(session['user'])	
		mysql.connection.commit()
		cursor.close()


		return redirect(url_for('index'))

@app.route("/login",methods=['GET',"POST"])
def login():
	if request.method == 'GET':
		return render_template('login.html',invalid_creds=False)
	if request.method == "POST":
		ieee_num = request.form['ieee_num']
		password = request.form['password']
		app.logger.info(ieee_num)
		cursor = mysql.connection.cursor()
		query_string = "SELECT _id,pass_hash,pass_salt FROM users WHERE ieee_num = %s"
		cursor.execute(query_string,[ieee_num])

		data = cursor.fetchall()

		salt = data[0][2]
		passhash = sha256((salt[:4]+password+salt[4:]).encode()).hexdigest()

		if(passhash == data[0][1]):
			session['user']=data[0][0]
			return redirect(url_for('index'))
		else:
			return render_template('login.html',invalid_creds=True)



		cursor.execute("SELECT * FROM users WHERE ")


@app.route("/about")
def about():
	return render_template('about.html')

	
@app.route("/gallery")
def gallery():
	return render_template('gallery.html')

@app.route("/events")
def events():
	return render_template('events.html')

@app.route('/logout')
def logout():
	session['user']=None
	return render_template('home.html')
	
if(__name__ == "__main__"):
	app.run(debug=True,host='0.0.0.0',port=8080)