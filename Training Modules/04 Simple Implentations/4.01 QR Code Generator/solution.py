import pyqrcode
import os
import qrcode
import pandas as pd
email =""
def createQRCode():
    os.system("mkdir asHTML")#creating a file asHTML
    os.system("mkdir asPNG")#creating a file asPNG
    df = pd.read_csv(" Any.csv")# in order to use this program the data should be entered as a csv
    for index, values in df.iterrows():
        email = values["Member email"]
        name = values["Member names"]# we can add more fields if needed
        data = f'''
        Email: {email}\n
        '''

        # this is if we want to share the qr code as an email template, this formats looks the best
        image = pyqrcode.create(data)
        image.svg(f"asHTML/{email}.svg", scale="5")

        # Create qr code instance
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4,
        )
        # Add data
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image()

        # Save it somewhere, change the extension as needed:
        # img.save("image.png")
        # img.save("image.bmp")
        # img.save("image.jpeg")
        img.save(f"asPNG/{email}.jpg")

        print(" QR created and saved for"+name)


createQRCode()
