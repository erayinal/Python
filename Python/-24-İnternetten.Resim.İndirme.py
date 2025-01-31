import urllib.request


url1 = "https://industryolog.com/wp-content/uploads/2020/12/python-socket-programming.jpg"
url2 = "https://industryolog.com/wp-content/uploads/2020/12/python-socket-programming.jpg"

urlliste = [url1 , url2]

sayı = 1

for url in urlliste:
    urllib.request.urlretrieve(url , "Resim " + str(sayı)+".jpg")
    sayı = sayı + 1









