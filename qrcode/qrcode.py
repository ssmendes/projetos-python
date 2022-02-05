pip install qrcode

import qrcode

img=qrcode.make('https://google.com')
img.save('qrcode.png')