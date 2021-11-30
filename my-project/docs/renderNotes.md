# Render Note Page

### Render Note Function

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

notes.html
```html
{% extends "base.html" %}

{% block content %}
<h1>Note</h1>
<p>Upload your note! We will organize them for you!</p>
<p>------------------------------------</p>
<p>*Only md files are allowed to upload*</p>
<p>------------------------------------</p>
<form method="POST" novalidate enctype="multipart/form-data">
        {{ form.hidden_tag() }}
        {% if form.file.errors %}
        <ul class="errors">
                {% for error in form.file.errors %}
                <li>{{ error }}</li>
                {% endfor %}
        </ul>
        {% endif %}
        <p> {{ form.file }} </p>
        <p>------------------------------------</p>
        <p> {{ form.submit() }} </p>
        <p>------------------------------------</p>
</form>
<h2> {{title}} </h2>
<ul>
        {% for note_title in note_titles %}
        <li>
                <a href="{{ url_for('show_note', title=note_title) }}">
                        {{ note_title }}
                </a>
        </li>
        {% endfor %}
</ul>
{% endblock %}
```
note.html
```html
{% extends "base.html" %}

{% block content %}
<h1>Viewing Note</h1>
{{ note|safe }}
<a href="/notes">-----------Navigate Back to Upload Note-----------</a>
{% endblock %}
```
routes.py
```python
@myapp_obj.route('/notes', methods=['GET', 'POST'])
def upload_note():
    title='Note Lists'

    form = FileForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            basedir, 'notes', filename
        ))
        flash('-----Note uploaded successfully-----')

    filenames = os.listdir(os.path.join(basedir, 'notes'))
    note_titles = list(sorted(re.sub(r"\.md$", "", filename)
        for filename in filenames if filename.endswith(".md")))

    return render_template('notes.html',
        form=form,
        title=title,
        note_titles=note_titles,
    )

@myapp_obj.route('/note/<title>')
def show_note(title):
    filenames = os.listdir(os.path.join(basedir, 'notes'))
    note_titles = list(sorted(re.sub(r"\.md$", "", filename)
        for filename in filenames if filename.endswith(".md")))

    if title in note_titles:
        with open(os.path.join(f"{basedir}/notes/{title}.md"), 'r') as f:
            text = f.read()
            return render_template('note.html',
                note=markdown.markdown(text),
                title=title)
    return redirect('/')
```
