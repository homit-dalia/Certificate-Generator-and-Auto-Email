import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os

def createSecondWindowFunction():
    GUITitleName = projectName + " - Certificate Generator and Automatic Email"
    secondWindow = Tk()
    menuTabBar = Menu(secondWindow)
    secondWindow.config(menu=menuTabBar)
    fileMenu = Menu(menuTabBar,tearoff=0)
    menuTabBar.add_cascade(label="File", menu=fileMenu)

    secondWindow.title(GUITitleName)
    secondWindow.geometry('1249x640')

    secondWindow.resizable(True,True)

    



    


    frameCSVFile = Frame(secondWindow)
    frameCSVFile.pack(side=LEFT)
    Label(frameCSVFile, text="Select your CSV file.",fg='#000000', font=("Arial",11)).pack(side=LEFT, padx= 10)


   


    

    def selectCSVFileFunction():
        csvFileDIR = filedialog.askopenfilename(initialdir=os.curdir, title="Open a CSV File", filetypes=(("CSV File","*.csv"),("all files","*.*")))

        print('CSV File Selected: ', csvFileDIR)
        labelCSVSelectedName.config(text=csvFileDIR)


    labelCSVSelectedName = Label(frameCSVFile, text=" ",fg='#808080', font=("Arial",11))
    labelCSVSelectedName.pack(side=LEFT, padx= 10)
    buttonSelectCSVFile = Button(frameCSVFile, text="Select CSV", command=selectCSVFileFunction)
    buttonSelectCSVFile.pack(side=LEFT, padx= 10)


def createFirstWindowFunction():
    firstWindow = Tk()
    firstWindow.geometry('700x440')
    firstWindow.resizable(0,0)

    projectNameFrame = Frame(firstWindow, bg = '#989898')
    projectNameFrame.place(relx=.5, rely=.5,anchor= CENTER)


    entryProjectName = Entry(projectNameFrame, font = ("Helvetica", 17))
    entryProjectName.insert(0,"MyFirstCertificate")
    entryProjectName.pack(side=TOP, pady=10)



    def buttonPress():
        #error - restrict empty folder name and slashes.
        global projectName
        projectName = entryProjectName.get()
        print("Project name is "+'"'+projectName+'"'+". Creating a directory named the folder.")
        try:
            os.mkdir(projectName)
        except:
            print("An error occured - Directory already exists. ")
        
        createSecondWindowFunction()
        firstWindow.destroy()


    right_arrow_blue = PhotoImage(file="source_images/right_arrow_blue.png")
    buttonSaveProjectName = Button(projectNameFrame, text=" Create Project", font=("Arial",11), activebackground='#9EDEC6',command=buttonPress, image=right_arrow_blue,compound=LEFT).pack(side=TOP, pady=10)
    label = Label(projectNameFrame, text="""A folder with your project name will be created in current directory,
    to store temporary and final files (pdfs) to be emailed. 
    Once created, you can access them without using this application.
    
    Please do not use same folder names and refrain 
    from using forward/back slash, as it can cause issues 
    fetching attachments from source.""",fg='#000000', bg = "#989898", font=("Arial",11))
    label.pack(pady=10)
    firstWindow.title("Certificate Generator")
    firstWindow['bg'] = '#989898'

    firstWindow.mainloop()

createFirstWindowFunction()









