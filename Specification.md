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



###### **4) shareFlashCards:**

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
- Alternate Postconditions: 



###### **5) renderNotes:**

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


###### **6) ConvertPDF:**

- Summary: Converts notes to pdf
- Actors: User (Student)
- Preconditions:
  1) User has notes that are uploaded. 
- Triggers: Users chooses notestopdf
- Primary Sequence:
  1) User has notes to choose from 
  2) User chooses a note to convert the file to PDF.
- Primary Postconditions:
  1) Note that user chose is converted to pdf
  2) User gets pdf file of note
- Alternate Sequences: If there is nothing uploaded then their will be nothing to be converted
- Alternate Trigger: No note is converted if there is not a note uploaded
- Alternate Postconditions: 



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



###### **8) timeBlocks:**

- Summary: use Markdown blocks to add text to the program with the Markdown language. Markdown blocks support lists, links, bolded and italicized text, and block quotes.
- Actors: customer (Student).
- Preconditions: Users are logged in their accounts.
- Triggers: Once logged in, users will see option for creating markdown blocks to add text to the program.
- Primary Sequence:
  1) Once the user is signed in the system prompts the markdown blocks box.
  2) With the blocks, shown user can type in text to the program.
  3) Users will be able to type in links, bolded and italicized texts.
  4) Once finished user will be able to click save button and post.
- Primary Postconditions:
  1) When the markdown block option is showing, user will have to click the box to enable the feature.
  2) With what is selected, the feature will help user save notes and share notes.
- Alternate Sequences: The user does not click save button. If the user does not save, it will show guide message to save or discard.
- Alternate Trigger: N/A.
- Alternate Postconditions: Users will be able to see that they have saved the notes.



###### **9) pomodoroTimer:**

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



###### **10) mindMap:**

- Summary: A broad view of the entire object to show the relationships among pieces.
- Actors: customer (Student).

- Preconditions: The customer has to input the values.
- Triggers: Customer select the option of the overview of some specific topic.
- Primary Sequence:
  1) The customer has to input the central idea (starting point, or the root).
  2) Add the branches to the central idea.
  3) Continue to input smaller branches as desired.
  4) The customer can edit like adding keywords or changing the color of the branch.
- Primary Postconditions:
  1) The customer has an overview of the subject.
  2) Recognize the relationship between branches.
- Alternate Sequences: The customer enter only 1 input (cannot show the relationship to others)
- Alternate Trigger: The system shows a message that requires customer to input more values.
- Alternate Postconditions:





###### **11) changeOrder:**

- Summary: Change order of flash cards based on how often the customer got answer correct
- Actors: customer
- Preconditions: The customer is to login and have a flashcard set which they will have to take a quiz, then the most frequently correct one will be send to the bottom.
- Triggers: Customer select the option of reviewing the incorrect answers.
- Primary Sequence:
  1) The customer has to take a quiz.
  2) Incorrect answers would be repeated more frequently and place on the top.
  3) The order continues to be changed until all answers are correct.
- Primary Postconditions:
  1) The customer has an idea of what need to review more.
- Alternate Sequences: none
- Alternate Trigger: none.
- Alternate Postconditions: none



###### **12) findText:**

- Summary: searching for a specific text on a file.
- Actors: customer
- Preconditions: User has to be signed in and have notes uploaded. 
- Triggers: Customer enters a text that needed to be searched
- Primary Sequence:
  1) Click on the search text icon
  2) Enter a text
  3) Click on upward or downward arrow to show the replicated text at different positions.
- Primary Postconditions:
  1) The customer can see the place of the words that they looking for
- Alternate Sequences: No text is not appear.
- Alternate Trigger: required another input or just click X to close the searching icon.
- Alternate Postconditions: none



###### **13) renameRegular:**

- Summary: rename a file by using regular expression.
- Actors: customer

- Preconditions: The customer has to on the 3 dots on the file to edit it.
- Triggers: Customer click on rename a file
- Primary Sequence:
  1) Click 3 dots to edit a file (find a file faster by using findText)
  2) Click on rename a file
  3) Click OK or Cancel to accept the change.
- Primary Postconditions:
  1) The customer can change a name of a file as they want
- Alternate Sequences: The new name is already exists.
- Alternate Trigger: required a different name for the file.
- Alternate Postconditions: none



###### **14) createGraph:**

- Summary: show visual relationships between subjects by different type of graph.
- Actors: customer
- Preconditions: The customer has to an option graphing
- Triggers: Customer click on the type of graph
- Primary Sequence:
  1) Choose a graph option
  2) Choose a type of graph
  3) Input the values, then connect the nodes or edges as desired
- Primary Postconditions:
  1) The customer can have a better view on a graph
- Alternate Sequences: none
- Alternate Trigger: none
- Alternate Postconditions: none



###### **15) trackHour:**

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



###### **16) toDo:**

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



###### **17) visualizeHours:**

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


###### **18) deleteAccount:**

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

