import qrcode

data = input("Enter the URL: ")
filename = input("Enter the filename: ")
filename += ".png"
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)  # Ensures proper QR code sizing
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f"QR code saved as {filename}")
