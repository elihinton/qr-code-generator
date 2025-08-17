'''
description: creates a qr code for a given link, with optional custom sizing, border, and color parameters
script usage: 
    python qr_code.py <link> <outputfilename.png>
    python qr_code.py <link> <size> <border> <outputfilename.png>
    python qr_code.py <link> <size> <border> <content-color>  <bg-color> <outputfilename.png>
    python qr_code.py <link> <content-color> <bg-color> <outputfilename.png> 
'''

import sys
import os
import subprocess
import qrcode


def parseArguments(args):
    # defaults
    size = 10
    border = 4
    content_color = "black"
    bg_color = "white"

    argc = len(args)

    if argc == 3:
        # <link> <outputfilename.png>
        link, outputfile = args[1], args[2]

    elif argc == 5:
        # Case 2: <link> <size> <border> <outputfilename.png>
        # Case 4: <link> <content-color> <bg-color> <outputfilename.png>
        if args[2].isdigit() and args[3].isdigit():
            # Size/border mode
            size = int(args[2])
            border = int(args[3])
            if size <= 0 or border < 0:
                sys.exit("Error: size must be > 0 and border >= 0.")
            link, outputfile = args[1], args[4]
        else:
            # Color mode
            link, content_color, bg_color, outputfile = args[1], args[2], args[3], args[4]

    elif argc == 7:
        # <link> <size> <border> <content-color> <bg-color> <outputfilename.png>
        if not args[2].isdigit() or not args[3].isdigit():
            sys.exit("Error: size and border must be integers.")
        size = int(args[2])
        border = int(args[3])
        if size <= 0 or border < 0:
            sys.exit("Error: size must be > 0 and border >= 0.")
        link, content_color, bg_color, outputfile = args[1], args[4], args[5], args[6]

    else:
        sys.exit(
            "Invalid number of arguments.\n"
            "Usage:\n"
            "  python qr_code.py <link> <outputfilename.png>\n"
            "  python qr_code.py <link> <size> <border> <outputfilename.png>\n"
            "  python qr_code.py <link> <content-color> <bg-color> <outputfilename.png>\n"
            "  python qr_code.py <link> <size> <border> <content-color> <bg-color> <outputfilename.png>"
        )

    # ensures PNG extension
    if not outputfile.lower().endswith(".png"):
        outputfile += ".png"

    return {
        "link": link,
        "size": size,
        "border": border,
        "content_color": content_color,
        "bg_color": bg_color,
        "outputfile": outputfile
    }


# creates the qr code image in cd with custom size, border and colors available
def createQrCode(opts):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = opts["size"],
        border = opts["border"],
    )

    qr.add_data(opts["link"])
    qr.make(fit = True)

    img = qr.make_image(fill_color = opts["content_color"], back_color = opts["bg_color"])
    type(img)
    img.save(opts["outputfile"])


# show the image in preview tool
def showImage(filePath):
    platform = sys.platform
    if platform.startswith("darwin"):
        subprocess.run(["open",filePath])
    elif platform.startswith("win"):
        os.startfile(filePath)
    elif platform.startswith("linux"):
        subprocess.run(["xdg-open",filePath])
    else:
        print(f"Unsupported OS: Cannot Auto-open file, {filePath}")


def main():
    opts = parseArguments(sys.argv)
    createQrCode(opts)
    showImage(opts["outputfile"])
    

if __name__ == "__main__":
    main()
    