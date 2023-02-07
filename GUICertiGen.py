import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os

def createSecondWindowFunction():

    def addTextField():
        print("Added Text Field")
    
    def addImageField():
        print("Added Image Field")
    
    GUITitleName = projectName + " - Certificate Generator and Automatic Email"
    secondWindow = Tk()

    menuTabBar = Menu(secondWindow)
    secondWindow.config(menu=menuTabBar)
    addMenu = Menu(menuTabBar,tearoff=0,font=("MV Boli",12))

    menuTabBar.add_cascade(label="Add", menu=addMenu)
    addMenu.add_command(label="Text", command=addTextField)
    addMenu.add_separator()
    addMenu.add_command(label="Image", command=addImageField)



    secondWindow.title(GUITitleName)
    secondWindow.geometry('1249x640')

    secondWindow.resizable(True,True)

    frameCSVFile = Frame(secondWindow)
    frameCSVFile.pack()
    Label(frameCSVFile, text="Select your CSV file.",fg='#000000', font=("Arial",11)).pack(side=LEFT, pady=10)

    def selectCSVFileFunction():
        csvFileDIR = filedialog.askopenfilename(initialdir=os.curdir, title="Open a CSV File", filetypes=(("CSV File","*.csv"),("all files","*.*")))

        print('CSV File Selected: ', csvFileDIR)
        labelCSVSelectedName.config(text=csvFileDIR)


    labelCSVSelectedName = Label(frameCSVFile, text=" ",fg='#808080', font=("Arial",11))
    labelCSVSelectedName.pack(side=LEFT, padx= 10)
    buttonSelectCSVFile = Button(frameCSVFile, text="Select CSV", command=selectCSVFileFunction)
    buttonSelectCSVFile.pack(side=LEFT, padx= 10)

    screen_width = secondWindow.winfo_screenwidth()

    frameStaticLabel = Frame(secondWindow)
    frameStaticLabel.pack()

    
    labelStaticFields = Label(frameStaticLabel, text="Static Fields",fg="#303030", font=("Helvetica", 15), width=screen_width,height=1, bg='#A0A0A0', relief=SUNKEN, border=0)
    labelStaticFields.pack(pady=20)

    frameDynamicLabel = Frame(secondWindow)
    frameDynamicLabel.pack()

    
    labelDynamicFields = Label(frameDynamicLabel, text="Dynamic Fields",fg="#303030", font=("Helvetica", 15), width=screen_width,height=1, bg='#A0A0A0', relief=SUNKEN, border=0)
    labelDynamicFields.pack(pady=20)

    frameNameColumn = Frame(secondWindow)
    frameNameColumn.pack()

    Label(frameNameColumn,text='"Name" Column : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryNameColumn = Entry(frameNameColumn, font=("Arial",17), width=3)
    entryNameColumn.pack(side=LEFT, padx=5, pady=10)

    Label(frameNameColumn,text='X : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryNameX = Entry(frameNameColumn, font=("Arial",17), width=3)
    entryNameX.pack(side=LEFT, padx=5, pady=10)

    Label(frameNameColumn,text='Y : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryNameY = Entry(frameNameColumn, font=("Arial",17), width=3)
    entryNameY.pack(side=LEFT, padx=5, pady=10)

    Label(frameNameColumn,text='Size : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryNameSize = Entry(frameNameColumn, font=("Arial",17), width=3)
    entryNameSize.pack(side=LEFT, padx=5, pady=10)

    Label(frameNameColumn,text='Color : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryNameColor = Entry(frameNameColumn, font=("Arial",17), width=3)
    entryNameColor.pack(side=LEFT, padx=5, pady=10)

    framePhotoColumn = Frame(secondWindow)
    framePhotoColumn.pack()
 
    Label(framePhotoColumn,text='"Photo" Column : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryPhotoColumn = Entry(framePhotoColumn, font=("Arial",17), width=3)
    entryPhotoColumn.pack(side=LEFT, padx=5, pady=10)

    Label(framePhotoColumn,text='X : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryNameX = Entry(framePhotoColumn, font=("Arial",17), width=3)
    entryNameX.pack(side=LEFT, padx=5, pady=10)

    Label(framePhotoColumn,text='Y : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryNameY = Entry(framePhotoColumn, font=("Arial",17), width=3)
    entryNameY.pack(side=LEFT, padx=5, pady=10)

    Label(framePhotoColumn,text='Size : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryNameSize = Entry(framePhotoColumn, font=("Arial",17), width=3)
    entryNameSize.pack(side=LEFT, padx=5, pady=10)

    

    frameEmailColumn = Frame(secondWindow)
    frameEmailColumn.pack()

    Label(frameEmailColumn,text='"Email" Column : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryEmailColumn = Entry(frameEmailColumn, font=("Arial",17), width=3)
    entryEmailColumn.pack(side=LEFT, padx=5, pady=10)

    frameEmailLabel = Frame(secondWindow)
    frameEmailLabel.pack()

    labelEmailFields = Label(frameEmailLabel, text="Email Information",fg="#303030", font=("Helvetica", 15), width=screen_width,height=1, bg='#A0A0A0', relief=SUNKEN, border=0)
    labelEmailFields.pack(pady=20)

    frameEmailFields = Frame(secondWindow)
    frameEmailFields.pack()

    Label(frameEmailFields, text="Sender Email ID : ",font=("Arial",13) ).pack(side=LEFT, padx= 15, pady=15)
    entryEmailID = Entry(frameEmailFields,font=("Arial",13), width= 22)
    entryEmailID.pack(side=LEFT, padx= 7, pady=15)

    Label(frameEmailFields, text="Sender Password : ",font=("Arial",13) ).pack(side=LEFT, padx= 15, pady=15)
    entryEmailPassword = Entry(frameEmailFields,font=("Arial",13), width= 22)
    entryEmailPassword.pack(side=LEFT, padx= 7, pady=15)

    frameEmailSubject = Frame(secondWindow)
    frameEmailSubject.pack()
    Label(frameEmailSubject, text="Email Subject : ",font=("Arial",13) ).pack(side=LEFT,padx= 15, pady=15)
    entryEmailSubject = Entry(frameEmailSubject,font=("Arial",13),width= 50)
    entryEmailSubject.pack(side=LEFT,padx= 15, pady=15)

    frameEmailBody = Frame(secondWindow)
    frameEmailBody.pack()
    Label(frameEmailBody, text="Email Body : ",font=("Arial",13) ).pack(side=LEFT,padx= 15, pady=15)
    entryEmailBody = Entry(frameEmailBody,font=("Arial",13),width= 50)
    entryEmailBody.pack(side=LEFT,padx= 15, pady=15)

    Label(secondWindow, text="Please go through README.md to understand every function in its entirety, \nfor example: your Email ID password is different from your email login \npassword, the steps to generate the same are mentioned in README.").pack(pady=20)

    frameProceedButtons = Frame(secondWindow, bg="#f2ebee")
    frameProceedButtons.pack(side=BOTTOM)

    buttonGenerateTestCertificate = Button(frameProceedButtons, text="Generate Test Certificate")
    buttonGenerateTestCertificate.pack(side=LEFT,padx=7)

    #Add a warning window to Send Test Email - Indicate that it will go to the first email from CSV or ask for an email in new window
    buttonSendTestEmail = Button(frameProceedButtons, text="Send Test Email")
    buttonSendTestEmail.pack(side=LEFT,padx=7)

    #Add a warning window
    buttonGenerateAllCertificates = Button(frameProceedButtons, text="Generate & Email - All")
    buttonGenerateAllCertificates.pack(side=LEFT,padx=7)





    



    





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
    label = Label(projectNameFrame, text="""A folder with your project name will be created in current directory,\n to store temporary and final files (pdfs) to be emailed. \nOnce created, you can access them without using this application.\n\nPlease do not use same folder names and refrain \nfrom using forward/back slash, as it can cause issues \nfetching attachments from source.""",fg='#000000', bg = "#989898", font=("Arial",11))
    label.pack(pady=10)
    firstWindow.title("Certificate Generator")
    firstWindow['bg'] = '#989898'

    firstWindow.mainloop()

createFirstWindowFunction()









