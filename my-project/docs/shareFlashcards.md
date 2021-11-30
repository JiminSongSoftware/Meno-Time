# Share Flash Cards Page

### Share Flash Cards Function

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

shareFlashcards.html
```html
{% extends "base.html" %}

{% block content %}
<!DOCTYPE html>
<body>
    <div class="text-left mx-auto d-block">
        <div class="col-md-12 mx-auto d-block">
            <div class="card-body col-md-8 mx-auto d-block">
                <h3 style='color:black' class="card-title text-left">Share FlashCard</h3>
                <form action="/shareFlash" method="POST">
                    <label style='color:black' class="text-center"> Recipient Email Address </label>
                    <input type="email" class="form-control" placeholder="Please enter recipient email!" name="email"></input>

                    <label style='color:black' class="text-center"> Flashcard Subject </label>

                    <input type="text" class="form-control" placeholder="Please enter subject!" name="subject"></input>

                    <label style='color:black' class="text-center"> Flashcard Question </label>

                    <textarea class='col-md-12 mx-auto d-block' name="email" name="message" placeholder="Question" required rows="4"></textarea>

                    <label style='color:black' class="text-center"> Flashcard Answer </label>
                    <textarea class='col-md-12 mx-auto d-block' name="email" name="message" placeholder="Answer" required rows="4"></textarea>

                    <input class="btn btn-success" type="submit" style="margin-top: 1px; margin-bottom: 10px; margin-right: 10px;" value="Send" name="message">
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
@myapp_obj.route('/shareFlash', methods=['GET', 'POST'])
def shareFlash():
    title = 'Share Flash'
    if  request.method == "POST":
        try:
            email = str(request.form['email'])
            subject = str(request.form['subject'])
            msg_ans = str(request.form['message'])
            msg_body = str(request.form['message'])

            message = Message(subject, sender="jimin.song.software@gmail.com", recipients=[email])
            message.body = msg_body
            mail.send(message)
            flash("Email Sent!")
            return redirect('/')

        except ConnectionRefusedError as connectionRefusedError_:
            return "Failed to send Email. Please try again later!"
    else:
        return render_template("shareFlashcards.html",title=title)
```
