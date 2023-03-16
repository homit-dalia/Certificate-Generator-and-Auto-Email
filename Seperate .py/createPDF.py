from fpdf import FPDF
from PIL import Image


imgSource = "template.jpg"

img = Image.open(imgSource)


width = img.width *25.4 / 128
height = img.height *25.4 / 128
dpi = img.info['dpi']

print("The height of the image is: ", height)
print("The width of the image is: ", width)
print("The size of the image is: ", dpi)


page1 = FPDF('l', 'mm', [height,width])

page1.add_page()

page1.image(imgSource, 0, 0, w = width, h=height )

page1.set_font("Arial",size=50)
page1.text(20,20,"Hello")

page1.output("Certi1.pdf")