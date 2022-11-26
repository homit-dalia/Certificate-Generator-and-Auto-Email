import urllib.request

image_url= "https://i.imgur.com/fVVEogF.jpeg"
#does not work with drive links
filename = "ImageDisplay/trees.jpg"
urllib.request.urlretrieve(image_url, filename)