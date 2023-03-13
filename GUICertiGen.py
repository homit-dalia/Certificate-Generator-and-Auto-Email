import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import os

import csv
import urllib.request
from fpdf import FPDF
from PIL import Image

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib


def createframeMainFunction():

    def sendEmail(testEmail):

        if(testEmail):
            message = 1
        else:
            message = messagebox.askyesno(title="Do you want to send the email?", message="Proceeding will email all the participants with their respective certificates.")

        if(message):
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
                            attachmentCertificateName = lines[int(entryNameColumn.get())-1] + ".pdf"
                            attachmentCertificateSource = projectName + '/OutputCertificates/' +  lines[int(entryNameColumn.get())-1] + ".pdf"
                            attachment = open(attachmentCertificateSource, 'rb')
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
        else:
            print("You selected 'No' to email participants.")
       

    def imageDownloader():
            with open('userData.csv', 'r') as csvfile:
                data = csv.reader(csvfile)
                for lines in data:
                    url = lines[2]
                    print ("Downloading image for " + lines[1])

                    image_url = url
    #does not work with drive links. Imgur or any other links ending with .jpg/.jpeg/.png works. Please use jpg or png format
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
        
        
        nameColumn = int(entryNameColumn.get()) - 1

        with open(labelCSVSelectedName.cget("text"), 'r') as csvfile:
            data = csv.reader(csvfile)

            for lines in data:

                try:
                    page1 = FPDF('l', 'mm', [height,width])
                    page1.add_page()
                    page1.image(labelTemplateSelectedName.cget("text"), 0, 0, w = width, h=height )
                    body = page1
                    body.set_font("Arial",size=int(entryNameSize.get()))
                    body.set_text_color(int(rgbColor[0]),int(rgbColor[1]),int(rgbColor[2]))

                    print ("Creating PDF for participant " + lines[int(nameColumn)])

                    body.text(int(entryNameX.get()),int(entryNameY.get()),lines[int(nameColumn)])

                    pdfName = projectName + "/OutputCertificates/" + lines[int(nameColumn)] + ".pdf"
                    body.output(pdfName)
                    page1.output(pdfName)

                    print("Certificate created for " + lines[int(nameColumn)])
                except:
                    print("Error creating certificate for " + lines[int(nameColumn)])

                if(testCertificate):
                    break
        if(testCertificate):
            print("Did not email as it is a test certificate")


    def addFont():
        print("Clicked Added Font")
    
    def generateAllCertificatesAndEmail():
        if messagebox.askyesno(title="Generate Certificates for all the entries?", message="Proceeding will freeze the interface for a while. Sit tight and relax!"):
            createPDF(0)
        else:
            print("Cancelled generate all certificates")

        #Add a warning that Window will hang and a warning - Contine \ Cancel

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

    secondWindow['bg'] = '#363940'
    secondWindow.resizable(0,0)


    #scrollbar starts here
    frameMainScrollBar = Frame(secondWindow, width=100)
    frameMainScrollBar.pack(fill=BOTH, expand=1)

    canvas = Canvas(frameMainScrollBar)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbarMain = tk.Scrollbar(frameMainScrollBar, orient=VERTICAL, width=25, troughcolor="black", command=canvas.yview)
    scrollbarMain.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbarMain.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frameMain =  Frame(canvas, bg = "#363940")
    canvas.create_window((0,0), window=frameMain, anchor="nw")
    #scrollbar code ends here


    frameCSVFile = Frame(frameMain, bg="#363940")
    frameCSVFile.pack()
    Label(frameCSVFile, text="Select your CSV file.", font=("Arial",11),fg='#BDBEC0', bg = "#363940").pack(side=LEFT, pady=10)

    def selectCSVFileFunction():
        csvFileDIR = filedialog.askopenfilename(initialdir=os.curdir, title="Open a CSV File", filetypes=(("CSV File","*.csv"),("all files","*.*")))

        print('CSV File Selected: ', csvFileDIR)
        labelCSVSelectedName.config(text=csvFileDIR)

    labelCSVSelectedName = Label(frameCSVFile, text="",fg='#BDBEC0', bg = "#363940", font=("Arial",11))
    labelCSVSelectedName.pack(side=LEFT, padx= 10)
    buttonSelectCSVFile = Button(frameCSVFile, text="Select CSV", command=selectCSVFileFunction)
    buttonSelectCSVFile.pack(side=LEFT, padx= 10)

    screen_width = secondWindow.winfo_screenwidth()

    frameStaticLabel = Frame(frameMain, bg="#363940")
    frameStaticLabel.pack()

    
    labelStaticFields = Label(frameStaticLabel, text="Static Fields",fg="#303030", font=("Helvetica", 15), width=100,height=1, bg='#A0A0A0', relief=SUNKEN, border=0)
    labelStaticFields.pack(pady=20)

    def addStaticFields():
        Label(frameMain, text="Test Static field",fg='#BDBEC0', bg = "#363940").pack()
        Entry(frameMain, bg='#ccd4de').pack()
    frameSelectTemplate = Frame(frameMain, bg="#363940")
    frameSelectTemplate.pack()
    Label(frameSelectTemplate, text="Select your Certificate Background/Template.",fg='#BDBEC0', bg = "#363940", font=("Arial",11)).pack(side=LEFT, pady=10)

    def selectTemplateButton():
        templateFileDIR = filedialog.askopenfilename(initialdir=os.curdir, title="Open an Image File", filetypes=(("JPEG File","*.jpg"),("PNG File","*.png"),("all files","*.*")))

        print('Image File Selected: ', templateFileDIR)
        labelTemplateSelectedName.config(text=templateFileDIR)

    labelTemplateSelectedName = Label(frameSelectTemplate, text="",fg='#BDBEC0', bg = "#363940", font=("Arial",11))
    labelTemplateSelectedName.pack(side=LEFT, padx= 10)
    buttonSelectTemplate = Button(frameSelectTemplate, text="Select Image", command=selectTemplateButton)
    buttonSelectTemplate.pack(side=LEFT, padx= 10)

    frameDynamicLabel = Frame(frameMain, bg="#363940")
    frameDynamicLabel.pack()

    labelDynamicFields = Label(frameDynamicLabel, text="Dynamic Fields",fg="#303030", font=("Helvetica", 15), width=100,height=1, bg='#A0A0A0', relief=SUNKEN, border=0)
    labelDynamicFields.pack(pady=20)

    frameNameColumn = Frame(frameMain, bg="#363940")
    frameNameColumn.pack()

    Label(frameNameColumn,text='"Name" Column : ', font=("Arial", 13),fg='#BDBEC0', bg = "#363940").pack(side=LEFT, pady=10)
    entryNameColumn = Entry(frameNameColumn, font=("Arial",17), width=3, bg='#ccd4de')
    entryNameColumn.pack(side=LEFT, padx=5, pady=10)

    Label(frameNameColumn,text='X : ', font=("Arial", 13),fg='#BDBEC0', bg = "#363940").pack(side=LEFT, pady=10)
    entryNameX = Entry(frameNameColumn, font=("Arial",17), width=3, bg='#ccd4de')
    entryNameX.pack(side=LEFT, padx=5, pady=10)

    Label(frameNameColumn,text='Y : ', font=("Arial", 13),fg='#BDBEC0', bg = "#363940").pack(side=LEFT, pady=10)
    entryNameY = Entry(frameNameColumn, font=("Arial",17), width=3, bg='#ccd4de')
    entryNameY.pack(side=LEFT, padx=5, pady=10)

    Label(frameNameColumn,text='Size : ', font=("Arial", 13),fg='#BDBEC0', bg = "#363940").pack(side=LEFT, pady=10)
    entryNameSize = Entry(frameNameColumn, font=("Arial",17), width=3, bg='#ccd4de')
    entryNameSize.pack(side=LEFT, padx=5, pady=10)

    Label(frameNameColumn,text='Color : ', font=("Arial", 13),fg='#BDBEC0', bg = "#363940").pack(side=LEFT, pady=10)
    entryNameColor = Entry(frameNameColumn, font=("Arial",17), width=9, bg='#ccd4de')
    entryNameColor.pack(side=LEFT, padx=5, pady=10)

    framePhotoColumn = Frame(frameMain, bg="#363940")
    framePhotoColumn.pack()
 
    Label(framePhotoColumn,text='"Photo" Column : ', font=("Arial", 13),fg='#BDBEC0', bg = "#363940").pack(side=LEFT, pady=10)
    entryPhotoColumn = Entry(framePhotoColumn, font=("Arial",17), width=3, bg='#ccd4de')
    entryPhotoColumn.pack(side=LEFT, padx=5, pady=10)

    Label(framePhotoColumn,text='X : ', font=("Arial", 13),fg='#BDBEC0', bg = "#363940").pack(side=LEFT, pady=10)
    entryPhotoX = Entry(framePhotoColumn, font=("Arial",17), width=3, bg='#ccd4de')
    entryPhotoX.pack(side=LEFT, padx=5, pady=10)

    Label(framePhotoColumn,text='Y : ', font=("Arial", 13),fg='#BDBEC0', bg = "#363940").pack(side=LEFT, pady=10)
    entryPhotoY = Entry(framePhotoColumn, font=("Arial",17), width=3, bg='#ccd4de')
    entryPhotoY.pack(side=LEFT, padx=5, pady=10)

    Label(framePhotoColumn,text='Size : ', font=("Arial", 13),fg='#BDBEC0', bg = "#363940").pack(side=LEFT, pady=10)
    entryPhotoSize = Entry(framePhotoColumn, font=("Arial",17), width=3, bg='#ccd4de')
    entryPhotoSize.pack(side=LEFT, padx=5, pady=10)

    frameEmailColumn = Frame(frameMain, bg="#363940")
    frameEmailColumn.pack()

    Label(frameEmailColumn,text='"Email" Column : ', font=("Arial", 13),fg='#BDBEC0', bg = "#363940").pack(side=LEFT, pady=10)
    entryEmailColumn = Entry(frameEmailColumn, font=("Arial",17), width=3, bg='#ccd4de')
    entryEmailColumn.pack(side=LEFT, padx=5, pady=10)

    frameEmailLabel = Frame(frameMain, bg="#363940")
    frameEmailLabel.pack()

    labelEmailFields = Label(frameEmailLabel, text="Email Information",fg="#303030", font=("Helvetica", 15), width=100,height=1, bg='#A0A0A0', relief=SUNKEN, border=0)
    labelEmailFields.pack(pady=20)

    frameEmailFields = Frame(frameMain, bg="#363940")
    frameEmailFields.pack()

    Label(frameEmailFields, text="Sender Email ID : ",font=("Arial",13) ,fg='#BDBEC0', bg = "#363940").pack(side=LEFT, padx= 15, pady=15)
    entryEmailID = Entry(frameEmailFields,font=("Arial",13), width= 22, bg='#ccd4de')
    entryEmailID.pack(side=LEFT, padx= 7, pady=15)

    Label(frameEmailFields, text="Sender Password : ",font=("Arial",13) ,fg='#BDBEC0', bg = "#363940").pack(side=LEFT, padx= 15, pady=15)
    entryEmailPassword = Entry(frameEmailFields,font=("Arial",13), width= 22, show="*", bg='#ccd4de')
    entryEmailPassword.pack(side=LEFT, padx= 7, pady=15)

    frameEmailSubject = Frame(frameMain, bg="#363940")
    frameEmailSubject.pack()
    Label(frameEmailSubject, text="Email Subject : ",font=("Arial",13) ,fg='#BDBEC0', bg = "#363940").pack(side=LEFT,padx= 15, pady=15)
    entryEmailSubject = Entry(frameEmailSubject,font=("Arial",13),width= 50, bg='#ccd4de')
    entryEmailSubject.pack(side=LEFT,padx= 15, pady=15)

    frameEmailBody = Frame(frameMain, bg="#363940")
    frameEmailBody.pack()
    Label(frameEmailBody, text="Email Body : ",font=("Arial",13),fg='#BDBEC0', bg = "#363940" ).pack(side=LEFT,padx= 15, pady=15)
    textEmailBody = Text(frameEmailBody,font=("Arial",13),width= 50, height=5, bg='#ccd4de')
    textEmailBody.pack(side=LEFT,padx= 15, pady=15)

    Label(frameMain, text="Please go through README.md to understand every function in its entirety, \nfor example: your Email ID password is different from your email login \npassword, the steps to generate the same are mentioned in README.",fg='#BDBEC0', bg = "#363940").pack(pady=20)

    frameProceedButtons = Frame(frameMain, bg="#363940")
    frameProceedButtons.pack(side=BOTTOM)

    buttonGenerateTestCertificate = Button(frameProceedButtons, text="Generate Test Certificate", command=lambda: createPDF(1))
    buttonGenerateTestCertificate.pack(side=LEFT,padx=7)

    buttonSendTestEmail = Button(frameProceedButtons, text="Send Test Email", command=lambda: sendEmail(1))
    buttonSendTestEmail.pack(side=LEFT,padx=7)

    #Add a warning window
    buttonGenerateAllCertificates = Button(frameProceedButtons, text="Generate All Certificates", command=generateAllCertificatesAndEmail)
    buttonGenerateAllCertificates.pack(side=LEFT,padx=7)

    buttonGenerateAllCertificates = Button(frameProceedButtons, text="Email All", command=lambda: sendEmail(0))
    buttonGenerateAllCertificates.pack(side=LEFT,padx=7)



def createFirstWindowFunction():
    firstWindow = Tk()
    firstWindow.geometry('700x440')
    firstWindow.resizable(0,0)

    projectNameFrame = Frame(firstWindow, bg = '#363940')
    projectNameFrame.place(relx=.5, rely=.5,anchor= CENTER)


    entryProjectName = Entry(projectNameFrame, font = ("Helvetica", 17), bg='#d5ed9d')
    entryProjectName.insert(0,"MyFirstCertificate")
    entryProjectName.pack(side=TOP, pady=10)



    def buttonPress():
        if(entryProjectName.get() != ""):
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
        else:
            print("Project name cannot be null")
            messagebox.showerror(title="Project Name cannot be empty", message="Try a different name" )


    right_arrow_blue = PhotoImage(file="source_images/right_arrow_blue.png")
    buttonSaveProjectName = Button(projectNameFrame, text=" Create Project", font=("Arial",11), activebackground='#363940',command=buttonPress, image=right_arrow_blue,compound=LEFT).pack(side=TOP, pady=10)
    label = Label(projectNameFrame, text="""A folder with your project name will be created in current directory,\n to store temporary and final files (pdfs) to be emailed. \nOnce created, you can access them without using this application.\n\nPlease do not use same folder names and refrain \nfrom using forward/back slash, as it can cause issues \nfetching attachments from source.""",fg='#BDBEC0', bg = "#363940", font=("Arial",11))
    label.pack(pady=10)
    firstWindow.title("Certificate Generator")
    firstWindow['bg'] = '#363940'

    firstWindow.mainloop()

createFirstWindowFunction()









