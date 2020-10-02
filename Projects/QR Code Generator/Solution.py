import pyqrcode
import os
import qrcode
import pandas as pd
email =""
def createQRCode():
    '''
    We need are creating files to store the qr codes 
    This program can generate Qr codes in two fromat 
    image type 
    svg fromat to be used in html templates, to be sent as email
    '''
    os.system("mkdir asHTML")
    os.system("mkdir asPNG")
    df = pd.read_csv("Sample.csv") # well use the csv of your choice

    
    for index, values in df.iterrows():
        email = values["Member email"]
        name = values["Member names"]
        data = f'''
        Email: {email}\n    # now we can add more fields to the f string 
        '''

        #Created as a Scalable vector Graphic (svg)
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