from PIL import Image
import os


folderPath = 'FingerImages'


for i in os.listdir(folderPath):
    image = Image.open(f'{folderPath}/{i}')
    image = image.resize((500,500),Image.ANTIALIAS)
    image.save(fp=f"FingIm/{i}.png")
    print(i)