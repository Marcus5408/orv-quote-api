import os
import json
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from numpy import add

root = Tk()
root.title("ORV Quote API - Add Quote")
root.iconbitmap("assets/favicon.ico")
root.minsize(500, 320)
root.geometry("500x320")

# define fields
heading_label = Label(root, text="Add Quote", font=("TKDefaultFont", 20, "bold"))

quote_label = Label(root, text="Quote:")
quote_input = Text(root, height=7, wrap="word")
quote_scrollbar = Scrollbar(root, command=quote_input.yview)
quote_input.config(yscrollcommand=quote_scrollbar.set)

import webbrowser

def open_wiki():
    webbrowser.open("https://github.com/<username>/<repository>/wiki")

quote_help_button = Button(root, text="Need Help?", command=lambda: help())

def help():
    help_window = Toplevel(root)
    help_window.title("Help")
    help_window.iconbitmap("assets/favicon.ico")

    help_window_label = Label(help_window, text="Select an option to get help filling out that field.", font=("TKDefaultFont", 20, "bold"))

    tabs = Notebook(help_window)
    quote_help = Frame(tabs)
    author_help = Frame(tabs)
    chapter_help = Frame(tabs)
    episode_help = Frame(tabs)
    episode_name_help = Frame(tabs)

    tabs.add(quote_help, text="Quote")
    tabs.add(author_help, text="Author")
    tabs.add(chapter_help, text="Chapter")
    tabs.add(episode_help, text="Episode Number")
    tabs.add(episode_name_help, text="Episode Name")
    
    

    text = "NOTE: THIS IS A NECESSARY FIELD. If this field is not filled out, your quote request will not be accepted.\n\nPlease keep quotes reasonably long. This means that you shouldn't quote 2 entire paragraphs, nor should you quote just 2 words. That is, of course, those two words are very prominent, such as \"Get lost, Kim Dokja.\""
    # messagebox.showinfo("Quote Info", text)

author_label = Label(root, text="Author:")
author_input = Entry(root)

chapter_label = Label(root, text="Chapter:")
chapter_input = Entry(root)

episode_label = Label(root, text="Episode Number:")
episode_input = Entry(root)

episode_name_label = Label(root, text="Episode Name:")
episode_name_input = Entry(root)

add_quote_button = Button(root, text="Add Quote", command=lambda: add_quote())

quote_label.grid(row=0, column=0, columnspan=2, pady=(10, 0), padx=10, sticky="w")
quote_help_button.grid(row=0, column=1, pady=(5, 0), padx=10, sticky="e")
quote_input.grid(row=1, column=0, columnspan=2, pady=(5, 5), padx=(10, 30), sticky="we")

quote_scrollbar.grid(row=1, column=1, pady=(5, 5), padx=(0, 10), sticky="nse")
quote_input.config(yscrollcommand=quote_scrollbar.set)

author_label.grid(row=2, column=0, pady=(5,5), padx=(10, 0), sticky="w")
author_input.grid(row=2, column=1, pady=(5,5), padx=(5, 10), sticky="we")

chapter_label.grid(row=3, column=0, pady=(5,5), padx=(10, 0), sticky="w")
chapter_input.grid(row=3, column=1, pady=(5,5), padx=(5, 10), sticky="we")

episode_label.grid(row=4, column=0, pady=(5,5), padx=(10, 0), sticky="w")
episode_input.grid(row=4, column=1, pady=(5,5), padx=(5, 10), sticky="we")

episode_name_label.grid(row=5, column=0, pady=(5,5), padx=(10, 0), sticky="w")
episode_name_input.grid(row=5, column=1, pady=(5,5), padx=(5, 10), sticky="we")

add_quote_button.grid(row=6, column=0, columnspan=2, pady=(5, 10), padx=10, sticky="we")

# make column 2 expandable, but column 1 fixed
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)

def add_quote():
    # if any fields are empty, show error
    quote = {
        "quote": quote_input.get("1.0", END),
        "author": author_input.get(),
        "chapter": int(chapter_input.get()),
        "episode": episode_input.get(),
        "episode_name": episode_name_input.get()
    }
    missing_fields = ""
    for key in quote:
        if quote[key] == "\n" or quote[key] == "":
            missing_fields += f"{key}" if missing_fields == "" else f", {key}"
    if missing_fields != "":
        messagebox.showerror("Error", f"Please fill out the {missing_fields} {'field' if missing_fields.count(',') == 0 else 'fields'}.")
        return
    # get quote
    quote["quote"] = quote["quote"].replace("\n", " ")
    # print(quote)
    quote_length = "long" if len(quote["quote"]) >= 150 else "short"
    if quote_length == "short":
        with open("quotes/short_quotes.json", "a") as f:
            json.dump(quote, f)
            f.write("\n")
    else:
        with open("quotes/long_quotes.json", "a") as f:
            json.dump(quote, f)
            f.write("\n")
    messagebox.showinfo("Success", "Quote successfully added!")
    # clear all fields
    quote_input.delete("1.0", END)
    author_input.delete(0, END)
    chapter_input.delete(0, END)
    episode_input.delete(0, END)
    episode_name_input.delete(0, END)


# run the app
if __name__ == "__main__":
    root.mainloop()