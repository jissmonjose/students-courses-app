# Django Course Registration Application

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2-brightgreen.svg)](https://djangoproject.com)

This course registration project allows the students to register for a IT related courses.
In this Django App, students can view various courses available, can also search through list of courses. Thus eases the course search process. Students can also view the trainer of the programe.
There is modules for Admin who has the proision to add students, courses, batches, trainers. Also he/she can allot schedule for each batches. Admin able to manipulate these datas if needed.

![Django Course Registration](https://github.com/jissmonjose/students-courses-app/blob/master/screenshots/screenshot3.png)



## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/jissmonjose/students-courses-app.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
