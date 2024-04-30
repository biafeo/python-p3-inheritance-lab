#!/usr/bin/env python


from user import User
import random

class Teacher(User):
    '''Class "Teacher" in teacher.py'''
    def __init__(self, first_name, last_name, knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
        ]):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
    @property
    def knowledge(self):
        return self._knowledge
    
    @knowledge.setter
    def knowledge(self, knowledge):
        if isinstance(knowledge, list) and len(knowledge) >0:
            self._knowledge=knowledge


    def teach(self):
        '''returns a random element from self.knowledge.'''
        if not self.knowledge:
            return None 
        return random.choice(self.knowledge)