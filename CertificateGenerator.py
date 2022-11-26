#Format of userData.csv file should be - [email,name,imageURL]

from pdf_mail import sendpdf
import csv
import urllib.request
from fpdf import FPDF

#call each functions in sequence

def sendEmail():
    with open('userData.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        for lines in data:
            print ("Sending Email to " + lines[0])

            sender = '9898dalia@gmail.com'
            receiver = lines[0]
            #remove/change password before printing
            password='nkzgyfdoviqzpwje' #empty for security reasons
            subject = 'Certificate of Participation for ' + lines[1]
            text = """Dear """ + lines[1] + """ ,
                                Congratulations for successfully attending an ISTE approved E-Webinar on
                    “Machine Learning” on 20th October, 2022, organized by CO, CKPCET.
    Regards,
    Webinar Coordinator"""

            k = sendpdf(    sender,
                            receiver,
                            password,
                            subject,
                            text, 
                            lines[1],
                            "D:/Study - Extra/Python Projects/OutputCertificates") 
                            #change this directory
            k.email_send()
            print("Certificate sent")

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

                print("Image Downloaed")

def createPDF():
    with open('userData.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        for lines in data:
            image = "Hello " + lines[0]
            print ("Creating PDF for participant " + lines[1])

            lenName = len(lines[1])

            nameInCertificate=''
            for i in range(int((60-lenName)/2)):
                nameInCertificate+='-'
            nameInCertificate+=' '
            nameInCertificate+=lines[1]
            nameInCertificate+=' '
            for i in range(int((60-lenName)/2)):
                nameInCertificate+='-'
                

            #change directory
            imagePath = "D:/Study - Extra/Python Projects/ImageDisplay/" + lines[1] + ".jpg"
            fpdf = FPDF()
            body = FPDF()
            heading = FPDF()
            bottomBold = FPDF()
            bottomLight = FPDF()

            fpdf.add_page('l')
            body = fpdf
            bottomBold = fpdf
            bottomLight = fpdf
            heading = fpdf

            fpdf.set_font("Arial",size=50)
            fpdf.set_text_color(48,107,149)
            fpdf.add_link()
            

            fpdf.text(9,30,txt="Certificate of Participation")
            fpdf.image("collegeLogo.png", 230,8,w=50)

            heading.set_font("Helvetica",size=15)
            heading.set_text_color(200,0,0)
            heading.write(60,"C.K. Pithawala College of Engineering and Technology","https://ckpcet.ac.in/")
            
            body.set_font("Courier",size=21)
            body.set_text_color(0,107,0)

            body.multi_cell(0,10,"\n\n\n\n\n\n\n\n\n\n"); 
            body.image(imagePath,240, 60, w = 35)
            body.image("excellence.png", 15, 62, w = 40)
        ##
            fpdf.multi_cell(0, 10, "This is to certify that \n"+nameInCertificate+"\nfrom CKPCET has successfully participated in an E-Webinar on Machine Learning on October 20, 2022 organized at Computer Engineering Department.", border = 0)

            bottomBold.set_font("Arial",size=17)
            bottomBold.set_text_color(0,0,0)
            bottomBold.text(5, 200, "Coordinator and Head, CO:")
            bottomBold.text(240, 200, "Principal:")

            bottomLight.set_font("Helvetica",size=14)
            bottomLight.set_text_color(0,0,0)
            bottomLight.text(5, 205, "Dr. Ami T. Choksi")
            bottomLight.text(240, 205, "Dr. Anish H. Gandhi")

            bottomLight.image("hodSign.png", 20, 180, w = 40 )
            bottomLight.image("principalSign.png", 240, 177, w = 40 )

            pdfName ="OutputCertificates/" + lines[1] + ".pdf"

            body.output(pdfName)
            fpdf.output(pdfName)
            heading.output(pdfName)
            bottomBold.output(pdfName)
            bottomLight.output(pdfName)

            print("PDF Created")
    
imageDownloader()
createPDF()
sendEmail()
