# InputOutputFlashCards

### InputOutputFlashCards Function

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

We can input a term with a definition

flashcards.html

```html
{% extends "base.html" %}

{% block content %}
    <section>
        <div class="flashc_container">
            <div id="create_card">
                <h2>Create Flashcard</h2>

                <label for="question">Term</label>
                <textarea id="question" maxlength="200"></textarea>
                <label for="answer" maxlength="500">Definition</label>
                <br>
                <textarea id="answer"></textarea>

                <button id="save_card" class="flashc_btn">Add Card</button>
                <button id="delete" class="flashc_btn">Delete All</button>
            </div>
        </div>
    </section>

    <section>
        <div class="flashc_container">
            <div id="flashcards"></div>
        </div>
    </section>

    <script src="{{ url_for('static', filename='flashc.js') }}"></script>
{% endblock %}

```

This is what creates the flashcard with buttons and textbox that can be used to create the flashcards

flashc.js

```Javascript
var contentArray = localStorage.getItem('items') ? JSON.parse(localStorage.getItem('items')) : [];

document.getElementById("save_card").addEventListener("click", () => {
  addFlashcard();
});
document.getElementById("delete").addEventListener("click", () => {
    localStorage.clear();
    flashcards.innerHTML = '';
    contentArray = [];
});



flashcardMaker = (text) => {
  const flashcard = document.createElement("div");
  const question = document.createElement('h2');
  const answer = document.createElement('h2');

  flashcard.className = 'flashcard';

  question.setAttribute("style", "border-top:1px solid red; padding: 15px; margin-top:30px");
  question.textContent = text.my_question;

  answer.setAttribute("style", "text-align:center; display:none; color:orangered");
  answer.textContent = text.my_answer;

  flashcard.appendChild(question);
  flashcard.appendChild(answer);

  flashcard.addEventListener("click", () => {
    if(answer.style.display == "none")
      answer.style.display = "block";
    else
      answer.style.display = "none";
  })

  document.querySelector("#flashcards").appendChild(flashcard);
}

contentArray.forEach(flashcardMaker);

addFlashcard = () => {
  const question = document.querySelector("#question");
  const answer   = document.querySelector("#answer");

  let flashcard_info = {
    'my_question' : question.value,
    'my_answer'   : answer.value
  }
  if (flashcard_info['my_question'] && flashcard_info['my_answer']) {
    contentArray.push(flashcard_info);
    localStorage.setItem('items', JSON.stringify(contentArray));
    flashcardMaker(contentArray[contentArray.length - 1]);
    question.value = "";
    answer.value   = "";
  }
  
}

```

routes.py

```python
@myapp_obj.route('/renderFlashCard')
def flashcards():
    title = 'Flashcards'
    return render_template("flashcards.html", title = title)
```

This is the the box of the flashcard and how they look

style.css

```css
.flashc_btn {
  padding: 8px;
  cursor: pointer;
  border: 1px solid lightgray;
  border-radius: 5px;
  background: aquamarine;
}

.flashc_btn:hover {
  background-color: orangered;
}

.flashc_container {
  width: 1000px;
  margin: auto;
}

#create_card {
  width: 370px;
  margin: auto;
  padding: 20px;
  margin-top: 10px;
  background: whitesmoke;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.9);
}

#create_card h2 {
  color: black;
  text-align: center;
}

#create_card textarea {
  width: 100%;
  border-radius: 5px;
  font-family: inherit;
  border: 1px solid lightgray;
}

#create_card button {
  width: fit-content;
}

#flashcards {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  width: 100%;
  margin: auto;
  margin-top: 10px;
  padding: 0px 10px;
}

.flashcard {
  width: 370px;
  height: 200px;
  word-wrap: break-word;
  margin: 10px;
  background: #fff;
  cursor: pointer;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.9);
}
```
