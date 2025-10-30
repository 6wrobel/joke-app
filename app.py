import tkinter as tk
from tkinter import ttk
import pyjokes


langs = ["en", "de", "it"]
cats = ["neutral", "chuck", "all"]


def click_button(cat):
    if cat == "random":
        joke_label.config(text=str(pyjokes.get_joke("en", "all")))
    elif cat == "chuck":
        joke_label.config(text=str(pyjokes.get_joke("en", "chuck")))
    elif cat == "neutral":
        joke_label.config(text=str(pyjokes.get_joke("en", "neutral")))


def copy_joke():
    text = joke_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(text)


# App window
root = tk.Tk()
root.title("Joke Generator")
root.minsize(480,300)


# Sections
top = tk.Frame(root, bg="#e9e9e9", height=60)   # header area
top.pack(fill="x")                              # stretch horizontally

mid = tk.Frame(root, bg="white")               # content area
mid.pack(fill="both", expand=True)             # stretch both ways, take extra space

bottom = tk.Frame(root, bg="#e9e9e9", height=80) # buttons area
bottom.pack(fill="x")


# Labels
title_label = tk.Label(top, text='Welcome to the famous joke generator!', font=("Comic Sans MS", 16, "bold"), bg="#e9e9e9")
title_label.pack(pady=10)

joke_label = tk.Label(mid, text="No joke, yet!", font=("Comic Sans MS", 12))
joke_label.pack(padx=10, pady=10, fill="both", expand=True)


# Buttons/fields
button_random = tk.Button(bottom, text="Get a random joke", width=25, height=2, command= lambda: click_button("random"))
button_random.grid(row=0, column=0, padx=4, pady=4)

button_chuck = tk.Button(bottom, text="Get a Chuck Norris joke", width=25, height=2, command= lambda: click_button("chuck"))
button_chuck.grid(row=1, column=0, padx=4, pady=4)

button_neutral = tk.Button(bottom, text="Get a neutral joke", width=25, height=2, command= lambda: click_button("neutral"))
button_neutral.grid(row=2, column=0, padx=4, pady=4)

button_copy = tk.Button(bottom, text="Copy to clipboard", width=25, height=2, command=copy_joke)
button_copy.grid(row=3, column=0, padx=4, pady=4)


bottom.grid_columnconfigure(0, weight=1)

root.mainloop()