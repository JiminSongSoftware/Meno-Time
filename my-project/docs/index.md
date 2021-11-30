# Welcome to Meno-Time

For full source code visit [github.com](https://github.com/nguyenbo7/Team11_project).
##Installation
In order to view the mkdocs, you need to type these commands in the terminal
```bash
pip install mkdocs
```
Create a new project and direct to the repository
```bash
mkdocs new my-project
cd my-project
```
Run this command
```bash
mkdocs serve
```
You will get a link prompted, then direct to that link
the link will look like this http://127.0.0.1:8000/

Now you are ready to see our projects in mkdocs.

##Other requirements
After downloading our repo, run below command to install all required modules.

```bash
pip install -r /path/to/requirements.txt
```

How to Run
```bash
python3 run.py
```

## Project layout
```python
.
├── README.md
├── Specification.md
├── gantt.xlsx
├── my-project
│   ├── docs
│   │   ├── delete.md
│   │   ├── index.md
│   │   ├── inputOutputFlashCards.md
│   │   ├── login.md
│   │   ├── pomodorotimer.md
│   │   ├── register.md
│   │   ├── renderNotes.md
│   │   ├── shareFlashcards.md
│   │   ├── shareNotes.md
│   │   ├── todolist.md
│   │   ├── trackHour.md
│   │   └── trackHours.md
│   └── mkdocs.yml
├── myapp
│   ├── __init__.py
│   ├── flashcards
│   ├── forms.py
│   ├── models.py
│   ├── notes
│   │   └── README.md
│   ├── routes.py
│   ├── static
│   │   ├── flashc.js
│   │   ├── pomodoroTimer.js
│   │   ├── style.css
│   │   └── trackHour.js
│   └── templates
│       ├── base.html
│       ├── flashcards.html
│       ├── hello.html
│       ├── loggedin.html
│       ├── login.html
│       ├── logout.html
│       ├── note.html
│       ├── notes.html
│       ├── pomodoroTimer.html
│       ├── register.html
│       ├── shareFlashcards.html
│       ├── shareNote.html
│       ├── todolist.html
│       └── trackHour.html
├── requirements.txt
└── run.py
```

Our Home HTML Page
```html
<!DOCTYPE html>
<html>     
  <head>
   {% if title %}
    <title>{{ title }}!</title>
    {% else %}
     <title >No Name </title>
     {% endif %}
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
     <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
   </head>
  <body style="background-color: bisque;">
   <style>
     h1,h2,h3 {
       font-family: 'Times New Roman', serif;
     }
     </style>
   <audio id="over_music">
     <source src="{{ url_for('static', filename='beepbeep.mp3') }}">
   </audio>
   <div>
      <a href="/register">Register</a>
      <a href="/delete">Delete your Account</a>
      <h1>Meno-Time</h1>
      <div>
      </div>
      <div>
      <a href="/">Home</a>
      </div>
      <a href="/login">Login</a>
      <a href="/logout">Logout</a>
    </div>
    <div>
     <a href="/renderFlashCard">Flash Cards</a>
    </div>
    <div>
     <a href="/shareFlash">Share Flash Cards</a>
    </div>
    <div>
     <a href="/notes">Notes</a>
    </div>
    <div>
     <a href="/shareNotes">Share Notes</a>
    </div>
    <div>
     <a href="/todolist">To-Do</a>
    </div>
    <div>
     <a href="/pomodoroTimer">Pomodoro Timer</a>
    </div>
    <div>
     <a href="/trackHours">Track Hours</a>
    </div>

    {% with messages = get_flashed_messages() %}
    {% if messages %}
    <ul>
      {% for m in messages %}
      <li>{{ m }}</li>
      {% endfor %}
   </ul>
   {% endif %}
   {% endwith %}
       {% block content %}
 {% endblock %}	 
 </body>
</html>
```
