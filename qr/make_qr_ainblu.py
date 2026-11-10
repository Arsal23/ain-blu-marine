import qrcode
import qrcode.image.svg

URL = "https://ain-blu-marine.vercel.app"

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=30,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)
img = qr.make_image(fill_color="#0b1230", back_color="white")  # navy, matches the page
img.save("ain-blu-marine-qr.png")

svg = qrcode.make(URL, image_factory=qrcode.image.svg.SvgPathImage)
svg.save("ain-blu-marine-qr.svg")

print("Done: ain-blu-marine-qr.png aur ain-blu-marine-qr.svg ban gayi")
