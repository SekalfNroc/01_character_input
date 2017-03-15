#!/usr/local/bin/python3
import datetime

class Person:
    def __init__(self, options={}):
        self.name = str(options['name'])
        self.age  = int(options['age'])
    
    def year_when_aged(self, age, now=datetime.datetime.now()):
        year = now.year
        return year + self.years_until_aged(age)

    def years_until_aged(self, age):
        return age - self.age

while True: # Broken on success
    try:
        user = Person({
            'name': input('What is your name:\n> '),
            'age':  input('How old are you?  \n> ')
        })
        break
    except:
        pass

final_age = 100
final_year = user.year_when_aged(final_age)

print("%s will be %d years old in the year %d" % (
    user.name,
    final_age,
    final_year
))

