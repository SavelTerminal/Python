# GIF Creator 🖼️

**Python script** that creates a GIF from multiple images.

## Overview
This project automates the creation of a **GIF animation** by combining multiple images into a single file.

## What it does
- **Loads images** from a folder
- **Combines images** into an animated GIF
- **Controls frame duration** and looping

## How it works
- Uses the **imageio** library
- Reads image paths sequentially
- Writes the final GIF to an **output folder**

## Requirements
- **Python 3.x**
- imageio

Install dependency:
    pip install imageio

## Usage
1. Place images inside the **Assets/** folder
2. Run the script:
    python GIF_creator.py
3. Find the generated GIF inside the **Output/** folder

## Output
- One **.gif file** generated from the input images

## Notes
Built as a learning project to practice **file handling** and **basic automation**.

## Possible improvements
- **Add CLI arguments**
- **Support image sorting** by name or date
