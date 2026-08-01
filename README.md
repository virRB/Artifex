# Artifex

## What is **Artifex?**
**Artifex** is a image to abstract art converter.
- Fast
- Easy to use
- No AI
- Runs locally on your machine

### Input 
- [Wikimedia Commons, Adam Schultz, Public 
domain](https://commons.wikimedia.org/wiki/File:Joe_Biden_presidential_portrait.jpg)

![input](biden.jpg)

### Output
![output](output.jpg)

## Dependencies
- [Python 3.9+](https://www.python.org/)
- Pillow
```bash
pip install pillow
```
- **Artifex** is currently only supported for *Windows*

## Get Started
- First, run `installer.py`
- Then, restart your terminal *(So windows PATH can update properly)*
- You can now use the `artifex` command!

### Commands
```bash
artifex <image1.jpg>
```
Converts the image and stores it as `output.jpg`

```bash
artifex <image1.jpg> --save <custom-file.jpg>
```
Saves the output with a custom filename
```bash
artifex <image1.jpg> --show
```
Converts the image and opens up a window to display it
```bash
artifex <image1.jpg> --size <amount>
```
Changes the image size of the output *(default 500)*
```bash
artifex <image1.jpg> --border-thickness <amount>
```
Changes the border thickness of the output *(default 3)*

**These attributes can be stacked:**
```bash
artifex <image1.jpg> --save <custom-file.jpg> --size 200 --border-thickness 5 --show
```