# Track Hour Page

### Track Hour Function

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

We track the amount of time when user click on start time

trackHour.html
```html
<h1>Track Hour</h1>
<div class="pomodoroTimer_container">
    <p id="work" class="label">Time:</p>

    <!--Timer-->
    <div id="work-timer" class="pomodoroTimer">
        <p id="w_hours">00</p>
        <p class="semicolon">:</p>
        <p id="w_minutes">00</p>
        <p class="semicolon">:</p>
        <p id="w_seconds">00</p>
    </div>

    <button id="start" class="btn">Start</button>
    <button id="stop"  class="btn">Pause</button>
    <button id="reset" class="btn">Reset</button>
</div>
<script src="{{ url_for('static', filename='trackHour.js') }}"></script>
```
The time will add 1 second after user click start time, user can also pause and reset the time.
```Javascript
trackHour.js
var start = document.getElementById('start');
var stop  = document.getElementById('stop');
var reset = document.getElementById('reset');

var wh = document.getElementById('w_hours');
var wm = document.getElementById('w_minutes');
var ws = document.getElementById('w_seconds');



//store a reference to a timer variable
var startTimer;

start.addEventListener('click', function(){

    //startTimer = setInterval(timer, 1000)
    if(startTimer === undefined){
        startTimer = setInterval(timer, 1000)
    } else {
        alert("Timer is already running, Press Ok to continue");
    }
})

reset.addEventListener('click', function(){
    wh.innerText = "00";
    wm.innerText = "00";
    ws.innerText = "00";

    stopInterval()
    startTimer = undefined;
})

stop.addEventListener('click', function(){
    stopInterval()
    startTimer = undefined;
})


//Start Timer Function
function timer(){
    //Work Timer Countdown
    ws.innerText++;

    if (ws.innerText == 60)
    {
        ws.innerText = 00;
        wm.innerText++;
    }
    else if (wm.innerText == 60)
    {
        wm.innerText = 00;
        wh.innerText++;
    }

}

//Stop Timer Function
function stopInterval()
{
    clearInterval(startTimer);
}
```

style.css (trackHour part)
```css
.pomodoroTimer_container {
  height: 200px;
  width: 500px;
  margin-left: 20px;
  border: 4px solid black;
  background-color: aquamarine;

  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(3, 1fr);
}

/*timers*/
.label {
  align-self: center;
  justify-self: center;
  font-family: "Times New Roman", serif;
  font-size: 30px;
  font-weight: bold;
}

#work {
  grid-area: 1 / 2 / 1 / 2;
}
#break {
  grid-area: 1 / 4 / 1 / 4;
}

.pomodoroTimer {
  display: flex;
  align-self: center;
  justify-self: center;

  font-size: 30px;
  font-weight: bold;
}

p {
  margin: 0;
  padding: 0;
}

#work-timer {
  grid-area: 2 / 2 / 2 / 2;
}

#break-timer {
  grid-area: 2 / 4 / 2 / 4;
}

/*buttons*/

.btn {
  align-self: center;
  justify-self: center;

  width: 80px;
  height: 30px;
  font-size: 20px;
}

#start {
  grid-area: 3 / 2 / 3 / 2;
}

#reset {
  grid-area: 3 / 3 / 3 / 3;
}

#stop {
  grid-area: 3 / 4 / 3 / 4;
}
```
