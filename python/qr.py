#!/usr/bin/env python
import qrcode 
img = qrcode.make('haoshoudi')
img.save('qr.png')
