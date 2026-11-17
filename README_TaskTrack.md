# Overview

TaskTrack is a web-based task management application designed to help users stay organized and keep track of their daily responsibilities. The idea behind the application is to provide a simple way to manage tasks without all the extra features and complexity that come with larger project management tools. Users can easily add tasks, view what they need to get done, mark tasks as completed, and delete tasks they no longer need.

The application is intended for students, working professionals, or anyone who wants an easy way to manage their personal to-do lists. Users can create an account and log in to manage their own tasks, keeping their information separate from other users. Each task includes a title and an optional description, giving users the flexibility to add as much or as little detail as they need. As tasks are finished, users can mark them as completed to keep track of their progress.

# Design (Sprint 1)

## User Stories

Describe the **user stories** for the project, which are short, simple descriptions of a feature told from the perspective of the end user. Each **user story** should include clear **acceptance criteria** and a **point estimate**. The **user stories** must align with the **use case diagram** and should be labeled as US#1, US#2, and so on. We suggest creating a separate Markdown section for each **user story**. 

Use the following template when writing your **user stories**. 

## US1: Register Account - 3 Story Points (Sprint 2)

As a new user, I want to create an account so that I can securely manage my personal tasks.

Given that I am a new user, when I enter a valid username and password, then the application creates my account and allows me to log in.


## US2: Log In - 3 Story Points (Sprint 2)

As a registered user, I want to log in to my account so that I can access and manage my personal tasks.

Given that I have a registered account, when I enter my correct username and password, then the application logs me in and allows me to access my task list.


## US3: Log Out - 1 Story Points (Sprint 2)

As a logged-in user, I want to log out of my account so that my personal tasks remain secure when I am finished using the application.

Given that I am logged in, when I select the logout option, then the application ends my session and redirects me to the login page.



## US4: Add Task - 3 Story Points (Sprint 3)

As a registered user, I want to add new tasks so that I can keep track of the things I need to complete.

Given that I am logged in, when I enter a task title and optional description and submit the form, then the application saves the task and displays it in my task list.


## US5: View Tasks - 2 Story Points (Sprint 3)

As a registered user, I want to view my tasks so that I can see what I need to complete and what I have already finished.

Given that I am logged in, when I open the task management page, then the application displays my saved tasks along with their completion status.


## US6: Complete Task - 2 Story Points (Sprint 3)

As a registered user, I want to mark tasks as completed so that I can track my progress.

Given that I have an incomplete task, when I select the complete option, then the application updates the task's status and displays it as completed.


## US7: Delete Task - 2 Story Points (Sprint 3)

As a registered user, I want to delete tasks that I no longer need so that I can keep my task list organized.

Given that I have an existing task, when I select the delete option, then the application removes the task and updates my task list.


## Sequence Diagram (Sprint 1)

At least one **user story**, unrelated to user creation or authentication, must be detailed using a **sequence diagram**. A **sequence diagram** is a type of UML diagram that shows how objects interact in a particular scenario, emphasizing the order of messages exchanged between components over time. This helps visualize the flow of operations and the responsibilities of different parts of the system.

## Model (Sprint 1)

Include a **class diagram** that clearly describes the **model classes** used in the project and their associations. A **class diagram** is a UML diagram that represents the structure of the system by showing its classes, their attributes, methods, and the relationships between them (such as inheritance, aggregation, or composition). This helps visualize how the data and logic are organized within the application.

# Development Process 

This section should describe, in general terms, how Scrum was applied in the project. Include a table summarizing the division of the project into sprints, the **user story** goals planned for each sprint, the ones actually completed, and the start and end dates of each sprint. You may also add any relevant observations or reflections about the sprints as you see fit.

|Sprint#|Goals|Start|End|Done|Observations|
|---|---|---|---|---|---|
|1|Project planning, requirements, user stories, UML diagrams, and GitHub setup|11/16/26|mm/dd/26|Project planning, requirements, user stories, UML diagrams, and GitHub setup|Establish the project structure, define requirements, and create the use case, class, and sequence diagrams.|
|2|US1, US2, US3|mm/dd/26|mm/dd/26|US1, US2, US3|Implement user registration, login, and logout functionality, including database integration.|
|3|US4, US5, US6, US7|mm/dd/26|mm/dd/26|US4, US5, US6, US7|Implement task creation, task viewing, task completion, and task deletion.|
|4|White-box testing, black-box testing, coverage report, Docker deployment, and final documentation|mm/dd/26|mm/dd/26|White-box testing, black-box testing, coverage report, Docker deployment, and final documentation|Verify application functionality, generate the HTML coverage report, test Docker deployment, complete the burndown chart, and finalize the README.|


As in Project 2, you should take notes on the major Scrum meetings: planning, daily scrums, review, and retrospective. These meetings are essential for tracking progress, identifying obstacles, and ensuring continuous improvement. Use the Scrum folder and the shared templates to record your notes in an organized and consistent manner.

Embed an image of the burndown chart here. 

# Testing (Sprint 4)

In this section, share the results of the tests performed to verify the quality of the developed product, including the test coverage relative to the written code. Test coverage indicates how much of your code is exercised by tests, helping assess reliability. There is no minimum coverage requirement, but ensure there is at least some coverage through one white-box test (which examines internal logic and structure) and one black-box test (which validates functionality from the user’s perspective).
