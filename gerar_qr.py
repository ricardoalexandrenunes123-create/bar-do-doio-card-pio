import qrcode

url = "https://bar-do-doio-card-pio.onrender.com"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr_bar_do_doio.png")

print("QR Code gerado com sucesso!")