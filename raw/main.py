from PIL import Image, ImageFilter, ImageEnhance, ImageTk
import os
import argparse
from tkinter import Label, Tk
import sys

RESET = "\033[0m"
CYAN = "\033[36m"
RED = "\033[91m"
YELLOW = "\033[33m"
ORANGE = "\033[38;5;208m"
BOLD = "\033[1m"
GREEN = "\033[32m"
parser = argparse.ArgumentParser(prog="Artifex")
parser.add_argument("subject")
parser.add_argument("--save", default="output.jpg")
parser.add_argument("--size", type=int, default=500)
parser.add_argument("--border-thickness", type=int, default=3)
parser.add_argument("--show", action="store_true")
argv = parser.parse_args()
if argv.border_thickness % 2 == 0:
    argv.border_thickness += 1
BASE = os.getcwd()
w, h = argv.size, argv.size
SUBJECT = os.path.join(BASE, argv.subject)
if not os.path.exists(SUBJECT):
    print(f"{RED}No such file or directory exists: {SUBJECT}{RESET}")
    sys.exit(1)

SUBJECT = Image.open(SUBJECT).convert("RGB")
SUBJECT = SUBJECT.resize((w, h))
SUBJECT = SUBJECT.filter(ImageFilter.GaussianBlur(radius=10))
RESULT = os.path.join(BASE, argv.save)

pixels_s = SUBJECT.load()
output = Image.new("RGB", (w, h))
pixels = output.load()

def normalize(pixel: tuple[int, int, int], strength: int=32) -> tuple[int, int, int]:
    r, g, b = pixel
    return (r//strength*strength, g//strength*strength, b//strength*strength)

def run() -> None:
    for x in range(w):
        for y in range(h):
            pixels[x, y] = normalize(pixels_s[x, y], strength=16)
            pixels[x, y] = normalize(pixels[x, y], strength=32)

def make_edges(enhance: int = 10, thickness: int=5) -> Image:
    edges = output.convert("L").filter(ImageFilter.FIND_EDGES)
    edges = ImageEnhance.Contrast(edges).enhance(enhance)
    edges = edges.filter(ImageFilter.MaxFilter(thickness))
    return edges.convert("RGB")

def mask() -> Image:
    edges = make_edges(enhance=50, thickness=argv.border_thickness)
    pixels_e = edges.load()
    masked = Image.new("RGB", (w, h))
    pixels_m = masked.load()
    for x in range(w):
        for y in range(h):
            pixel_edge = pixels_e[x, y]
            pixel = pixels[x, y]
            if not (pixel_edge == (0, 0, 0)):
                pixels_m[x, y] = (0, 0, 0)
            else:
                pixels_m[x, y] = pixel
    return masked

run()
mask().save(RESULT)

if argv.show:
    root = Tk()
    root.title("Artifex")
    img = Image.open(RESULT)
    img = ImageTk.PhotoImage(img)
    label = Label(root, image=img)
    label.image = img
    label.pack()
    root.mainloop()