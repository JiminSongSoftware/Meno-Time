# Share Note Page

### Share Note Function

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

shareNote.html
```html
{% extends "base.html" %}

{% block content %}
<!DOCTYPE html>
<body>
    <div class="text-left mx-auto d-block">
        <div class="col-md-12 mx-auto d-block">
            <div class="card-body col-md-8 mx-auto d-block">
                <h3 style='color:black' class="card-title text-left">Share Notes</h3>
                <form action="/shareNotes" method="POST">
                    <label style='color:black' class="text-center"> Recipient Email Address </label>
                    <input type="email" class="form-control" placeholder="Please enter recipient email!" name="email"></input>

                    <label style='color:black' class="text-center"> Note Subject </label>
                    <input type="text" class="form-control" placeholder="Please enter subject!" name="subject"></input>

                    <label style='color:black' class="text-center"> Note Body </label></br>
                    <textarea class='col-md-12 mx-auto d-block' name="email" name="message" placeholder="Body" required rows="10"></textarea></br>
                    <input class="btn btn-success" type="submit" style="margin-top: 1px; margin-bottom: 15px; margin-right: 10px;" value="Send" name="message">
                </form>
            </div>
        </div>
    </div>
</body>
</html>
{% endblock %}
```
routes.py
```python
@myapp_obj.route('/shareNotes', methods=['GET', 'POST'])
def shareNotes():
    title = 'Share Note'
    if  request.method == "POST":
        try:
            email = str(request.form['email'])
            subject = str(request.form['subject'])
            msg_body = str(request.form['message'])

            message = Message(subject, sender="jimin.song.software@gmail.com", recipients=[email])
            message.body = msg_body
            mail.send(message)
            flash("Email Sent!")
            return redirect('/')

        except ConnectionRefusedError as connectionRefusedError_:
            return "Failed to send Email. Please try again later!"
    else:
        return render_template("shareNote.html",title=title)
```
