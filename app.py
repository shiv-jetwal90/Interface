from flask  import  Flask,  render_template, flash, redirect, url_for, session, logging, request
#from data import Articles
import mysql.connector
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.handlers.sha2_crypt import sha512_crypt


app = Flask(__name__, template_folder='templates')
cnx= mysql.connector.connect(user ='root', password= '#########', host = '127.0.0.1', database='mysql',auth_plugin='mysql_native_password')



@app.route('/')
def index ( ) :
    return  render_template('home.html')

@app.route('/about')
def about(  ):
    return render_template ('about.html')

@app.route('/articles')
def articles(  ):
    return render_template ('articles.html',articles = Articles)

@app.route('/article/<string:id>/')
def article( id ):
    return render_template ('article.html',id=id)

# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)] )
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


@app.route( '/register', methods = ['GET', 'POST'])
def register( ):
	global name,email,username,password
	form = RegisterForm(request.form)
	if request.method   ==  'POST' and form.validate( ):
              name =form.name.data
              email = form.email.data
              username = form.username.data
              password = sha512_crypt.encrypt(str(form.password.data))
# Making Cursor Object For Query Execution
	cur=cnx.cursor()
	cur.execute("INSERT INTO  users (name, email, username, password) VALUES (%s ,%s, %s ,%s)",(name, email, username, password))
	cnx.commit()
	cur.commit()
	cnx.close()

	flash('You are Registerd','Sucess')

	redirect(url_for  ('index') )
	return render_template('register.html')
	return render_template('register.html', form = form)

if __name__ == '__main__' :
       app.secret_key= 'secret123'
       app.run(debug=True)
