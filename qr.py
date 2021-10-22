import qrcode
from PIL import Image

img = qrcode.make('You can input here text/url/name etc')

img.save("sample.png") # instead of sample.png you can write any name of your choice