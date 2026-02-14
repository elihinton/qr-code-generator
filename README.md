# QR Code Generator

A simple, flexible QR code generator available in both **Python** and **JavaScript (web)** versions. Easily create QR codes for any URL with optional customization for size, border, and colors.

<p align="center">
  <img src="assets/example.png" alt="QR Code Generator in Web browser" width="600" style="text-align: center;">
</p>

---

## Python Script Version

### Overview
This Python script generates QR codes from any URL and allows for optional customization of:

- QR code **size** (number of pixels per box)
- **Border width**
- **Content color** (QR code color)
- **Background color**
- Output **filename**

It also automatically previews the generated QR code using your system's default image viewer.

### Features
- Quick generation from the command line
- Optional customization for design
- Automatic PNG output
- Cross-platform image preview

### Installation
Make sure Python is installed, then install dependencies:

```bash
pip install qrcode[pil]
```

### Usage
There are various customisations available for QR code generation engrained in this script. The allowed formats can be seen below.
```bash
python qr_code.py <link> <outputfilename.png>
python qr_code.py <link> <size> <border> <outputfilename.png>
python qr_code.py <link> <size> <border> <content-color>  <bg-color> <outputfilename.png>
python qr_code.py <link> <content-color> <bg-color> <outputfilename.png> 
```
For example, the following is valid:
```bash
python qr_code.py https://youtube.com 10 4 red black yt_qrcode.png
```
## Use Cases
- Quickly generate QR codes for websites, social media links, or documents
- Customize QR codes for presentations, marketing, or personal projects
- Integrate into other applications or websites
