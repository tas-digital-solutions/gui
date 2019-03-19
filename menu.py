from tkinter import *
#http://effbot.org/tkinterbook/menu.htm


def doNothingFunction():
    # this function presents a button that does nothing
    # normally you would hook up the menus to do something
    filewin = Toplevel(root)
    button = Button(filewin, text="Ok")
    button.pack()


def exitProgram():
    exit()


# main tk window
root = Tk()

# main menubar
menuBar = Menu(root)

# file menu
filemenu = Menu(menuBar, tearoff=0)
filemenu.add_command(label="New", command=doNothingFunction)
filemenu.add_command(label="Open", command=doNothingFunction)
filemenu.add_command(label="Save", command=doNothingFunction)
filemenu.add_command(label="Save as...", command=doNothingFunction)
filemenu.add_command(label="Close", command=doNothingFunction)
# adding a spacer
filemenu.add_separator()

# adding the commands to exit
filemenu.add_command(label="Exit", command=exitProgram)
menuBar.add_cascade(label="File", menu=filemenu)

# edit menu
editmenu = Menu(menuBar, tearoff=0)
editmenu.add_command(label="Undo", command=doNothingFunction)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=doNothingFunction)
editmenu.add_command(label="Copy", command=doNothingFunction)
editmenu.add_command(label="Paste", command=doNothingFunction)
editmenu.add_command(label="Delete", command=doNothingFunction)
editmenu.add_command(label="Select All", command=doNothingFunction)

menuBar.add_cascade(label="Edit", menu=editmenu)

# help menu
helpmenu = Menu(menuBar, tearoff=0)
helpmenu.add_command(label="Help Index", command=doNothingFunction)
helpmenu.add_command(label="About...", command=doNothingFunction)
menuBar.add_cascade(label="Help", menu=helpmenu)

# add the menubar to the root window
root.config(menu=menuBar)
# run our TK
root.mainloop()
