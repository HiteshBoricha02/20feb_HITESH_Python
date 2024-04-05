import pyqrcode

url="https://www.instagram.com/abhisheksingh.02/"

qr=pyqrcode.create(url)

qr.png("Abhshek_singh.png")