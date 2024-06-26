# ClassForge
Welcome to the ClassForge repository! This project is a web aplication designed to help college students manage their courses and grades efficiently.

Note: This project is currently a work in progress and not finished yet.

## Table of Contents

* Installation
* Demo
* Features
* Usage
* Roadmap
* Contact

## Installation
The Project is made using the Django framework which runs on python

1. Install [Python](https://www.python.org/downloads/)
2. Install Django using the following in your editors command prompt:
* Windows: `py -m pip install Django==5.0.6`
* Mac/Linux: `python -m pip install Django==5.0.6`
4. Clone the repository
5. Change the direcotry to ClassForge 
6. In the terminal input `python manage.py migrate` to run migration 
7. In the terminal input `python manage.py runserver`

Once that is done you can open the project by using `crtl + Left Click` on the link next to `Starting development server at` or copying and pasting the url. Use the url paths next to each section in the demo

## Demo
### Login (/Login/login_view/)
Users must use thier email and password to login.
![image](https://github.com/MichaelP901/ClassForge/assets/93054968/789a5b63-1dc2-4c0a-bf6e-d8aceb7885e1)
### Sign up (/Login/signup/)
New users must sign up using their email and the same email cannot be used for multiple accounts.
![image](https://github.com/MichaelP901/ClassForge/assets/93054968/027aaaa5-a6ad-4627-a3df-666d4732f6ca)
### Dashboard (/HomeScreen)
Welcomes the user and shows assignments in the assignment and date table if there are any, Grades of all classes, and shows the calender and highlights the current day.
![image](https://github.com/MichaelP901/ClassForge/assets/93054968/2f712b74-7a74-4011-adc2-534c06cae7d3)
### Grades (/Grades)
The user can input classes and assingments. (Note: in order to add an assingment the user must click on the class before adding an assignment)
![image](https://github.com/MichaelP901/ClassForge/assets/93054968/98eaf3a3-4298-4ecb-9b58-5ed022fc9388)
### Calender (/Calender)
The user can add assignments and look at assignments thorughout the semester
![image](https://github.com/MichaelP901/ClassForge/assets/93054968/7ba698aa-786f-4f39-9fb1-24a43b97972b)


## Features
* Course Management: Add, update, and delete courses.
* Grade Management: Record and manage grades for each course.
* Dashboard: Show upcoming assingments and calender.
* User Authentication: Secure login and registration for students.

## Usage

1. Register: Create a new account using your email.
2. Login: Access your account by logging in.
3. Add Courses: Go to the "Courses" section and add your current courses.
4. Manage Grades: Enter grades for assignments, exams, and other assessments.
5. View Dashboard: Get an overview of your academic performance and upcoming assignments
6. Calender: View assignment, exams, or other scheduled events

## Roadmap
Currently Implemented
* User authentication (login and registration)
* Course management (add, update, delete courses)
* Grade management (record grades for courses)
* Dashboard for an overview of courses and grades

In Progress
* Responsive design improvements
* Calender revamp
* Dashboard improvments

Planned Features
* Charts showing Grades and how the class grades are split up (ie. Homework: 15%, Exams: 25%, etc.)
* Notifications and reminders for upcoming assignments and exams
* Display student discounts under Student Perks

## Contact
Email: michael.mp915@gmail.com
