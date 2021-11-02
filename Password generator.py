"""
	 A simple password generator program that uses random numbers and letters to generate
	passwords of desired length 
								"""

# import needed modules
from tkinter import *
from PIL import ImageTk, Image
import time
root = Tk()

root.title('Password Generator')
root.iconbitmap("icons/favicon.ico")
#root.geometry('420x350')
root.configure(bg='#252323')

# textbox
e = Text(root, width=25, height=2, relief=SUNKEN)

# The definitions 
def gen():
	num = e.get('1.0', END)
	for i in range(10):
		s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
		p = list(s)

		l = []
		global m
		m = ''
		for i in range(int(num)):
			from random import choice
			l.append(choice(p))

		for ele in l:
			m += ele
		if m[0] in '0123456789':
			global myLabel1
			myLabel1 = Label(root, text=f'Your generated password is {m}		'  , font=("Book Antiqua", 12), bg='#252323', fg='white')
			myLabel1.grid(row=3, column=0)



			break
			
		else:
			continue

def clear():
	myLabel1.destroy()#Destroys the widget
	e.delete('1.0', END)

# root.bind('<Return>', gen)
# root.bind('<Delete>', clear)

# align widgets in a frame
frame = Frame(root)
myLabel = Label(root, text='Enter the length of the Password you want', font=("Book Antiqua", 12), bg='#252323', fg='white')
button = Button(frame, text='Generate', font=("Book Antiqua", 12), command=gen, bg='#252323', fg='white')
button_clear = Button(frame, text='Clear', font=("Book Antiqua", 12), command=clear, bg='#252323', fg='white')

# place the widgets on screen
myLabel.grid(row=0, column=0, columnspan=2)
e.grid(row=1, column=0, columnspan=2, pady=10 )
frame.grid(row=2, column=0, pady=10, columnspan=2)
button.grid(row=0, column=0)
button_clear.grid(row=0, column=1)

# run the program
mainloop()