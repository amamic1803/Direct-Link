import pyperclip
import tkinter as tk
import sys
import os


def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except AttributeError:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def gen_link():
	pass

	full_link = input("Google Drive link: ")

	full_link_list = full_link.split("/")

	if len(full_link_list[5]) != 33:
		print("Invalid link!")
	else:
		print("https://drive.google.com/uc?export=download&id=" + str(full_link_list[5]))
		pyperclip.copy("https://drive.google.com/uc?export=download&id=" + str(full_link_list[5]))

def gen_click(event):
	pass

def paste_click(event):
	clipboard = pyperclip.paste()

def gui():
	global link_entry

	root = tk.Tk()
	root.title("Direct-Link")
	root.geometry(f"800x190+{root.winfo_screenwidth() // 2 - 400}+{root.winfo_screenheight() // 2 - 95}")
	root.config(background="#FFC0CB")
	root.resizable(False, False)
	root.iconbitmap(resource_path("data\\icon.ico"))

	title = tk.Label(text="Direct-Link", font=("Gabriola", 75, "italic", "bold"),
	                 foreground="white", activeforeground="white",
	                 background="#FFC0CB", activebackground="#FFC0CB",
	                 highlightthickness=0, borderwidth=0)
	title.place(x=0, y=0, width=750, height=100)

	link_label = tk.Label(text="LINK:", font=("Gabriola", 30, "bold"),
	                      foreground="white", activeforeground="white",
	                      background="#FFC0CB", activebackground="#FFC0CB",
	                      highlightthickness=0, borderwidth=0)
	link_label.place(x=0, y=125, width=100, height=35)

	link_entry = tk.Entry(font=("Helvetica", 11), justify=tk.CENTER, insertbackground="white",
	                      foreground="white", disabledforeground="white",
	                      background="#E5ACB6", disabledbackground="#E5ACB6",
	                      highlightthickness=2, highlightcolor="white", highlightbackground="white",
	                      borderwidth=0)
	link_entry.place(x=100, y=125, width=500, height=35)

	paste_btn = tk.Label(text="Paste", font=("Gabriola", 25, "bold"),
	                     foreground="white", activeforeground="white",
	                     background="#FFCCD5", activebackground="#FFCCD5",
	                     highlightthickness=3, highlightcolor="white", highlightbackground="white",
	                     borderwidth=0)
	paste_btn.place(x=600, y=125, width=75, height=35)
	paste_btn.bind("<Enter>", lambda event: paste_btn.config(background="#FFD9DF", activebackground="#FFD9DF"))
	paste_btn.bind("<Leave>", lambda event: paste_btn.config(background="#FFCCD5", activebackground="#FFCCD5"))
	paste_btn.bind("<ButtonRelease-1>", paste_click)

	gen_btn = tk.Label(text="Generate", font=("Gabriola", 25, "bold"),
	                   foreground="white", activeforeground="white",
	                   background="#FFCCD5", activebackground="#FFCCD5",
	                   highlightthickness=3, highlightcolor="white", highlightbackground="white",
	                   borderwidth=0)
	gen_btn.place(x=675, y=125, width=125, height=35)
	gen_btn.bind("<Enter>", lambda event: gen_btn.config(background="#FFD9DF", activebackground="#FFD9DF"))
	gen_btn.bind("<Leave>", lambda event: gen_btn.config(background="#FFCCD5", activebackground="#FFCCD5"))
	gen_btn.bind("<ButtonRelease-1>", gen_click)

	root.mainloop()

def main():
	gui()


if __name__ == "__main__":
	main()
