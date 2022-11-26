from fpdf import FPDF
import pandas as pd


def createPDF():

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
    fpdf.image("eagle.png", 230,5,w=45)

    heading.set_font("Helvetica",size=15)
    heading.set_text_color(200,0,0)
    heading.write(60,"C.K. Pithawala College of Engineering and Technology","https://ckpcet.ac.in/")
    
    body.set_font("Courier",size=21)
    body.set_text_color(0,107,0)

    body.multi_cell(0,10,"\n\n\n\n\n\n\n\n\n\n"); 
    body.image("human.png",250, 60, w = 25)
    body.image("excellence.png", 15, 62, w = 40)
##
    fpdf.multi_cell(0, 10, "This is to certify that \n------------------------'Homit Dalia'------------------------ \nfrom CKPCET has successfully participated in an E-Webinar on Machine Learning on October 20, 2022 organized at Computer Engineering Department.", border = 0)

    bottomBold.set_font("Arial",size=17)
    bottomBold.set_text_color(0,0,0)
    bottomBold.text(5, 200, "Coordinator and Head, CO:")
    bottomBold.text(220, 200, "Principal:")

    bottomLight.set_font("Helvetica",size=14)
    bottomLight.set_text_color(0,0,0)
    bottomLight.text(5, 205, "Dr. Ami T. Choksi")
    bottomLight.text(220, 205, "Dr. Anish H. Gandhi")

    bottomLight.image("hodSign.png", 20, 180, w = 40 )
    bottomLight.image("principalSign.png", 220, 175, w = 40 )


    pdfName ="OutputCertificates/" +"Test1.pdf"

    body.output(pdfName)
    fpdf.output(pdfName)
    heading.output(pdfName)
    bottomBold.output(pdfName)
    bottomLight.output(pdfName)
    

createPDF()
