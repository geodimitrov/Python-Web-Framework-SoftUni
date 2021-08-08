Python Web Framework @ SoftUni

This repo was created for the 'Python Web Framework' course at SoftUni. 
It contains only one Django project which is my web app for the final exam.

The idea behind the project is to create an operational web application which allows
users to register, create/edit profiles, interact with each other, have a good user 
experience, use AWS for various purposes, etc. In thi case, the app took the form of
a 'book center' where the main focus would be books, reading, events related to books
and reading, etc. 

The project consists of one main app called 'book center', folder for static files, 
templates folder & tests folder. Media files are hosted on AWS.

The project app uses Postgresql as a DBMS and it's hosted on AWS.

The app can send automatic emails via AWS SES.

The project app uses environment variables to hide sensitive information.

The project app uses 3-rd party packages:
- django-crispy-forms
- django-storages
- django-ses
- pillow
- psycopg2


DISCLAIMER: This app is not a fully operational product, it's not intended for commercial use 
and has many features that haven't been properly tested or developed.
