#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  curryVsLambda01.py
#  
#  Copyright 2015 Franz Habison <habison.franz@gmx.at>
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

# http://www.ferg.org/thinking_in_tkinter/all_programs.html


from tkinter import *

# ---------- code for class: curry (begin) ---------------------
class curry:
    """from Scott David Daniels'recipe
    "curry -- associating parameters with a function"
    in the "Python Cookbook"
    http://aspn.activestate.com/ASPN/Python/Cookbook/
    """

    def __init__(self, fun, *args, **kwargs):
        self.fun = fun
        self.pending = args[:]
        self.kwargs = kwargs.copy()

    def __call__(self, *args, **kwargs):
        if kwargs and self.kwargs:
            kw = self.kwargs.copy()
            kw.update(kwargs)
        else:
            kw = kwargs or self.kwargs
        return self.fun(*(self.pending + args), **kw)
# ---------- code for class: curry (end) ---------------------


# ---------- code for function: event_lambda (begin) --------
def event_lambda(f, *args, **kwds ):
    """A helper function that wraps lambda in a prettier interface.
    Thanks to Chad Netzer for the code."""
    return lambda event, f=f, args=args, kwds=kwds : f( *args, **kwds )
# ---------- code for function: event_lambda (end) -----------


class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        button_name = "OK"

        # command binding -- using curry
        self.button1 = Button(self.myContainer1,
           command = curry(self.buttonHandler, button_name, 1, "Good stuff!"))

        # event binding -- using the event_lambda helper function
        self.button1.bind("<Return>",
            event_lambda( self.buttonHandler, button_name, 1, "Good stuff!" ) )

        self.button1.configure(text=button_name, background="green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()  # Put keyboard focus on button1


        button_name = "Cancel"

        # command binding -- using curry
        self.button2 = Button(self.myContainer1,
            command = curry(self.buttonHandler, button_name, 2, "Bad  stuff!"))

        # event binding -- using the event_lambda helper function in two steps
        event_handler = event_lambda( self.buttonHandler, button_name, 2, "Bad  stuff!" )
        self.button2.bind("<Return>", event_handler )

        self.button2.configure(text=button_name, background="red")
        self.button2.pack(side=LEFT)


    def buttonHandler(self, argument1, argument2, argument3):
        print("    buttonHandler routine received arguments:", \
            argument1.ljust(8), argument2, argument3)

    def buttonHandler_a(self, event, argument1, argument2, argument3):
        print("buttonHandler_a received event", event)
        self.buttonHandler(argument1, argument2, argument3)

print("\n"*100) # clear the screen
print("Starting program tt079.")
root = Tk()
myapp = MyApp(root)
print("Ready to start executing the event loop.")
root.mainloop()
print("Finished       executing the event loop.")
