import urllib.request


image_url= "https://drive.google.com/file/d/1jqPvr89xn3LDoL_nGQ6teDwBKiQHoIft/view?usp=share_link" + ".png"
#does not work with drive links
filename = "test.jpg"
urllib.request.urlretrieve(image_url, filename)