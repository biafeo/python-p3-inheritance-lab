#!/usr/bin/env python

class User:
    def __init__(self, first_name, last_name):
        self.first_name= first_name
        self.last_name = last_name


from teacher import Teacher  
knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

my_teacher = Teacher("First", "Last", knowledge)