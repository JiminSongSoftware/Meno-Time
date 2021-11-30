# Pomodoro Timer Page

### Pomodoro Timer Function

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

pomodoroTimer.html
We create a countdown to count the time from 25 min back to zero
User can reset the time, and pausse the time
Every 25 min of working, user will have 5 min break.

    <h1>Pomodoro Timer</h1>

    <div class="pomodoroTimer_container">
        <p id="work" class="label">Time:</p>
        <p id="break" class="label">Break:</p>

        <!--Work Timer-->
        <div id="work-timer" class="pomodoroTimer">
            <p id="w_minutes">25</p>
            <p class="semicolon">:</p>
            <p id="w_seconds">00</p>
        </div>

        <!--Break Timer-->
        <div id="break-timer" class="pomodoroTimer">
            <p id="b_minutes">05</p>
            <p class="semicolon">:</p>
            <p id="b_seconds">00</p>
        </div>

        <button id="start" class="btn">Start</button>
        <button id="stop"  class="btn">Pause</button>
        <button id="reset" class="btn">Reset</button>
    </div>
    
    pomodoroTimer.js
    The logic 
    
var start = document.getElementById('start');
var stop  = document.getElementById('stop');
var reset = document.getElementById('reset');

var wm = document.getElementById('w_minutes');
var ws = document.getElementById('w_seconds');

var bm = document.getElementById('b_minutes');
var bs = document.getElementById('b_seconds');

//store a reference to a timer variable
var startTimer;

start.addEventListener('click', function(){
    if(startTimer === undefined){
        startTimer = setInterval(timer, 1000)
    } else {
        alert("Timer is already running, Press Ok to continue");
    }
})

reset.addEventListener('click', function(){
    wm.innerText = 25;
    ws.innerText = "00";

    bm.innerText = 5;
    bs.innerText = "00";

    document.getElementById('counter').innerText = 0;
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
    if(ws.innerText != 0){
        ws.innerText--;
    } else if(wm.innerText != 0 && ws.innerText == 0){
        ws.innerText = 59;
        wm.innerText--;
    }

    //Break Timer Countdown
    if(wm.innerText == 0 && ws.innerText == 0){
        if(bs.innerText != 0){
            bs.innerText--;
        } else if(bm.innerText != 0 && bs.innerText == 0){
            bs.innerText = 59;
            bm.innerText--;
        }
    }
}

//Stop Timer Function
function stopInterval(){
    clearInterval(startTimer);
}
