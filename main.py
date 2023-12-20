import base64
import os
import sys
import tkinter as tk
from tkinter.messagebox import showinfo, showerror

import pyperclip


def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except AttributeError:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def gen_link(link):
	if "drv.ms" in link:
		return f"""https://api.onedrive.com/v1.0/shares/u!{base64.b64encode(bytes(link, "utf-8")).decode("utf-8")}/root/content"""
	elif "google" in link:
		return f"""https://drive.google.com/uc?export=download&id={link.split("/")[5]}"""
	else:
		return ""


class App:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Direct-Link")
		self.root.geometry(f"800x190"
		                   f"+{self.root.winfo_screenwidth() // 2 - 400}"
		                   f"+{self.root.winfo_screenheight() // 2 - 95}")
		self.root.config(background="#FFC0CB")
		self.root.resizable(False, False)
		self.root.iconbitmap(resource_path("resources/download-icon.ico"))

		self.title = tk.Label(self.root, text="Direct-Link", font=("Gabriola", 75, "italic", "bold"),
		                      foreground="white", activeforeground="white",
		                      background="#FFC0CB", activebackground="#FFC0CB",
		                      highlightthickness=0, borderwidth=0)
		self.title.place(x=0, y=7, width=750, height=100)

		self.link_label = tk.Label(self.root, text="LINK:", font=("Gabriola", 30, "bold"),
		                           foreground="white", activeforeground="white",
		                           background="#FFC0CB", activebackground="#FFC0CB",
		                           highlightthickness=0, borderwidth=0)
		self.link_label.place(x=0, y=125, width=100, height=35)

		self.link_entry = tk.Entry(self.root, font=("Helvetica", 11), justify=tk.CENTER, insertbackground="white",
		                           foreground="white", disabledforeground="white",
		                           background="#E5ACB6", disabledbackground="#E5ACB6",
		                           highlightthickness=2, highlightcolor="white", highlightbackground="white",
		                           borderwidth=0)
		self.link_entry.place(x=100, y=125, width=500, height=35)

		self.paste_btn = tk.Label(self.root, text="Paste", font=("Gabriola", 25, "bold"), cursor="hand2",
		                          foreground="white", activeforeground="white",
		                          background="#FFCCD5", activebackground="#FFCCD5",
		                          highlightthickness=3, highlightcolor="white", highlightbackground="white",
		                          borderwidth=0)
		self.paste_btn.place(x=600, y=125, width=75, height=35)
		self.paste_btn.bind("<Enter>", lambda event: self.paste_btn.config(background="#FFD9DF", activebackground="#FFD9DF"))
		self.paste_btn.bind("<Leave>", lambda event: self.paste_btn.config(background="#FFCCD5", activebackground="#FFCCD5"))
		self.paste_btn.bind("<ButtonRelease-1>", lambda event: self.paste_click())

		self.gen_btn = tk.Label(self.root, text="Generate", font=("Gabriola", 25, "bold"), cursor="hand2",
		                        foreground="white", activeforeground="white",
		                        background="#FFCCD5", activebackground="#FFCCD5",
		                        highlightthickness=3, highlightcolor="white", highlightbackground="white",
		                        borderwidth=0)
		self.gen_btn.place(x=675, y=125, width=125, height=35)
		self.gen_btn.bind("<Enter>", lambda event: self.gen_btn.config(background="#FFD9DF", activebackground="#FFD9DF"))
		self.gen_btn.bind("<Leave>", lambda event: self.gen_btn.config(background="#FFCCD5", activebackground="#FFCCD5"))
		self.gen_btn.bind("<ButtonRelease-1>", lambda event: self.gen_click())

		self.root.mainloop()

	def paste_click(self):
		self.link_entry.delete(0, tk.END)
		self.link_entry.insert(0, pyperclip.paste())

	def gen_click(self):
		generated_link = gen_link(self.link_entry.get())

		if len(generated_link) == 0:
			showerror(title="Error!", message="Generating direct download link failed!\nCheck link and try again!", parent=self.root)
		else:
			pyperclip.copy(generated_link)
			showinfo(title="Success!", message="Direct download link copied to clipboard!", parent=self.root)


def main():
	App()


if __name__ == "__main__":
	main()
