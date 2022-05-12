# import modules
import qrcode
from PIL import Image

# taking image which user wants
# in the QR code center
lg=input("enter logo link:")
Logo_link = 'ivis.png'
if len(lg)==0:
    logo = Image.open(Logo_link)
else:
    logo = Image.open(lg)

# taking base width
basewidth = 100

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# taking url or text
url= input("enter url:")
# taking qrcode saved name or text
qrimg=input("qrimg name:")
# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = 'orange'

# adding color to QR code
QRimg = QRcode.make_image(
	fill_color=QRcolor, back_color="black").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
	(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('{}.png'.format(qrimg))

print('QR code generated!')



