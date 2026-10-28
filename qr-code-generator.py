import qrcode

data = input("Enter text or URL : ")
# qr = qrcode.make(data)
qr = qrcode.QRCode()
# qr.save("myqr.png")
qr.add_data(data)
qr.make()
qr.print_ascii()
print("QR Code Generated Successfully!")