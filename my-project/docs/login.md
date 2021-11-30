# Login Page

### Login Function

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

login.html
```python
    {% extends "base.html" %}

    {% block content %}

    <h1>Login</h1>

    <form method = "POST" novalidate >
          {{ form.hidden_tag() }}

    <p> {{ form.username.label }} <br>
        {{ form.username }}</p>

    <p> {{ form.password.label }} <br>
        {{ form.password }}</p>

    <p> {{ form.remember_me.label }} <br>
        {{ form.remember_me() }}</p>

    <p> {{ form.submit() }} </p>

    </form>
    {% endblock %}
```
loggedin.html
```python
{% extends "base.html" %}

{% block content %}
<h1>Welcome</h1>
<p>{{ title }} </p>
{% endblock  %}
```
logout.html
```python
{% extends "base.html" %}

{% block content %}
<h1>Logout </h1>
{% endblock %}
```

routes.py
```python
@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    getuser=User.query.all()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user)
        return redirect('/loggedin')
    return render_template("login.html", form=form)
```

```python
@myapp_obj.route('/loggedin')
@login_required
def log():
    flash('You are logged in', 'error')
    return redirect('/')
```

```python
@myapp_obj.route('/logout')
def logout():
    logout_user()
    flash('You are logged out', 'error')
    return redirect('/')
```
