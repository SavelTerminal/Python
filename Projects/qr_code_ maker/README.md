# QR Code Maker 📱

**Python script** that generates a QR code from a URL.

## Overview
This project creates a **QR code image** starting from a simple text string or website link.

## What it does
- **Takes a URL** as input
- **Generates a QR code**
- **Saves the result** as a PNG image

## How it works
- Uses the **qrcode** library
- Applies **basic size and border configuration**
- Exports a **black-and-white PNG image**

## Requirements
- **Python 3.x**
- qrcode

Install dependency:
    pip install qrcode[pil]

## Usage
1. Edit the **website_link** variable in the script
2. Run:
    python Qr_code_maker.py
3. The QR code image will be saved **locally**

## Output
- One **.png QR code image**

## Notes
Created to practice **third-party libraries** and **image generation**.

## Possible improvements
- **Add color customization**
- **Accept user input** from CLI
