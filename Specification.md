# **Team 11 Study App Project**

**Date:**  9/16/2021

**Product Name:**  Meno-Time

**Problem Statement:** A smart and entertaining way to study



#### I ) URL GitHub link:

https://github.com/nguyenbo7/Team11_project.git



#### II ) Team Members:

Jimin Song:	https://github.com/JimSongTheGreatest

Jimmy Phan:  https://github.com/PhannJimmy

Nguyen Chau:	 https://github.com/nguyenbo7

Rogelio Ibarra:	https://github.com/Rogelio-42


#### III)Main Use Cases:
1) Login 
2) Signup/Register

#### III) Use cases name:

1) InputOutputFlashCards

2) shareFlashCards

3) renderNotes

4) ConvertPdf

5) shareNotes

6) timeBlocks

7) pomodoroTimer

8) mindMap

9) changeOrder

10) findText

11) renameRegular

12) createGraph

13) trackHour

14) toDo

15) visualizeHour

16) deleteAccount


#### IV) Use Case Description

#### Main Use Cases:

###### 1) Signup/Register:**

- Summary: 
- Actors: User (Students)
- Preconditions: User is on sign up page 
- Triggers: The user clicks on the signup/register option
- Primary Sequence:
  1) When user clicks on signup/register option they are redirected to a page to create an account
  2) The user enters in information that is required like username and a password
  3) After filling in information user clicks on create account
- Primary Postconditions:
  1) User account is created then they will be redirected back to the login page
  2) A flash message will appear at the top saying "you are registered or account created"
- Alternate Sequences: 
- Alternate Trigger:
- Alternate Postconditions: 

###### 2) Login/Sign out:**

- Summary: A login funciton for the user to login into their Account so they do not do things in guest mode
- Actors: User (Student)
- Preconditions: 
  1) User must have made an account that is currently an existing account
  2) User clicks on Login feature to get redirected to the login page
  3) User types in their information and clicks login. Whiled logged in their account they have the option to log out
- Triggers: The user would have to click the login feature to login their account or log out feature to log out their account
- Primary Sequence:
  1) User clicks on login 
  2) They are redirected to the login page
  3) User enters information that they used to create their account to login
  4) User clicks login.
- Primary Postconditions:
  After logging in user is redirected to home page to access all the features provided. 
- Alternate Sequences: 
  User has option to sign out at the top if they wanted to. 
- Alternate Trigger: User clicks on sign out option 
- Alternate Postconditions: User is then redirected to Home page. 


 ###### **3) InputOutputFlashCards:**

- Summary: Create a randomly generated set of flash cards based on optional input attributes.
- Actors: User (Student).
- Preconditions: The customer has to login to their account to do the feature 
- Triggers: Customer chooses flashcard activity
- Primary Sequence:
  1) Customer inputs keywords related to desired flashcards.
  2) Customer inputs desired number of flashcards.
- Primary Postconditions:
  1) Customer gets a set of flashcards of desired quantity and related to keywords.
- Alternate Sequences: The flashcard set will show nothing.
- Alternate Trigger: The customer inputs nothing.
- Alternate Postconditions: Customer gets an infinitely long set of random flashcards

###### **4) deleteFlashcards:**

- Summary: Allows the user to be able to delete their flashcards so that they can add more. 
- Actors: User(student)

- Preconditions: Student must have an account and created flashcards
- Triggers:  User now can select the delete flashcard options to delete their flashcards. 
- Primary Sequence:
  1) If user is logged in and have created flashcards set
  2) They now have the option to delete all their flashcards to create new ones
- Primary Postconditions:
  1) With their flashcards deleted it becomes an empty canvas 
  2) With an empty canvas they can now add more flashcards that the use would like to add. 
- Alternate Sequences: User does not have any flashcards created 
- Alternate Trigger: The delete option would not work because no flashcards are there to be able to delete. 
- Alternate Postconditions: If no flashcards set are created then there should not be anything to be able to delete so the delete option would not work. 



###### **5) shareFlashCards:**

- Summary: Share Flashcards to different users
- Actors: customer (Student).
- Preconditions: While logged into their account user can share their flashcards that they have created with other users by emailing them. 
- Triggers: Customer chooses to share.
- Primary Sequence:
  1) Customer chooses the shareFlashcard feature 
  2) Customer chooses user by email to send to
  3) User sends the email to share their flash cards they have created. 
- Primary Postconditions:
  1) The customer sends chosen flashcards to chosen users by email. 
- Alternate Sequences: Then they will not be able to share their flashcards that they have created. 
- Alternate Trigger: That email does not exist 
- Alternate Postconditions: With the email not existing they cannot send it to that person. 



###### **6) renderNotes:**

- Summary: render/upload markdown file that turns into Notes for customer.
- Actors: User (Student).
- Preconditions: 
  User is signed into an account
- Triggers: Customer chooses to view notes.
- Primary Sequence:
  1) User clicks on notes feature
  2) This will send them to a page where they can send notes 
  3) User browses their markdown file notes to upload
  4) Then click upload
- Primary Postconditions:
  1) After notes are uploaded the user can see their notes right under the upload notes option
  2) User can click on their notes and can see what was inside those notes.
- Alternate Sequences: Nothing will be shown or uploaded at all it will be empty
- Alternate Trigger: User uploads nothing
- Alternate Postconditions: No notes to click on because nothing was uploaded. 

###### **7) shareNotes:**

- Summary: help user share notes along other user in the program or share externally.
- Actors: customer (Student).
- Preconditions: Users are logged in their accounts.
- Triggers: After signing in, user clicks the shareNotes box.
- Primary Sequence:
  1) User selects option for sharing notes.
  2) User selects objects they want to share.
  3) The system will show whether user wants to share internally or externally.
  4) Users click x box to close shareNotes feature.
- Primary Postconditions:
  1) Users will be notified upon successful attempt to share.
- Alternate Sequences: Users are not logged in -> will bring up guide message to log in.
- Alternate Trigger: Users will have option for login in as a guest and have study mode.
- Alternate Postconditions: Users will be notified upon completion of log-in or guest-log-in.


###### **8) pomodoroTimer:**

- Summary: enable user to track the time and use their time effectively and efficiently.
- Actors: customer (Student).
- Preconditions: Users are logged in their accounts.
- Triggers: User clicks pomodoroTimer box to enable 30 mins timer.
- Primary Sequence:
  1) Once the user clicks the Timer box, it will show options of time duration.
  2) Once user clicks time duration (30 mins, 1 hour).
  3)  Upon activation, the time will run and will alarm user at the end of the timer..
- Primary Postconditions:
  1)  Users input the duration they want to study with timer.
  2) Shows the time remaining.
- Alternate Sequences: User does not enter the time duration in. If no input for the duration is typed, then it will automatically run on 30 mins option.
- Alternate Trigger: N/A.
- Alternate Postconditions: Timers will not run. User will not be able to use timer to study with..


###### **9) trackHour:**

- Summary: Tracks the amount of hours of work the user has done each day.
- Actors: User(student)
- Preconditions: Student logs in to their account.
- Triggers:  When signed in and select track hour feature
- Primary Sequence:
  1) User is signed in and can access the track hour feature
  2) When moved to the track hour page there is a timer that will go like a stop watch
  3) The timer will go on and the student can track how long they have done work and studied.
- Primary Postconditions:
  1) User can see hours they of how long they been studying for. 
- Alternate Sequences: The user enters in a wrong account or the user does not log in. That means the system can not track the hours done for the account.
- Alternate Trigger: That the user is signed in guest mode and does their studying.
- Alternate Postconditions: the hours of the user are not tracked. That means the student can not see the hours they spent each day.


###### **10) toDo:**

- Summary: A todo list for the student that they created or suggested so the student knows what they should focus on that day and days after.
- Actors: User(student)
- Preconditions: Student logs in to their account.
- Triggers:  Once signed in onto the app todo list is shown first to give the student what to focus on.
- Primary Sequence:
  1) Once the user is signed in the system prompts the toDo list.
  2) With the toDo list shown user can select what they want to focus on.
  3) With selected topics chosen the system can help the user give the topic they want to focus on.
  4) Once finished the user can add more onto the toDo list.
  5) User logs out.
- Primary Postconditions:
  1) When the todo is shown the user has what they can select from the todo list.
  2) With what is selected it helps the user what they should focus on.
- Alternate Sequences: The user does not enter a todo list. With no todo list the system does not know what the user wants to focus on.
- Alternate Trigger: N/A.
- Alternate Postconditions: (No todo list is shown) User wouldn't know what they should focus on for that day.

###### **11) editToDoList:**

- Summary: Allows the user to be able to edit their ToDo list by removing things they did not do or edit the list they listed.

- Preconditions: Student must be logged in and have a ToDo list created. 
- Triggers:  User selects edit option to then be able to edit their ToDo list.
- Primary Sequence:
  1) If user has created an existing account
  2) They can then make a ToDo list
  3) After making their ToDo list the user can now edit it. 
- Primary Postconditions:
  1) The users can edit their todo list so that they made a mistake on it. It is now fixed 
  2) Now the user has a updated ToDo list. 
- Alternate Sequences: User does not have a ToDo list so their is nothing to edit.
- Alternate Trigger: They try to edit their todo list but with nothing added for them ToDo they can not edit anything.
- Alternate Postconditions: Will not have a edited todo list with no ToDo list ever created. 

###### **12) deleteToDoList:**

- Summary: Allows the user to delete things off their ToDo list. 
- Actors: User(student)

- Preconditions: Student must be logged in and have a ToDo list created. 
- Triggers:  User can select delete option which can delete some of the users things that they listed. 
- Primary Sequence:
  1) If user has created an existing account
  2) They can then make a ToDo list
  3) If something on their list is not what they want they can delete it as an option.
- Primary Postconditions:
  1) When a user created a mistake in their ToDo list they can not click the delete option 
  2) Then when deleted the list is now off the ToDo list. 
- Alternate Sequences: User does not have a ToDo list so they can not delete anything off the todo list
- Alternate Trigger: When clicking on the delete option for the ToDo list with nothing listed nothing will be deleted. 
- Alternate Postconditions: Will not have anything deleted off their todo list with no ToDo list ever created.

###### **13) visualizeHours:**

- Summary: show the hours needed to work on that day and show the work done for the work needed.
- Actors: User(student)

- Preconditions: Student logs in to their account.
- Triggers:   User inputs how many hours they want to work and the work/project they need to do.
- Primary Sequence:
  1) Once the user inputs the work they have and what they have to do they can set the amount of hours they want to work.
  2) Then the system processes that input from the user.
  3) Then blocks them in and shows them like a calendar what they should do and the amount of hours to work.
- Primary Postconditions:
  1) Then the system can process and block the schedule for the user.
  2) Shows the hours the user will have to do.
- Alternate Sequences: User does not enter anything in. No schedule is blocked and cannot see the amount of hours visualize.
- Alternate Trigger: N/A.
- Alternate Postconditions: No hours and work are shown. User will not be able to visualize the hours and see the amount of work they have to do each day.


###### **14) deleteAccount:**

- Summary: Allows the user to be able to delete their account from our website.
- Actors: User(student)

- Preconditions: Student must have an account
- Triggers:  User can select delete account option to delete their account
- Primary Sequence:
  1) If user has created an existing account
  2) They have the option to delete their account
- Primary Postconditions:
  1) Then their account will be deleted from the system.
- Alternate Sequences: User does not have an account so there wont be an account to delete.
- Alternate Trigger: N/A.
- Alternate Postconditions: Will not have an account to delete if there is not an account that exists. 


#### V) Non-functional Requirements

- The system displays message in either English or Korean

- Every requests must be processed within 10s

- Show error message when user faces an error

