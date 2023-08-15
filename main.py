import qrcode
url = input("enter  url : ")
features = qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data(url)
features.make(fit=True)
genarate_image = features.make_image(fill_color = "Black", back_color = "Whiite")
genarate_image.save("QR CODE.png")


