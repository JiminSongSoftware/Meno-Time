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



#### IV) Use Case Description

 

###### **1) InputOutputFlashCards:**

- Summary: Create a randomly generated set of flash cards based on optional input attributes.
- Actors: customer (Student).
- Preconditions: The customer has to input the values.
- Triggers: Customer chooses flashcard activity
- Primary Sequence:
  1) Customer inputs keywords related to desired flashcards.
  2) Customer inputs desired number of flashcards.
- Primary Postconditions:
  1) Customer gets a set of flashcards of desired quantity and related to keywords.
- Alternate Sequences: The customer inputs nothing.
- Alternate Trigger:
- Alternate Postconditions: Customer gets an infinitely long set of random flashcards



###### **2) shareFlashCards:**

- Summary: Share Flashcards to different users
- Actors: customer (Student).
- Preconditions: 
- Triggers: Customer chooses to share.
- Primary Sequence:
  1) Customer chooses flashcard(s) to share.
  2) Customer chooses user(s) to share to.
- Primary Postconditions:
  1) The customer sends chosen flashcards to chosen users.
- Alternate Sequences: 
- Alternate Trigger:
- Alternate Postconditions: 



###### **3) renderNotes:**

- Summary: render Notes for customer.
- Actors: customer (Student).
- Preconditions: 
- Triggers: Customer chooses to view notes.
- Primary Sequence:
  1) Customer selects Notes to render.
- Primary Postconditions:
  1) The customer has view of Notes.
- Alternate Sequences: 
- Alternate Trigger:
- Alternate Postconditions: 



###### **4) ConvertPDF:**

- Summary: convert file to PDF.
- Actors: customer (Student).
- Preconditions: 
- Triggers: Customer chooses to view notes.
- Primary Sequence:
  1) Customer chooses to convert a file to PDF.
- Primary Postconditions:
  1) Customer gets PDF file.
- Alternate Sequences: 
- Alternate Trigger:
- Alternate Postconditions: 



###### **5) shareNotes:**

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



###### **6) timeBlocks:**

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



###### **7) pomodoroTimer:**

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



###### **8) mindMap:**

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





###### **9) changeOrder:**

- Summary: Change order of flash cards based on how often the customer got answer correct
- Actors: customer

- Preconditions: The customer has to take a quiz, then the most frequently correct one will be send to the bottom.
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



###### **10) findText:**

- Summary: searching for a specific text on a file.
- Actors: customer

- Preconditions: The customer has to click on a icon of searching text.
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



###### **11) renameRegular:**

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



###### **12) createGraph:**

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



###### **13) trackHour:**

- Summary: Tracks the amount of hours of work the user has done each day.
- Actors: User(student)
- Preconditions: Student logs in to their account.
- Triggers:  When signed in and select study options.
- Primary Sequence:
  1) User selects study option they want to do.
  2) The system will track the amount of hours they do.
  3) System tracks and shows the amount of hours user has done.
  4) User close apps.
- Primary Postconditions:
  1) User can see hours they have done each day.
- Alternate Sequences: The user enters in a wrong account or the user does not log in. That means the system can not track the hours done for the account.
- Alternate Trigger: That the user is signed in guest mode and does their studying.
- Alternate Postconditions: the hours of the user are not tracked. That means the student can not see the hours they spent each day.



###### **14) toDo:**

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



###### **15) visualizeHours:**

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





#### V) Non-functional Requirements

- The system displays message in either English or Korean

- Every requests must be processed within 10s

- Show error message when user faces an error

