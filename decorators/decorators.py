#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  decorators.py
#  
#  Copyright 2016 Franz Habison <habison.franz@gmx.at>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# Quelle: https://codequs.com/p/Ski411egq/understanding-decorators-in-python/

from datetime import datetime
from time import sleep

# Startpunkt
def greet(name):
	return "Greetings, {}!".format(name)


def time_wrapper(fn):
	def new_function(*args, **kwargs):
		msg = fn(*args, **kwargs)
		new_msg = "Time: {} {} ".format(datetime.now(), msg)
		return new_msg
	
	return new_function


greet = time_wrapper(greet)
print(greet("fraunz"))


# Decorators allgemein
#@decorator_callable
#def awesome_func():
#	return True

# Equivalent zu
#awesome_func = decorator_callable(awesome_func)



# Beispiel eigenen Decorator schreiben
def timed(fn):
	def wrapped():
		print("Current time: {}".format(datetime.now()))
		return fn()
	
	return wrapped


@timed
def hello():
	print("Hello World!")

for x in range(5):
	hello()
	sleep(1)


# Sleeper Decorator
print("Sleeper Decorator *******************")
def sleeper(secs):
	def decorator(fn):
		def wrapped(*args, **kwargs):
			sleep(secs)
			fn(*args, **kwargs)
		
		return wrapped
	
	return decorator

@sleeper(3)
def say_hello(name):
	print("Hello {}!".format(name))

say_hello("Fraunz")


# Decorator Chaining
print("Sleeper Decorator Chaining *******************")

@sleeper(5)
@sleeper(2)
def say_hello2(name):
	print("Hello {}!".format(name))

say_hello2("Rudolf")


print("Class Sleeper Decorator *******************")
class Sleeper:
	def __init__(self, secs):
		self.__secs = secs
	
	def __call__(self, fn):
		def wrapped(*args, **kwargs):
			sleep(self.__secs)
			return fn(*args, **kwargs)
		
		return wrapped




@Sleeper(5)
def say_hello3(name):
	print("Hello {}, it is now: {}".format(name, datetime.now()))

for x in range(5):
	say_hello3("Sepp")



print("Decorating Class and Class Methods *******************")
def int_age(fn):
	def wrapped(**kwargs):
		kwargs['age'] = int(kwargs.get('age'))
		return fn(**kwargs)
	
	return wrapped

@int_age
class Person:
	def __init__(self, age):
		self.age = age
	
	def print_age(self):
		print(self.age)

p = Person(age='12')
p.print_age()
























