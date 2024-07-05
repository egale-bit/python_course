#!/usr/bin/env python3

#qr code generator.

import segno

content = input("Enter your content: ")
newfile= input("Give a qrcode file name(use image format like, png, jpg..): ")
qr = segno.make_qr(content)
qr.save(
    newfile,
    scale=5,
    border=10
)


