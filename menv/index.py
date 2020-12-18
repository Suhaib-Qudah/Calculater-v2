from flask import Flask, render_template, url_for, flash, redirect, request
from datetime import datetime

# Create an instance of the Flask application
app = Flask(__name__)
#Create a secret key 
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

app = Flask(__name__)
me = {
	"first_name":"Suhaib",
	"last_name":"Qudah",
	"address": "Amman/jordan",
	"description": "Frontend at altibbi",
	"social_links": [
			{"site":"Facebook","url":"https://facebook.com/saeb.almajali.99"}, 
			{"site": "GitHub", "url": "https://github.com/saeb998"}
	],
	"age": 22,
    "avatarpic": "https://web.facebook.com/photo/?fbid=3171178226226881&set=a.358728794138519",
	"email": "saeb998almajali@gmail.com",
	"skills": ["Python" , "c++" , "java" , "networking"],
	"projects": [
		{"name":"mini wep site ", "description":"a small wep site for shoping", "tags":["shopping"]},
	],
    "work_experince" :[
        {"jop":"data entry" , "company":"alkarak company"},
        {"jop":"maintenance","company":"zain company"}
    ],
	"sport" : [
		{"sport":"football", "position":"CM"},
		{"sport":"basketball", "position":"AMF"},
	]
}
@app.route('/')
def index():
	name = me.get('first_name') + " " + me.get("last_name") 
	disc = me.get('description')
	time = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
	menu = [{"title":"Me", "url":url_for("personal_info")},
            {"title":"Skills", "url":url_for("my_skills")},
            {"title":"Projects", "url":url_for("my_projects")},
            {"title":"Sports", "url":url_for("my_sports")}
        ]
	return render_template('home.html' , name =name , disc = disc , time = time , menu = menu)
@app.route('/personal')
def personal_info():
    title= "personal page"
    name = me.get('first_name') + " " + me.get("last_name")
    disc = me.get('description')
    age = me.get('age')
    social_links = []
    email = me.get('email')
    for i in me.get('social_links'):
        social_links.append(i)
        pass
    return render_template('personal.html' ,title = title, age = age, name=name, disc = disc , social_links =social_links, email = email)
    pass
@app.route('/skill')
def my_skills():
    skills = me.get('skills')
    return render_template('skill.html', skills =skills, title = "My personal skills is:")
    pass
@app.route('/')
def my_projects():
	pass

@app.route('/edit' , methods= ['post', 'get'])
def edit():
    name = me.get('first_name') + " " + me.get("last_name")
    age = me.get('age')
    email = me.get('email')
    address = me.get('address')
    if request.method == 'POST':
        name = str(request.form['name'])   # read the value from the first number input
        email = str(request.form['email'])  # read the value from the second number input
        age = int(request.form['age'])  # read the value from the second number input
        address = str(request.form['address'])
        description = me.get('description')
        me['email'] = email 
            # render the add page
        return render_template("personal.html", age = age, email = email, name = name, address= address,disc=description )
    pass
    return render_template('edit.html', title = "Edit page", age = age, email = email, name = name, address= address)

@app.route('/sport')
def my_sports():
    favorite  =  []
    for i in me.get('sport'):
        favorite.append(i)
        pass
    return render_template('sport.html', favorite = favorite , title = "My favorite things is:")
pass

