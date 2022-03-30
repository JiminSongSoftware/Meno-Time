# Delete Page

### Delete Function

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

routes.py
```python
@application.route("/delete",)
def delete():
    user = User.query.filter_by(id=1).delete()
    db.session.commit()
    flash('Your account is deleted', 'error')
    return redirect("/register")
```
