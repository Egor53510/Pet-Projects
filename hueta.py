import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10, border=4)
qr.add_data('https://i.ytimg.com/vi/tks-7oaBExk/maxresdefault.jpg')
qr.make(fit=True)

img = qr.make_image(fill_color="black", black_color="white")
img.show()