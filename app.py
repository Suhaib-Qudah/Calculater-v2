from flask import Flask,render_template,request,redirect,url_for
from data import generate_contacts,Contact


#create flask app
app = Flask(__name__)
#Generate Dummy data 
contact_book = generate_contacts()

@app.route('/')
@app.route('/index')
def index():
   return render_template('layout.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', contacts = contact_book.get_contacts())


@app.route('/add', methods = ['GET','POST'])
def add():
    if request.method == 'POST':
         #get values from html
        first_name = request.form['first_name'] 
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
      
        # create a new contact
        contact = Contact(first_name,last_name,username,email)
        
        # add contact to contact book
        contact_book.add_contact(contact)

        return render_template('layout.html')
    else:
       
        return render_template('add.html')


@app.route('/edit/<int:id>' , methods = ["POST", "GET"])
def edit(id):
    if request.method == "POST":
        contact = contact_book.get_contact_by_id(id)

        firstname = request.form['first_name'] 
        lastname = request.form['last_name']
        username = request.form['username']
        email = request.form['email']

        contact.set_username(username)
        contact.set_f_name(firstname)
        contact.set_l_name(lastname)
        contact.set_email(email)

        return render_template('layout.html',contact= contact )

    else:
        contact = contact_book.get_contact_by_id(id)
        return render_template('edit.html',contact= contact)


@app.route('/delete/<int:id>',methods = ['GET','POST'])
def delete(id):
    id = int(id)
    contact_book.remove_contact(id)
    return redirect(url_for('index'))



