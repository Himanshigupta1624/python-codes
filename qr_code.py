# import qrcode as qr
# img=qr.make("https://face-recognition.readthedocs.io/en/latest/face_recognition.html")
# img.save("himanshi.png")

import qrcode 
from PIL import Image
qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)

qr.add_data("https://face-recognition.readthedocs.io/en/latest/face_recognition.html")

qr.make( fit= True)
img=qr.make_image(fill_color="black",back_color="blue")
img.save("himanshi.png")