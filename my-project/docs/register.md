# Register Page

### Register Function

This is our import Flask library

```python
    import time, os, re, markdown

    from flask import *
    from flask_login import current_user, login_user, logout_user, login_required
    from flask_mail import Message

    from werkzeug.utils import secure_filename

    from myapp import myapp_obj, basedir, db, mail
    from myapp.forms import LoginForm, RegisterForm, FileForm, uploadForm
    from myapp.models import User, Post, todo_list
```

We can take in a username and password to create an account

routes.py

```python 
@myapp_obj.route('/register' ,methods=['GET','POST'])
def register():
    form = RegisterForm()
   # all_users = User.query.all()

    if form.validate_on_submit():
        new_user = User(username=form.username.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You are registered', 'error')
        return redirect("/login")
    return render_template("register.html",form=form)
```

register.html

```html 
{% extends "base.html" %}

{% block content %}
<head>
	<title>{{ title }}</title>
</head>

<h2>Sign-Up</h2>
<p>Let's Get Started!</p>
<p>Please enter a Username and Password</p>
<form method = "POST" novalidate >
	        {{ form.hidden_tag() }}

		        <p> {{ form.username.label }} <br>
			            {{ form.username }}</p>
			        <p> {{ form.password.label }} <br>
				            {{ form.password }}

					        <p> {{ form.submit() }} </p>

</form>
<h2>
	<a href="/login">Already signed up? Click here to Log In</a>
</h2>
{% endblock %} 
```
