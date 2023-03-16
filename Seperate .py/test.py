#Import the required library
from tkinter import *
#Create an instance of tkinter frame or window
win = Tk()
#Define the geometry
win.geometry("750x400")
#Create a Frame
frame= Frame(win, height=10)
def close():
   win.destroy()
#Create a Label widget in the frame
text= Label(frame, text= "Register", font= ('Helvetica bold', 14))
text.pack(pady=20)
#ADDING A SCROLLBAR
myscrollbar=Scrollbar(frame,orient="vertical")
myscrollbar.pack(side="right",fill="y")
#Add Entry Widgets
Label(frame, text= "Username").pack()
username= Entry(frame, width= 20)
username.pack()
Label(frame, text= "password").pack()
password= Entry(frame, show="*", width= 15)
password.pack()
Label(frame, text= "Email Id").pack()
email= Entry(frame, width= 15)
email.pack()
#Create widget in the frame
button= Button(frame, text= "Close",font= ('Helvetica bold',14),
command= close)
button.pack(pady=20)
frame.pack()
win.mainloop()