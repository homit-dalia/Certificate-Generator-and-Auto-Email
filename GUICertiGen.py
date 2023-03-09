import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os

import csv
import urllib.request
from fpdf import FPDF

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from pathlib import Path
from PIL import Image

def createframeMainFunction():

    def sendEmail(testEmail):
        
        #fixed fields in email
        from_addr = entryEmailID.get()
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['Subject'] = entryEmailSubject.get()
        body = MIMEText(textEmailBody.get(1.0,END))
        msg.attach(body)

        try:
            with smtplib.SMTP(host="smtp.gmail.com", port = 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(entryEmailID.get(),entryEmailPassword.get())
                incorrectEmailIDPassword = False
        except:
            incorrectEmailIDPassword = True
            print("Email ID and/or password is incorrect. Please try again.")

        if(incorrectEmailIDPassword == False):
            with open(labelCSVSelectedName.cget("text"), 'r') as csvfile:
                
                csvData = csv.reader(csvfile)
                for lines in csvData:
                    if(testEmail):
                        msg['To'] = entryEmailID.get()
                        print("Sending Test Email to : " + entryEmailID.get())

                    else:
                        msg['To'] = lines[int(entryEmailColumn.get())-1]
                        print("Sending Email to : " + lines[int(entryEmailColumn.get())-1])

                    try:
                        attachmentCertificateName = projectName + 'OutputCertificates/' +  lines[int(entryNameColumn.get())-1] + ".pdf"
                        attachment = open(attachmentCertificateName, 'rb')
                        attachment_package = MIMEBase('application', 'octet-stream')
                        attachment_package.set_payload((attachment).read())
                        encoders.encode_base64(attachment_package)
                        attachment_package.add_header('Content-Disposition', "attachment; filename= " + attachmentCertificateName)
                        msg.attach(attachment_package)
                    except:
                        print("Could not fetch/open certificate for participant - " + lines[int(entryNameColumn.get())-1])

                    try:
                        with smtplib.SMTP(host="smtp.gmail.com", port = 587) as smtp:
                            smtp.ehlo()
                            smtp.starttls()
                            smtp.login(entryEmailID.get(),entryEmailPassword.get())
                            smtp.send_message(msg)
                            print("Email sent to " + lines[int(entryEmailColumn.get())-1])
                    except:
                        print("Error sending email to : participant - " + lines[int(entryNameColumn.get())-1]+". Please try sending them an email manually. Possible reason - Bad Email Address.")
                    
                    if(testEmail):
                        break

    def imageDownloader():
            with open('userData.csv', 'r') as csvfile:
                data = csv.reader(csvfile)
                for lines in data:
                    url = lines[2]
                    print ("Downloading image for " + lines[1])

                    image_url = url
    #does not work with drive links. Imgur or any other links ending with .jpg/.jpeg/.png works. Please use jpg or pjeg format
                    filename = "ImageDisplay/" + lines[1] + ".jpg"
                    urllib.request.urlretrieve(image_url, filename)

                    print("Image Downloaded")

    def createPDF(testCertificate):

        template = Image.open(labelTemplateSelectedName.cget("text"))

        hex = entryNameColor.get().lstrip('#')

        rgbColor =tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        print(rgbColor)

        dpi = template.info['dpi']
        width = template.width *25.4 / dpi[0]
        height = template.height *25.4 / dpi[0]

        page1 = FPDF('l', 'mm', [height,width])
        page1.add_page()
        
        page1.image(labelTemplateSelectedName.cget("text"), 0, 0, w = width, h=height )
        body = page1
        body.set_font("Arial",size=int(entryNameSize.get()))
        body.set_text_color(int(rgbColor[0]),int(rgbColor[1]),int(rgbColor[2]))

        with open(labelCSVSelectedName.cget("text"), 'r') as csvfile:
            print("Inside create PDF")
            data = csv.reader(csvfile)

            nameColumn = int(entryNameColumn.get()) - 1
            
            for lines in data:
                print ("Creating PDF for participant " + lines[int(nameColumn)])

                body.text(int(entryNameX.get()),int(entryNameY.get()),lines[int(nameColumn)])

                pdfName = projectName + "/OutputCertificates/" + lines[int(nameColumn)] + ".pdf"
                body.output("Certi1.pdf")
                page1.output("Certi1.pdf")

                print("Certificate created for " + lines[int(nameColumn)])

                if(int(testCertificate) == 1):
                    break


    def addFont():
        print("Clicked Added Font")
    
    GUITitleName = projectName + " - Certificate Generator and Automatic Email"
    secondWindow = Tk()

    menuTabBar = Menu(secondWindow)
    secondWindow.config(menu=menuTabBar)
    addMenu = Menu(menuTabBar,tearoff=0,font=("MV Boli",12))

    #change to just add font types from menubar
    menuTabBar.add_cascade(label="Add", menu=addMenu)
    addMenu.add_command(label="Font", command=addFont)

    secondWindow.title(GUITitleName)
    secondWindow.geometry('1100x640')

    secondWindow.resizable(0,0)


    #scrollbar starts here

    frameMainScrollBar = Frame(secondWindow, width=100)
    frameMainScrollBar.pack(fill=BOTH, expand=1)

    canvas = Canvas(frameMainScrollBar,)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbarMain = tk.Scrollbar(frameMainScrollBar, orient=VERTICAL, width=25, troughcolor="black", command=canvas.yview)
    scrollbarMain.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbarMain.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frameMain =  Frame(canvas)
    canvas.create_window((0,0), window=frameMain, anchor="nw")

    #scrollbar code ends here

    frameCSVFile = Frame(frameMain)
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

    frameStaticLabel = Frame(frameMain)
    frameStaticLabel.pack()

    
    labelStaticFields = Label(frameStaticLabel, text="Static Fields",fg="#303030", font=("Helvetica", 15), width=100,height=1, bg='#A0A0A0', relief=SUNKEN, border=0)
    labelStaticFields.pack(pady=20)

    def addStaticFields():
        Label(frameMain, text="Test Static field").pack()
        Entry(frameMain).pack()
    frameSelectTemplate = Frame(frameMain)
    frameSelectTemplate.pack()
    Label(frameSelectTemplate, text="Select your Certificate Background/Template.",fg='#000000', font=("Arial",11)).pack(side=LEFT, pady=10)

    def selectTemplateButton():
        templateFileDIR = filedialog.askopenfilename(initialdir=os.curdir, title="Open an Image File", filetypes=(("JPEG File","*.jpg"),("PNG File","*.png"),("all files","*.*")))

        print('Image File Selected: ', templateFileDIR)
        labelTemplateSelectedName.config(text=templateFileDIR)

    labelTemplateSelectedName = Label(frameSelectTemplate, text=" ",fg='#808080', font=("Arial",11))
    labelTemplateSelectedName.pack(side=LEFT, padx= 10)
    buttonSelectTemplate = Button(frameSelectTemplate, text="Select Image", command=selectTemplateButton)
    buttonSelectTemplate.pack(side=LEFT, padx= 10)

    frameDynamicLabel = Frame(frameMain)
    frameDynamicLabel.pack()

    labelDynamicFields = Label(frameDynamicLabel, text="Dynamic Fields",fg="#303030", font=("Helvetica", 15), width=100,height=1, bg='#A0A0A0', relief=SUNKEN, border=0)
    labelDynamicFields.pack(pady=20)

    frameNameColumn = Frame(frameMain)
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
    entryNameColor = Entry(frameNameColumn, font=("Arial",17), width=9)
    entryNameColor.pack(side=LEFT, padx=5, pady=10)

    framePhotoColumn = Frame(frameMain)
    framePhotoColumn.pack()
 
    Label(framePhotoColumn,text='"Photo" Column : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryPhotoColumn = Entry(framePhotoColumn, font=("Arial",17), width=3)
    entryPhotoColumn.pack(side=LEFT, padx=5, pady=10)

    Label(framePhotoColumn,text='X : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryPhotoX = Entry(framePhotoColumn, font=("Arial",17), width=3)
    entryPhotoX.pack(side=LEFT, padx=5, pady=10)

    Label(framePhotoColumn,text='Y : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryPhotoY = Entry(framePhotoColumn, font=("Arial",17), width=3)
    entryPhotoY.pack(side=LEFT, padx=5, pady=10)

    Label(framePhotoColumn,text='Size : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryPhotoSize = Entry(framePhotoColumn, font=("Arial",17), width=3)
    entryPhotoSize.pack(side=LEFT, padx=5, pady=10)

    frameEmailColumn = Frame(frameMain)
    frameEmailColumn.pack()

    Label(frameEmailColumn,text='"Email" Column : ', font=("Arial", 13)).pack(side=LEFT, pady=10)
    entryEmailColumn = Entry(frameEmailColumn, font=("Arial",17), width=3)
    entryEmailColumn.pack(side=LEFT, padx=5, pady=10)

    frameEmailLabel = Frame(frameMain)
    frameEmailLabel.pack()

    labelEmailFields = Label(frameEmailLabel, text="Email Information",fg="#303030", font=("Helvetica", 15), width=100,height=1, bg='#A0A0A0', relief=SUNKEN, border=0)
    labelEmailFields.pack(pady=20)

    frameEmailFields = Frame(frameMain)
    frameEmailFields.pack()

    Label(frameEmailFields, text="Sender Email ID : ",font=("Arial",13) ).pack(side=LEFT, padx= 15, pady=15)
    entryEmailID = Entry(frameEmailFields,font=("Arial",13), width= 22)
    entryEmailID.pack(side=LEFT, padx= 7, pady=15)

    Label(frameEmailFields, text="Sender Password : ",font=("Arial",13) ).pack(side=LEFT, padx= 15, pady=15)
    entryEmailPassword = Entry(frameEmailFields,font=("Arial",13), width= 22, show="*")
    entryEmailPassword.pack(side=LEFT, padx= 7, pady=15)

    frameEmailSubject = Frame(frameMain)
    frameEmailSubject.pack()
    Label(frameEmailSubject, text="Email Subject : ",font=("Arial",13) ).pack(side=LEFT,padx= 15, pady=15)
    entryEmailSubject = Entry(frameEmailSubject,font=("Arial",13),width= 50)
    entryEmailSubject.pack(side=LEFT,padx= 15, pady=15)

    frameEmailBody = Frame(frameMain)
    frameEmailBody.pack()
    Label(frameEmailBody, text="Email Body : ",font=("Arial",13) ).pack(side=LEFT,padx= 15, pady=15)
    textEmailBody = Text(frameEmailBody,font=("Arial",13),width= 50, height=5)
    textEmailBody.pack(side=LEFT,padx= 15, pady=15)

    Label(frameMain, text="Please go through README.md to understand every function in its entirety, \nfor example: your Email ID password is different from your email login \npassword, the steps to generate the same are mentioned in README.").pack(pady=20)

    frameProceedButtons = Frame(frameMain, bg="#f2ebee")
    frameProceedButtons.pack(side=BOTTOM)

    buttonGenerateTestCertificate = Button(frameProceedButtons, text="Generate Test Certificate", command=lambda: createPDF(1))
    buttonGenerateTestCertificate.pack(side=LEFT,padx=7)

    buttonSendTestEmail = Button(frameProceedButtons, text="Send Test Email", command=lambda: sendEmail(1))
    buttonSendTestEmail.pack(side=LEFT,padx=7)

    #Add a warning window
    buttonGenerateAllCertificates = Button(frameProceedButtons, text="Generate & Email - All")
    buttonGenerateAllCertificates.pack() 

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
        
        createframeMainFunction()
        firstWindow.destroy()


    right_arrow_blue = PhotoImage(file="source_images/right_arrow_blue.png")
    buttonSaveProjectName = Button(projectNameFrame, text=" Create Project", font=("Arial",11), activebackground='#9EDEC6',command=buttonPress, image=right_arrow_blue,compound=LEFT).pack(side=TOP, pady=10)
    label = Label(projectNameFrame, text="""A folder with your project name will be created in current directory,\n to store temporary and final files (pdfs) to be emailed. \nOnce created, you can access them without using this application.\n\nPlease do not use same folder names and refrain \nfrom using forward/back slash, as it can cause issues \nfetching attachments from source.""",fg='#000000', bg = "#989898", font=("Arial",11))
    label.pack(pady=10)
    firstWindow.title("Certificate Generator")
    firstWindow['bg'] = '#989898'

    firstWindow.mainloop()

createFirstWindowFunction()









