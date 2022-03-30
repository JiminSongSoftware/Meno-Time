# To-Do List Page

### To-Do Function

This is our import Flask library

```python
    import time, os, re, markdown

    from flask import *
    from flask_login import current_user, login_user, logout_user, login_required
    from flask_mail import Message

    from werkzeug.utils import secure_filename

    from myapp import application, basedir, db, mail
    from myapp.forms import LoginForm, RegisterForm, FileForm, uploadForm
    from myapp.models import User, Post, todo_list
```

todolist.html
```html
{% extends "base.html" %}

{% block content %}
<body>
    <div>
	    <h2>To-Do</h2>
        <p style = "font-size: 12pt">Help yourself with task in priorities</p>
        <h3>Type in things to-do</h3>
        <form action = "{{ url_for('add') }}" method = "POST">
            <input type = "text" name = "todoitem">
            <input type = "submit" value = "submit" class = "button">
        </form>
    </div>
    <h2>Waiting to be completed</h2>
    <p>Click Done to move incomplete task to complete section</p>
    <ul>
        {% for todo in incomplete %}
        <li style = "font-size: 12pt">{{ todo.todo_item}}<a href="{{ url_for('complete', id=todo.id) }}">: Done</a></li>
        {% endfor %}
    </ul>
    <h2>Completed tasks</h2>
    <ol>
        {% for todo in complete %}
        <li style = "font-size: 12pt"> {{ todo.todo_item }} </li>
        {% endfor %}
    </ol>

</body>

{% endblock  %}
```

```python
routes.py
@application.route('/todolist')
def todolist():
    title = 'To-Do List'
    complete = todo_list.query.filter_by(complete=True).all()
    incomplete = todo_list.query.filter_by(complete=False).all()

    return render_template('todolist.html', title = title,complete = complete, incomplete = incomplete)

@application.route('/add', methods=['POST'])
def add():
    todo = todo_list(todo_item = request.form["todoitem"], complete = False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('todolist'))

@application.route('/complete/<id>')
def complete(id):
    todo = todo_list.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()

    return redirect(url_for('todolist'))
```
