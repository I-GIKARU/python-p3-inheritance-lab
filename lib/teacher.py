#!/usr/bin/env python3

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # Initialize knowledge list with at least one item
        self.knowledge = [
            "Math", 
            "Science", 
            "History", 
            "Art", 
            "Literature"
        ]

    def teach(self):
        # Return a random topic from knowledge
        return random.choice(self.knowledge)
