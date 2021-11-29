from project import myapp_obj
from project.forms import LoginForm
from flask import render_template, flash, redirect

from project import db
from project.models import User, FlashCard, Notes
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/loggedin")
@login_required
def log():
    return 'Hi you are logged in'

@myapp_obj.route("/logout")
def logout():
    logout_user()
    return redirect('/')

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login invalid username or password!')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        flash(f'Login requested for user {form.username.data},remember_me={form.remember_me.data}')
        flash(f'Login password {form.password.data}')
        return redirect('/')
    return render_template("login.html", form=form)

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return 'Hi ' + name

@myapp_obj.route("/signup", methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Welcome!')
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username, email)
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_templates('signup.html', form=form)

@myapp_obj.route("/home", methods=['GET', 'POST']
def home():
    return render_template('home.html')

@myapp_obj.route("/input_flash", methods=['GET', 'POST'])
def inputflash():
    form = CreateFlash()
    if form.validate_on_submit():
	flash(f'Added!')
	title = form.title.data
	body = form.body.data
	flashc = FlashCard(title, body)
	db.session.add(flashc)
	db.session.commit()
	return redirect("/home")
    return render_templates('inpFlash.html', form=form)

@myapp_obj.route("/renderFlashCard", methods=['GET', 'POST'])
def outputflash():
    return render_templates("flashlist.html")

@myapp_obj.route("/shareFlashCard", methods-['GET', 'POST'])
def shareFlash():
	form =ShareForm()
	if form.validate_on_submit():
	    user = User.query.filter_by(username=form.User.data).first()
		if user is None:
			flash('Invalid User')
			return redirect("/shareFlashCard")
	    flash = FlashCard.query.filter_by(title=form.Title.data).first()
		if flash is None:
			flash('Invalid FlashCard')
			return redirect("/shareFlashCard")	
	    user.sharedFlash(flash)	
	    flash(f'Shared!')
            return redirect("/shareFlashCard")
	return render_template('ShareFlash.html', form=form)

@myapp_obj.route("/shareNotes", methods=['GET, 'POST'])
def shareNotes():
    form = ShareForm()
    if form.validate_on_submit():
         user = User.query.filter_by(username=form.User.data).first()
         if user is None:
               flash('Invalid User')
               return redirect("/shareNotes")
         note = Notes.query.filter_by(title=form.Title.data).first()
         if note is None:
               flash('Invalid Note')
               return redirect("/shareNotes") 
         user.sharedNotes(note)
	 flash(f'Shared!')
         return redirect("/shareNotes")
    return render_template("ShareFlash.html", form=form)
